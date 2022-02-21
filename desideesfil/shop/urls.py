from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path(f"{app_name}/", views.shop, name = "shop"),
]