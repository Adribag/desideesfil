from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path(f"", views.index, name = "index"),
    path(f"contact/", views.contact, name="contact"),
]