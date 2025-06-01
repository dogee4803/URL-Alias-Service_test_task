from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CreateShortURL(APIView):
    def post(self, request):
        return Response({"message": "CreateShortURL works"}, status=status.HTTP_200_OK)


class URLListView(APIView):
    def get(self, request):
        return Response({"message": "URLListView works"}, status=status.HTTP_200_OK)


class DeactivateURL(APIView):
    def post(self, request, pk=None):
        return Response({"message": "DeactivateURL works"}, status=status.HTTP_200_OK)


class RedirectToOriginalView(APIView):
    def get(self, request, short_code):
        
        original_url = "https://example.com"

        if original_url:
            return HttpResponseRedirect(original_url)
        else:
            raise Http404("URL not found")
