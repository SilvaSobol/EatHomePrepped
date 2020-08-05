from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.create_user),
    path('login', views.user_login),
    path('log_out', views.log_out),
    path('user/', views.login, name = "login"),
    path('cart/', views.cart, name = "cart"),
    path('menu/', views.item_menu, name ="menu"),
]