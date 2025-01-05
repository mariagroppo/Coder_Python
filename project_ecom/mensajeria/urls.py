from django.urls import path
from mensajeria import views

# Para usar imagenes cargadas por el usuario
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mensajeria'  # Esto define el namespace

urlpatterns = [
    path('chat', views.chat, name='chat'),
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Para usar imagenes cargadas por el usuario