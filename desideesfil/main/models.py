from django.conf import settings
from django.db import models

# Create your models here.
class Contact(models.Model):

    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    mail = models.EmailField(max_length=255)
    message = models.TextField(max_length=1000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=19)