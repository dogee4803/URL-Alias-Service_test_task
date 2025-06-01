from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class CreateShortURL(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        return Response({"message": "CreateShortURL works"}, status=status.HTTP_200_OK)


class URLListView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({"message": "URLListView works"}, status=status.HTTP_200_OK)


class DeactivateURL(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk=None):
        return Response({"message": "DeactivateURL works"}, status=status.HTTP_200_OK)


class RedirectToOriginalView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, short_code):
        
        original_url = "https://example.com"

        if original_url:
            return HttpResponseRedirect(original_url)
        else:
            raise Http404("URL not found")
