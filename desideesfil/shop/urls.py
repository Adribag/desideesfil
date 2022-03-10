from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path(f"{app_name}/", views.shop, name = "shop"),
    path('article/<int:product_id>', views.articleView, name="article"),
    path('cart/', views.cart, name="cart"),
    path('deleteArticle/<int:id>/', views.deleteArticle, name="deleteArticle"),
]