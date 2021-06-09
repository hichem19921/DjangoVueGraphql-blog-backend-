from django.db import models
from django.conf import settings
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,)
    website = models.URLFIELD(blank=True)
    
