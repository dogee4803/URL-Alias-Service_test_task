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
        fields = ['short_code', 'original_url', 'is_active', 'created_at', 'expire_at',]
        read_only_fields = ['short_code', 'created_at', 'expire_at']
        
        
class ShortURLStatsSerializer(serializers.ModelSerializer):
    """
    Serializer for short URL statistics.
    
    """
    clicks_last_hour = serializers.SerializerMethodField()
    clicks_last_day = serializers.SerializerMethodField()
    total_clicks = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['short_code', 'original_url', 'clicks_last_hour', 'clicks_last_day', 'total_clicks']

    def get_clicks_last_hour(self, obj):
        return obj.clicks_last_hour()

    def get_clicks_last_day(self, obj):
        return obj.clicks_last_day()

    def get_total_clicks(self, obj):
        return obj.total_clicks()
