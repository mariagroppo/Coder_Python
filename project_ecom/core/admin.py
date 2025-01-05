from django.contrib import admin
from .models import Product,Items,Purchase, UserInfo

# Register your models here.

admin.site.register(Product)
admin.site.register(Items)
admin.site.register(Purchase)
admin.site.register(UserInfo)