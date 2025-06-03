from rest_framework import serializers
from .models import ShortURL

class ShortURLCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a short URL.

    """
    class Meta:
        model = ShortURL
        fields = ['original_url']


class ShortURLListSerializer(serializers.ModelSerializer):
    """
    Serializer for listing short URLs.
    
    """
    class Meta:
        model = ShortURL
        fields = ['short_code', 'original_url', 'is_active', 'created_at', 'expire_at', 'click_count']
        read_only_fields = ['short_code', 'created_at', 'expire_at', 'click_count']
