from django.contrib import admin
from .models import ShortURL, Click

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

@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Click model.
    """
    list_display = ('short_url', 'clicked_at')
    search_fields = ('short_url__short_code',)
    list_filter = ('clicked_at',)
    ordering = ('-clicked_at',)
