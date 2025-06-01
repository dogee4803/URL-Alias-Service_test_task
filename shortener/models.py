from django.db import models

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"
    
    def is_expired(self):
        return timezone.now() > self.expire_at
