from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('students/details/<int:id>', views.details, name='details'),
    path('students/delete/<int:id>', views.delete, name='delete'),
    path('students/update/<int:id>', views.update, name='update'),
    path('students/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('add_information/', views.add_information, name='add_information'),



]

