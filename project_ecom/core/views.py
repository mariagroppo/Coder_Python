from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateProductForm, UpdateProductForm, UpdatePurchaseForm, ProfileUpdateForm
from .models import Product, Purchase, Items, UserInfo
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
#from django.contrib.auth.models import auth, authenticate

# ----------------------------------------------------------------------------------------------------
# LOGIN AND REGISTRATION
# ----------------------------------------------------------------------------------------------------

# Register a user ---------------------------------------------------------
def register(request):
    
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, "Account created successfully!")
            return redirect("core:my-login")
    context = {'form':form}
    return render(request, 'auth/register.html', context=context)

# Login a user -------------------------------------------------------------
def my_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.get_user()
            login(request, username)
            UserInfo.objects.get_or_create(user=username)
            return redirect('core:home')
            
    context = {'form':form}
    return render(request, 'auth/login.html', context=context)

# Perfil -------------------------------------------------------------
@login_required(login_url='core:my-login')
def profile(request):
    cart_opened = Purchase.objects.filter(user=request.user, status="Para cargar").exists()
    if cart_opened == True:
        cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
        prods_qty = cart.products.count()
    else:
        prods_qty=0
    context = {'prods_qty':prods_qty, 'cart_opened': cart_opened}
    return render(request, 'auth/profile.html', context=context)

