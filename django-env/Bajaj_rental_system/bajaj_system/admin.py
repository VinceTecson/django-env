from django.contrib import admin
from .models import *


class function_customer(admin.ModelAdmin):
    list_display = ('ct_fname', 'ct_mname', 'ct_lname', 'ct_birthday', 'ct_address', 'ct_contact')

class function_rentalschedule(admin.ModelAdmin):
    list_display = ('rs_date', 'rs_type', 'rs_plan', 'rs_payment', 'rs_customer', 'rs_units')

class function_rentalplans(admin.ModelAdmin):
    list_display = ('plan_name', 'plan_description', 'plan_hours', 'plan_cost')

class function_cdt_conditions(admin.ModelAdmin):
    list_display = ('cdt_unit_condition',)

class function_units(admin.ModelAdmin):
    list_display = ('unit_color', 'unit_type', 'unit_info', 'unit_image', 'unit_cdt_condition')

class function_rentalrecord(admin.ModelAdmin):
    list_display = ('rr_customer', 'rr_units')

class function_contact(admin.ModelAdmin):
    list_display = ('name', 'username', 'message')

admin.site.register(Customer, function_customer)
admin.site.register(RentalSchedule, function_rentalschedule)
admin.site.register(Rental_Plans, function_rentalplans)
admin.site.register(Units_conditions, function_cdt_conditions)
admin.site.register(Units, function_units)
admin.site.register(RentalRecord, function_rentalrecord)
admin.site.register(Contact, function_contact)
