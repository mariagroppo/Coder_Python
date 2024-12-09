from .models import Product
from django import forms

# - Create a product -------------------------------------------------------------------
class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['picture', 'title', 'description', 'price', 'stock']
        """ labels = {
            'picture': 'imagen',
            'title': 'Titulo',
            'description': 'Descripcion',
            'price': 'Precio ($)',
            'stock': 'stock',
        } """