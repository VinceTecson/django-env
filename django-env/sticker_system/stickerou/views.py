from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def login_page(request):
    if 'user_id' in request.session:
        if request.session.get('is_admin'):
            return redirect('admin_dashboard')
        return redirect('dashboard')

    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        try:
            user = Useracc.objects.get(user_name=user_name, user_password=user_password)
            request.session['user_id'] = user.id
            request.session['is_admin'] = user.is_admin  # Save admin status in session
            messages.success(request, 'Login successful.')
            
            if user.is_admin:
                return redirect('admin_dashboard')
            return redirect('dashboard')
        except Useracc.DoesNotExist:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

def logout_user(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, 'Logout successful.')
    return redirect('login_page')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('login')

    user_id = request.session['user_id']
    user = Useracc.objects.get(id=user_id)

    return render(request, 'dashboard.html', {'user': user})

def admin_dashboard(request):
    if 'user_id' not in request.session or not request.session.get('is_admin'):
        return redirect('login')

    user_id = request.session['user_id']
    user = Useracc.objects.get(id=user_id)

    return render(request, 'admin_dashboard.html', {'user': user})


def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_page')
    
    user = Useracc.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})

def shop(request):
    items = Item.objects.all()
    return render(request, 'shop.html', {'items': items})

def buy_item(request, item_id):
    if 'user_id' not in request.session:
        return redirect('login_page')

    item = Item.objects.get(id=item_id)
    user = Useracc.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        Purchase.objects.create(user=user, item=item, quantity=quantity)
        messages.success(request, 'Purchase successful!')
        return redirect('profile')

    return render(request, 'buy_item.html', {'item': item})