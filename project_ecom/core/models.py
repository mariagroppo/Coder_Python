from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    # picture = models.CharField(max_length=100, default="{% static 'images/no-image.png' %}")
    picture = models.ImageField(upload_to='products', null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

class Items(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    subtotal = models.FloatField(default=0)

    def __str__(self):
        return "ID " + str(self.product.id) + " x " + str(self.quantity) 

class Purchase(models.Model):

    STATUS_CHOICES = [
        ('Para cargar', 'Para cargar'),
        ('Pendiente de aprobacion', 'Pendiente de aprobacion'),
        ('Pagado', 'Pagado'),
        ('En preparacion', 'En preparacion'),
        ('Listo para retirar', 'Listo para retirar'),
        ('Finalizado', 'Finalizado'),
        ('Cancelado', 'Cancelado')
    ]
    
    creation_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('Items', blank=True)
    total = models.FloatField(default=0)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Para cargar')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=1)

    def __str__(self):
        return str(self.creation_date) + " x " + str(self.total) 


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    birthDate = models.DateField(null=True)

