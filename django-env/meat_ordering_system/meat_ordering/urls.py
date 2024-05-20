from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html')),
    path('', views.product_list, name='index'),
    path('accounts/', include('allauth.urls')),
    path('home', views.product_list, name ='products'),
    path('adminproduct/', views.admin_products, name ='adminproducts'),
    path('adminproduct/addproduct/', views.adminAddProduct, name = 'adminAddProduct'),
    path('adminproduct/delete/<int:id>/', views.delete_product, name='delete_product'),
    
    path('update/<int:id>/', views.updateForm, name='update_product'),
    path('update/updateproduct/<int:id>/', views.update_product, name='update_product'),

    path('category/<int:category_id>/', views.prodCateg, name='prodCateg'),

    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('checkout/', views.checkout, name='checkout'),
]