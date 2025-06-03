import random
import string
from datetime import timedelta
from django.db import models
from django.utils import timezone


def default_expire_at():
    # todo: Посмотреть, возможно ли использовать lambda-функцию для установки значения по умолчанию
    return timezone.now() + timedelta(days=1)


# Create your models here.
class ShortURL(models.Model):
    """
    Model representing a shortened URL.
    
    """
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField(default=default_expire_at)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

    @staticmethod
    def generate_unique_short_code(length = 8):
        characters = string.ascii_letters + string.digits
        while True:
            short_code = ''.join(random.choice(characters, k=length))
            if not ShortURL.objects.filter(short_code=short_code).exists():
                return short_code

    def is_expired(self):
        return timezone.now() > self.expire_at
