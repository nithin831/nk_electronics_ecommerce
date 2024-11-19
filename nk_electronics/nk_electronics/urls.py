"""
URL configuration for nk_electronics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", v.home, name = "home"),
    path("base/", v.base, name = "base"),
    path("products/", v.product, name = "products"),
    path("search/", v.search, name = "search"),
    path("products/<str:id>", v.product_details, name = "product_details"),
    path("contact/", v.contact, name = "contact"),
    path("register/", v.handel_register, name = "register"),
    path("login/", v.handel_login, name = "login"),
    path("logout/", v.handel_logout, name = "logout"),
    
    # cart
    path('cart/add/<int:id>/', v.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', v.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', v.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', v.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', v.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',v.cart_detail,name='cart_detail'),
    
    path('cart/checkout/',v.checkout,name='checkout'),
    path('cart/checkout/placeorder',v.placeorder,name='placeorder'),
    
    path("success/", v.success, name = "success"),
    
    path("your_order/", v.your_order, name = "your_order"),
    
    
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
