from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateProductForm
from .models import Product, Purchase, Items

# Create your views here.

def index(request):
    # return HttpResponse ("welcome")
    cart_opened = Purchase.objects.filter(status="Para cargar").exists()
    if cart_opened == True:
        cart = Purchase.objects.filter(status="Para cargar").first()
        prods_qty = cart.products.count()
    else:
        prods_qty=0
    context = {'prods_qty': prods_qty}
    return render (request, 'core/index.html', context=context)

# PRODUCTS --------------------------------------------------------------------------
def products(request):
    try:
        all_products = Product.objects.all()
        cart_opened = Purchase.objects.filter(status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0
        context = {'products': all_products, 'prods_qty': prods_qty, 'cart_opened': cart_opened}
        return render(request, 'core/products.html', context=context)
        #return render(request, 'core/products.html')
    except:
        return render(request, 'core/index.html')

def add_product(request):
    try:
        cart_opened = Purchase.objects.filter(status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0

        if request.method == "POST": # POST request
            form = CreateProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return redirect("products") # In case the url is written manually
        else: # GET request
            form = CreateProductForm()
            context = {'form': form, 'prods_qty': prods_qty}
            return render(request, 'core/add_product.html', context=context) # When clicking the ADD A NEW CLIENT button
    except:
        """ messages.error(request, "Error while trying to create a new customer. Please, contact admin.") """
        return redirect("products")


# CART --------------------------------------------------------------------------
def cart(request):
    try:
        cart_opened = Purchase.objects.filter(status="Para cargar").exists()
        if cart_opened == True:
            cart = Purchase.objects.filter(status="Para cargar").first()
            prods_qty = cart.products.count()
        else:
            prods_qty=0
        all_carts = Purchase.objects.all()
        context = {'carts': all_carts, 'prods_qty': prods_qty, 'cart_opened': cart_opened}
        return render(request, 'core/cart.html', context=context)
        #return render(request, 'core/products.html')
    except:
        return render(request, 'core/index.html')


def add_cart(request):
    try:
        # chequear que el ultimo po creado sea distinto de vacio
        all_carts = Purchase.objects.filter(status="Para cargar").exists()
        if all_carts == True:
            print("Pedido ya abierto.")
        else:
            new_cart = Purchase()
            new_cart.save()
            
        return redirect("cart") # In case the url is written manually     
    except:
        print("Error")
        return redirect("cart")
    
def add_product_to_cart(request):
    try:
        if request.method == 'POST':
            product_id = int(request.POST.get('product_id'))
            # prod = Product.objects.filter(id=product_id)
            prod = get_object_or_404(Product, id=product_id)
            quantity = int(request.POST.get('qty_selected'))
            if quantity <= 0:
                print("La cantidad debe ser mayor a 0")
                return redirect("products")

            new_item = Items()
            new_item.quantity = quantity
            new_item.subtotal = prod.price * quantity
            new_item.product = prod
            new_item.save()

            cart = Purchase.objects.filter(status="Para cargar").first()
            if not cart:  # Si no hay un carrito, crearlo
                cart = Purchase()
                cart.save()
            cart.products.add(new_item)
            cart.total += new_item.subtotal
            cart.save()
            
            return redirect("products") # In case the url is written manually
    except:
        print("Error")
        return redirect("products")


def cart_ready(request):
    try:
        cart = Purchase.objects.filter(status="Para cargar").first()
        cart.status = 'Pendiente de aprobacion'
        cart.save()
        return redirect("cart")
    except:
        print("Error")
        return redirect("cart")