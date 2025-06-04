from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from .models import ShortURL, Click
from .serializers import ShortURLCreateSerializer, ShortURLListSerializer, ShortURLStatsSerializer

# Create your views here.

class CreateShortURL(APIView):
    """
    API endpoint for creating a short URL.
    Requires user authentication.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShortURLCreateSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            short_code = ShortURL.generate_unique_short_code()
            short_url = ShortURL.objects.create(
                original_url=original_url,
                short_code=short_code
            )
            return Response({
                'original_url': short_url.original_url,
                'short_code': short_url.short_code,
                'short_url': request.build_absolute_uri(f'/{short_url.short_code}/')
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class URLListView(APIView):
    """
    API endpoint for listing all URLs for the authenticated user.
    Requires user authentication.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = ShortURL.objects.all()
        serializer = ShortURLListSerializer(url, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeactivateURL(APIView):
    """
    API endpoint for deactivating a short URL.
    Requires user authentication.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, short_code):
        try:
            short_url = ShortURL.objects.get(short_code=short_code)
        except ShortURL.DoesNotExist:
            return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)
        short_url.is_active = False
        short_url.save()
        return Response({"message": "Short URL deactivated"}, status=status.HTTP_200_OK)


class RedirectToOriginalView(APIView):
    """
    API endpoint for redirecting to the original URL using a short code.
    Accessible by any user (no authentication required).

    """
    permission_classes = [AllowAny]

    def get(self, request, short_code):
        try:
            short_url = ShortURL.objects.get(short_code=short_code)
        except ShortURL.DoesNotExist:
            return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)

        if not short_url.is_actual:
            if short_url.is_active and short_url.is_expired():
                short_url.is_active = False
                short_url.save(update_fields=['is_active'])
            return Response(
                    {"error": "Short URL is inactive or expired"},
                    status=status.HTTP_410_GONE)
        
        Click.objects.create(short_url=short_url)
        
        short_url.save()

        return Response(
                {"original_url": short_url.original_url},
                status=status.HTTP_302_FOUND,
                headers={"Location": short_url.original_url})


class GlobalStatsView(APIView):
    """
    API endpoint for retrieving global statistics of all short URLs.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Получаем все ссылки и сортируем по total_clicks (сначала самые популярные)
        urls = list(ShortURL.objects.all())
        urls.sort(key=lambda url: url.total_clicks(), reverse=True)
        serializer = ShortURLStatsSerializer(urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

