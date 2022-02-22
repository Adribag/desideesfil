from django.conf import settings
from django.db import models

# Create your models here.

# class User_address(models.Model):

#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     delivery_address = models.CharField(max_length=255)
#     delivery_code = models.IntegerField()
#     delivery_city = models.CharField(max_length=255)

#     billing_address = models.CharField(max_length=255)
#     billing_code = models.IntegerField()
#     billing_city = models.CharField(max_length=255)



class AddressCategory(models.Model):

    name = models.CharField(max_length=255)
class Address(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    code = models.IntegerField()
    city = models.CharField(max_length=255)
    addressCategoryName = models.ForeignKey(AddressCategory, on_delete=models.CASCADE)

