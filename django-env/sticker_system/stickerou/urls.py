from django.urls import path
from .views import *

urlpatterns = [
     path('login/', login_page, name='login_page'),
    path('logout/', logout_user, name='logout_user'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('shop/', shop, name='shop'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('buy/<int:item_id>/', buy_item, name='buy_item'),

]