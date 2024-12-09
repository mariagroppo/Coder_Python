from django.urls import path
from core import views

# Para usar imagenes cargadas por el usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    
    # PRODUCTS ------------------------------------------
    path('products', views.products, name='products'),
    path('products/add', views.add_product, name='add_product'),
    

    # CART ------------------------------------------
    path('cart', views.cart, name='cart'),
    path('cart/add', views.add_cart, name='add_cart'),
    path('cart/add_product', views.add_product_to_cart, name='add_product_to_cart'),
    path('cart/ready', views.cart_ready, name='cart_ready'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para usar imagenes cargadas por el usuario