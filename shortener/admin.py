from django.contrib import admin
from .models import ShortURL

# Register your models here.
@admin.register(ShortURL)
class ShortURLAdmin(admin.ModelAdmin):
    """
    Admin interface for managing ShortURL model.
    """
    list_display = ('short_code', 'original_url', 'is_active', 'created_at', 'expire_at')
    search_fields = ('short_code', 'original_url')
    list_filter = ('is_active', 'created_at')
    ordering = ('-created_at',)
