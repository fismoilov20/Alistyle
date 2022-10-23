"""Alistyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home', Home2View.as_view(), name='home2'),
    path('sections/<str:s>', SectionsView.as_view(), name='sections'),
    path('inners/<str:d>', InnersView.as_view(), name='inners'),
    path('products/<str:j>', ProductsView.as_view(), name="products"),
    path('product/<int:pk>', ProductDetailsView.as_view(), name="product"),
    path('wishlist', WishlistView.as_view(), name="wishlist"),
    path('shoppingcart', ShoppingCartView.as_view(), name="shoppingcart"),
    path('orders', OrdersView.as_view(), name="orders"),
]
