from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.landing_page, name='landing_page' ),
    path('homepage/', views.unit_list, name='unit_list'),
    path('new_unit_list/<int:id>/', new_unit_list, name='new_unit_list'),
    path('signup/', views.signup_user, name='signup_user'),
    path('ctmlist/', views.customer_list, name='customer_list'),
    path('checking/', views.scheduling, name='scheduling'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_user, name='logout_user'),
    path('pricing/', views.pricing, name='pricing'),
    path('schedule/<int:unit_id>/', views.schedule_by_unit_id, name='schedule_by_unit_id'),
    path('bajaj_display/', views.bajaj_display, name='bajaj_display'),
    # display contact.
    path('contact/', views.contact, name='contact'),
    # function for conatct submit.
    path('contact_submit/', views.contact_submit, name='contact_submit'),
    path('profile/', views.profile_display, name='profile_display'),
    path('nav/', views.nav_display, name='nav_display'),
    path('update_schedule/', views.update_schedule, name='update_schedule'),
    path('delete_schedule/', views.delete_schedule, name='delete_schedule'),
    path('rules_view/', views.rules_view, name='rules_view'),


    # --------------------------------admin path ----------------------------------------

    path('myadmin/', views.admin_dashboard, name='admin_dashboard'),
    # add units.
    path('add_units/', views.add_units, name='add_units'),
    # update units.
    path('update_unit/', views.update_unit, name='update_unit'),
    # submit schedule.
    path('my_schedule_selected/', my_schedule_selected, name='my_schedule_selected'),
    # add price for bajaj.
    path('add_price/', views.add_price, name='add_price'),
    # update function.
    path('update_plan/<int:id>/', views.update_plan, name='update_plan'),

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)