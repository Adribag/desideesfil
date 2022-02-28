from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path(f"{app_name}/", views.shop, name = "shop"),
    path('article/<int:product_id>', views.articleView, name="article")
]