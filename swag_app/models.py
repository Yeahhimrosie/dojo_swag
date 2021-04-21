from django.db import models
from django.contrib.auth.models import user

# Create your models here.
# Abbey will handle models

class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(default=0.00)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)