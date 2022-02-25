from django.urls import path
from . import views

urlpatterns = [
    # path(r'profile/(?P<id>[a-zA-Z0-9]+)$', views.profile, name = 'profile'),
    path(f'profile/', views.profile, name='profile'),
    path(f'profile/deliveryAddress/', views.addressUpdateDelivery, name='deliveryAddress'),
    path(f'profile/billingAddress/', views.addressUpdateBilling, name='billingAddress'),
    path(f'profile/user/', views.userUpdate, name='user'),
    path(f'profile/delete/', views.userDelete, name='delete'),
]