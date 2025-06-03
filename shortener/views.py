from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from .models import ShortURL
from .serializers import ShortURLCreateSerializer

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
        return Response({"message": "URLListView works"}, status=status.HTTP_200_OK)


class DeactivateURL(APIView):
    """
    API endpoint for deactivating a short URL.
    Requires user authentication.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        return Response({"message": "DeactivateURL works"}, status=status.HTTP_200_OK)


class RedirectToOriginalView(APIView):
    """
    API endpoint for redirecting to the original URL using a short code.
    Accessible by any user (no authentication required).

    """
    permission_classes = [AllowAny]

    def get(self, request, short_code):

        original_url = "https://example.com"

        if original_url:
            return HttpResponseRedirect(original_url)
        raise Http404("URL not found")
