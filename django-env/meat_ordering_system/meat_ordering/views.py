from django.shortcuts import render, redirect ,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from datetime import datetime
from .models import *
from .forms import *

def product_list(request):
    products = Products.objects.all()
    template = loader.get_template('blog/index.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def admin_products(request):
    products = Products.objects.all()
    template = loader.get_template('admin/products.html')
    context = {
        'products' : products,
    }
    return HttpResponse(template.render(context, request))

def adminAddProduct(request):
    if request.method == 'POST':
        form = AdminAddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(admin_products)
    else:
        form = AdminAddProduct()
        context = {
            'form': form
        }
    return render(request, 'admin/addproduct.html', context)

def updateForm(request, id):
    product = Products.objects.get(pk=id)
    return render(request, 'admin/updateproduct.html', {'product': product})

'''def updateForm(request, id):
    product = get_object_or_404(Products, pk=id)
    # Render a template with a form to update the product
    return render(request, 'admin/updateproduct.html', {'product': product})'''

def update_product(request, id):
    product = Products.objects.get(pk=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.prodName = request.POST.get('prodName')
        product.price = request.POST.get('price')
        product.category = request.POST.get('category')
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect(admin_products)
    return render(request, 'admin/updateproduct.html', {'product': product, 'categories': categories})

#------------------------------------------------------#
def delete_product(request, id):
    product = Products.objects.get(pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('adminproducts')
    context = {'product': product}
    return render(request, 'admin/delete.html', context)
#----------------------------------------------------------#
def prodCateg(request, category_id):
    if category_id == 0:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category=category_id)
    return render(request, 'blog/index.html', {'products': products})

def view_cart(request):
    cart_items = Carts.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = Carts.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('/home')
 
def remove_from_cart(request, item_id):
    cart_item = Carts.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')

def checkout(request):
    cart_items = Carts.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.subtotal = item.product.price * item.quantity
    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})



'''def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('account/login.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        username = request.POST['username']
        username = request.POST['username']
        username = request.POST['username']
        username = request.POST['username']
        username = request.POST['username']



    template = loader.get_template('signup.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

#def login(request):
    #return render(request, "authentication/login.html")

#def logout(request):
    #return render(request, "authentication/signup.html")'''

