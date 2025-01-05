from .models import Product, Purchase
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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


# - Update a product -------------------------------------------------------------------
class UpdateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'stock']



# - Update a purchase -------------------------------------------------------------------
class UpdatePurchaseForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        fields = ['status']

# Registro de usuario --------------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)

    class Meta: # configuraciones de mi formulario
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2']
        help_texts = {'username': '',
                      'email': ''}




# Edicion de perfil --------------------------
class ProfileUpdateForm(UserChangeForm):
    password = None
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    avatar = forms.ImageField(required=False)
    birthDate = forms.DateField(label='Fecha de nacimiento (YYYY-MM-DD)', required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'birthDate', 'avatar']
