from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class CreateShortURL(APIView):
    """
    API endpoint for creating a short URL.
    Requires user authentication.
    
    """
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "CreateShortURL works"}, status=status.HTTP_200_OK)


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
