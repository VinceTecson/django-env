from django.urls import path
from . import views

urlpatterns = [
    path('book_record/', views.records, name='records'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('book_record/delete/<int:id>', views.delete, name='delete'),
    path('book_record/update/<int:id>', views.update, name='update'),
    ]