# Editar perfil -------------------------------------------------------------
@login_required(login_url='core:my-login')
def profileUpdate(request):
    user_info = request.user.userinfo
    form = ProfileUpdateForm(initial={'avatar': user_info.avatar, 'birthDate': user_info.birthDate}, instance=request.user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            if form.cleaned_data.get('avatar'):
                user_info.avatar = form.cleaned_data.get('avatar')
                user_info.save()
            if form.cleaned_data.get('birthDate'):
                user_info.birthDate = form.cleaned_data.get('birthDate')
                print(form.cleaned_data.get('birthDate'))
                user_info.save()
            form.save()
            return redirect('core:profile')
    context = {'form':form}
    return render(request, 'auth/profileUpdateForm.html', context=context)

# Cambiar contrasena -------------------------------------------------------------
class ChangePwd(LoginRequiredMixin, PasswordChangeView):
    template_name = 'auth/profileChangePwd.html'
    success_url = reverse_lazy('core:profile')

# ----------------------------------------------------------------------------------------------------
# VARIOS
# ----------------------------------------------------------------------------------------------------

def index(request):
    return render (request, 'core/index.html')

@login_required(login_url='core:my-login')
def aboutMe(request):
    return render (request, 'aboutMe.html')


# PRODUCTS --------------------------------------------------------------------------
@login_required(login_url='core:my-login')
def products(request):
    try:
        query = request.GET.get('query')  # Tomamos el parámetro de la URL
        if query:
            #all_products = Product.objects.filter(title__icontains=query)  # Filtrar por nombre
            all_products = Product.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        else:
            all_products = Product.objects.all()  # Mostrar todos los productos si no hay búsqueda
        cart_opened = Purchase.objects.filter(user=request.user, status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0
        context = {'products': all_products, 'prods_qty':prods_qty, 'cart_opened': cart_opened}
        return render(request, 'core/products.html', context=context)
        #return render(request, 'core/products.html')
    except:
        return render(request, 'core/index.html')

@login_required(login_url='core:my-login')
def add_product(request):
    try:
        cart_opened = Purchase.objects.filter(user=request.user, status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0
        
        if request.method == "POST": # POST request
            form = CreateProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect("core:products") # In case the url is written manually
        else: # GET request
            form = CreateProductForm()
            context = {'form': form, 'prods_qty':prods_qty, 'cart_opened': cart_opened}
            return render(request, 'core/add_product.html', context=context) # When clicking the ADD A NEW CLIENT button
    except:
        """ messages.error(request, "Error while trying to create a new customer. Please, contact admin.") """
        return redirect("core:products")


@login_required(login_url='core:my-login')
def update_product (request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if request.method == 'POST':
            form = UpdateProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
            return redirect("core:products")
        form = UpdateProductForm(instance=product)
        context = {'form': form, 'product': product}
        return render(request, 'core/update_product.html', context=context)
        
    except:
        return redirect("core:products")
    
@login_required(login_url='core:my-login')
def delete_product (request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return redirect("core:products")
        
    except:
        return redirect("core:products")


# REQUESTS --------------------------------------------------------------------------
@login_required(login_url='core:my-login')
def requests(request):
    try:
        if request.user.username == 'admin':
            purchases = Purchase.objects.filter(
                ~Q(status__in=['Para cargar', 'Finalizado', 'Cancelado'])
            )
            context = {'purchases': purchases}
            return render(request, 'core/requests.html', context=context)
        return redirect("core:products")
    except:
        return redirect("core:products")

@login_required(login_url='core:my-login')
def requests_all(request):
    try:
        if request.user.username == 'admin':
            purchases = Purchase.objects.exclude(status='Para cargar')
            context = {'purchases': purchases}
            return render(request, 'core/requests.html', context=context)
        return redirect("core:products")
    except:
        return redirect("core:products")

@login_required(login_url='core:my-login')
def update_purchase (request, pur_id):
    try:
        if request.user.username == 'admin':
            purchase = Purchase.objects.get(id=pur_id)
            if request.method == 'POST':
                form = UpdatePurchaseForm(request.POST, instance=purchase)
                if form.is_valid():
                    form.save()
                return redirect("core:requests")
            form = UpdatePurchaseForm(instance=purchase)
            context = {'form': form, 'product': purchase}
            return render(request, 'core/update_purchase.html', context=context)
        return redirect("core:requests")
    except:
        return redirect("core:requests")

# CART --------------------------------------------------------------------------
@login_required(login_url='core:my-login')
def cart(request):
    try:
        cart_opened = Purchase.objects.filter(user=request.user, status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0
        all_carts = Purchase.objects.filter(user=request.user)
        context = {'carts': all_carts, 'prods_qty':prods_qty, 'cart_opened': cart_opened}
        return render(request, 'core/cart.html', context=context)
        #return render(request, 'core/products.html')
    except:
        return render(request, 'core/index.html')


@login_required(login_url='core:my-login')
def add_cart(request):
    try:
        # chequear que el ultimo po creado sea distinto de vacio
        all_carts = Purchase.objects.filter(user=request.user, status="Para cargar").exists()
        if all_carts == False:
            new_cart = Purchase()
            new_cart.user = request.user
            new_cart.save()
            
        return redirect("core:cart") # In case the url is written manually     
    except:
        #print("Error")
        return redirect("core:cart")

@login_required(login_url='core:my-login')
def add_product_to_cart(request):
    try:
        if request.method == 'POST':
            product_id = int(request.POST.get('product_id'))
            prod = get_object_or_404(Product, id=product_id)
            quantity = int(request.POST.get('qty_selected'))
            if quantity <= 0:
                print("La cantidad debe ser mayor a 0")
                return redirect("core:products")

            new_item = Items()
            new_item.quantity = quantity
            new_item.subtotal = prod.price * quantity
            new_item.product = prod
            new_item.save()

            cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
            if not cart:  # Si no hay un carrito, crearlo
                cart = Purchase()
                cart.save()
            cart.products.add(new_item)
            cart.total += new_item.subtotal
            cart.user = request.user
            cart.save()
            
            return redirect("core:products") # In case the url is written manually
    except:
        print("Error")
        return redirect("core:products")

@login_required(login_url='core:my-login')
def cart_ready(request):
    try:
        cart = Purchase.objects.filter(user=request.user, status="Para cargar").first()
        if cart.products.count() > 0:
            cart.status = 'Pendiente de aprobacion'
            cart.save()
        return redirect("core:cart")
    except:
        print("Error")
        return redirect("core:cart")