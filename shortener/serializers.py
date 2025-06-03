from rest_framework import serializers
from .models import ShortURL

class ShortURLCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a short URL.
    
    """
    class Meta:
        model = ShortURL
        fields = ['original_url']