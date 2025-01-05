from django.urls import path
from core import views
from django.contrib.auth.views import LogoutView

# Para usar imagenes cargadas por el usuario
from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'  # Esto define el namespace

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutMe', views.aboutMe, name="aboutMe"), # aboutMe page
    path('profile', views.profile, name="profile"), # profile
    path('profile/update', views.profileUpdate, name="profileUpdate"), # profile Update
    path('profile/changePwd', views.ChangePwd.as_view(), name="changePwd"), # change password
    
    # AUTH ------------------------------------------
    path('register', views.register, name="register"), # Register page
    path('my-login', views.my_login, name="my-login"), # Login page
    path('user-logout', LogoutView.as_view(template_name='auth/logout.html'), name="user-logout"), # Logout page

    # PRODUCTS ------------------------------------------
    path('products/', views.products, name='products'),
    path('products/add', views.add_product, name='add_product'),  # ADMIN - Add new product
    path('products/update/<int:product_id>', views.update_product, name='update_product'), # ADMIN - Update product
    path('products/delete/<int:product_id>', views.delete_product, name='delete_product'), # ADMIN - Delete product
    
    # REQUESTS ------------------------------------------
    path('requests', views.requests, name='requests'), #  ADMIN - Read requests with status in progress
    path('requests_all', views.requests_all, name='requests_all'), # ADMIN - Read all requests
    path('requests/update/<int:pur_id>', views.update_purchase, name='update_purchase'), # ADMIN - Update requests status
    
    # CART ------------------------------------------
    path('cart', views.cart, name='cart'), # Read all carts by user
    path('cart/add', views.add_cart, name='add_cart'), # # Add new cart
    path('cart/add_product', views.add_product_to_cart, name='add_product_to_cart'), # Add product to cart
    path('cart/ready', views.cart_ready, name='cart_ready'), # Close cart, send request to bar

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para usar imagenes cargadas por el usuario