from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
import os
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages


def rules_view(request):
    return render(request, 'association_rules.html')


# ---------------------------------- display profile function -------------------------------------

# function display the information of user to profile page.
def profile_display(request):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login_page')
        
        user = Customer.objects.get(id=user_id)
        records_Rental = RentalRecord.objects.filter(rr_customer=user)
        schedules = RentalSchedule.objects.filter(rs_customer_id=user_id).select_related('rs_units')
        my_plans = Rental_Plans.objects.all() #rental plans display

        return render(request, 'profile.html', {'user': user, 'records_Rental':records_Rental, 'schedules':schedules, 'my_plans':my_plans})


# function to display the profile page.
def user_profile(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = Customer.objects.get(id=user_id)
        return {'user': user}
    return {}

# function for update the schedule created.
def update_schedule(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule_id')
        rs_date = request.POST.get('rs_date')
        rs_timeStart = request.POST.get('rs_timeStart')
        rs_plan_id = request.POST.get('rs_plan')

        try:
            schedule = RentalSchedule.objects.get(pk=schedule_id)
        except RentalSchedule.DoesNotExist:
            error_message = "Schedule does not exist."
            return render(request, 'profile.html', {'error_message': error_message})

        try:
            rs_plan = Rental_Plans.objects.get(pk=rs_plan_id)
        except Rental_Plans.DoesNotExist:
            error_message = "Rental plan does not exist."
            return render(request, 'profile.html', {'error_message': error_message})

        schedule.rs_date = rs_date
        schedule.rs_timeStart = rs_timeStart
        schedule.rs_plan = rs_plan
        schedule.save()

        return redirect('profile_display') 
    else: 
        return redirect('profile_display')
    

# delete function for user profile schedule created.
def delete_schedule(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule_id')

        try:
            schedule = RentalSchedule.objects.get(pk=schedule_id)
        except RentalSchedule.DoesNotExist:
            error_message = "Schedule does not exist."
            return render(request, 'admin.html', {'error_message': error_message})

        schedule.delete()

        return redirect('profile_display') 
    else: 
        return redirect('profile_display')





# ---------------------------------- navigation display fname and lname user ------------------------------------

def nav_display(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_page')
    
    user = Customer.objects.get(id=user_id)
    return render(request, 'nav.html', {'user': user})


# display information of the user in navigation bar.

def nav_function(request):
    try:
        latest_prof = Customer.objects.latest('id')
    except Customer.DoesNotExist:
        latest_prof = None
    return redirect('nav_display')

# -------------------------------- login form ---------------------------------
    
# login functon.
def login_page(request):
    if 'user_id' in request.session:
        return redirect('unit_list')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Customer.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            request.session['myadmin'] = user.myadmin

            if user.myadmin:
                return redirect('admin_dashboard')
            return redirect('unit_list')
        except Customer.DoesNotExist:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'login.html')

# log out function 

def logout_user(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('landing_page')
    
# ------------------------------------- display list of customer -------------------------------------------


# list of customer | display all the customer.
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'homepage.html', {'customers': customers})


# -------------------------------------- display list of units in "HOMEPAGE" ----------------------------------------------

# function no.1
# list of bajaj auto | display all the bajaj.
def unit_list(request):
    bajaj = Units.objects.all()

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_page')
    
    user = Customer.objects.get(id=user_id)
    
    return render(request, 'homepage.html', {'bajaj': bajaj, 'user': user})

    

# function no.2
# function from selecting units | geting the id of units.
def new_unit_list(request, id):
    unit_id = id
    unit = Units.objects.get(id=unit_id) #units display
    my_plans = Rental_Plans.objects.all() #rental plans display
    return render(request, 'checking.html', {'unit': unit, 'my_plans':my_plans})


# ---------------------------------------- display landing page ---------------------------------------------

def landing_page(request):
    bajaj = Units.objects.all()
    return render(request, 'landingpage.html', {'bajaj':bajaj})

# ---------------------------------------- display pricing page ---------------------------------------------

def pricing(request):
    rental_plans = Rental_Plans.objects.all()
    return render(request, 'pricing.html', {'rental_plans': rental_plans})


# ---------------------------------------- user fill-up form | username & password --------------------------


def signup_user(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        ct_fname  = request.POST.get('ct_fname')
        ct_mname  = request.POST.get('ct_mname')
        ct_lname  = request.POST.get('ct_lname')
        ct_birthday   = request.POST.get('ct_birthday')
        ct_address   = request.POST.get('ct_address')
        ct_contact   = request.POST.get('ct_contact')

        user = Customer.objects.create(
            username=username,
            password=password,
            ct_fname=ct_fname,
            ct_mname=ct_mname, 
            ct_lname=ct_lname,
            ct_birthday=ct_birthday,
            ct_address=ct_address,
            ct_contact=ct_contact
        )

        return HttpResponseRedirect(reverse('landing_page'))
    else:
        return render(request, 'signup.html')


# ------------------------------------------ scheduling function -----------------------------------------

# set schedule function.

def scheduling(request):
    error_message = None

    if request.method == 'POST': 
        rs_date = request.POST.get('rs_date')
        unit_id = request.POST.get('unit_id')
        rs_timeStart = request.POST.get('rs_timeStart')
        rs_plan_id = request.POST.get('rs_plan')

        if not rs_date:
            error_message = 'Please provide a valid date.'
            return HttpResponseRedirect(reverse('unit_list') + f'?error_message={error_message}')

        else:
            unit = Units.objects.get(id=unit_id)
            
            existing_schedule = RentalSchedule.objects.filter(rs_date=rs_date).exists()

            if existing_schedule:
                error_message = 'This schedule already exists.'
            else:
                user_id = request.session.get('user_id')
                if user_id:
                    try:
                        user = Customer.objects.get(id=user_id)
                    except Customer.DoesNotExist:
                        error_message = 'User not found.'
                        return HttpResponseRedirect(reverse('unit_list') + f'?error_message={error_message}')
                    
                    if RentalSchedule.objects.filter(rs_customer=user).exists():
                        error_message = 'A customer can create only one schedule per unit..'
                        return HttpResponseRedirect(reverse('unit_list') + f'?error_message={error_message}')
                    
                    try:
                        rs_plan = Rental_Plans.objects.get(id=rs_plan_id)
                    except Rental_Plans.DoesNotExist:
                        error_message = 'Rental plan not found.'
                        return HttpResponseRedirect(reverse('unit_list') + f'?error_message={error_message}')
                    
                    schedule_storage = RentalSchedule.objects.create(
                        rs_date=rs_date,
                        rs_units=unit,
                        rs_timeStart=rs_timeStart,
                        rs_plan=rs_plan,
                        rs_customer=user
                    )
                    error_message = 'Thank you for Creating a schedule. Good luck!'
                    return HttpResponseRedirect(reverse('unit_list') + f'?error_message={error_message}')
                else:
                    error_message = 'User not logged in, Please login.'

    if error_message:
        return HttpResponseRedirect(reverse('landing_page') + f'?error_message={error_message}')
    
# ----------------------------- display all schedule's from schedule record ----------------------------------

# display all schedule in checking.
def schedule_by_unit_id(request, id):
    schedules = RentalSchedule.objects.filter(unit_id=id)
    bajaj = Units.objects.all()
    return render(request, 'checking.html', {'schedules': schedules, 'bajaj': bajaj})
    

# ---------------------------------------------------------------------------------------------
# display units in list of bajaj page.
def bajaj_display(request):
    bajaj = Units.objects.all()
    return render(request, 'bajaj_display.html', {'bajaj': bajaj})

# ---------------------------------------------------------------------------------------------
# displat contact.
def contact(request):
    return render(request, 'contact.html')


# ---------------------------------------------------------------------------------------------
# submit function for contact.
def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        message = request.POST.get('message')
        
        contact = Contact.objects.create(
            name=name,
            username=username,
            message=message,    
        )
        return redirect('unit_list')
    else:
        return render(request, 'contact.html')
    
    
    

    
# ------------------------------------------ "ADMIN"  --------------------------------------------------------

# ---------------------------- display all units in "ADMIN PAGE" ---------------------------------------------


# display all units in admin page.
def admin_dashboard(request):
    units = Units.objects.all() #for units
    schedules = RentalSchedule.objects.all() #for schedules
    customers = Customer.objects.all() #for customer
    rental_records = RentalRecord.objects.all() #for rental record
    rental_plans = Rental_Plans.objects.all() #for plans
    unit_conditions = Units_conditions.objects.all()

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login_page')
    
    user = Customer.objects.get(id=user_id)
    return render(request, 'admin.html', {'units': units, 'schedules': schedules, 'customers': customers, 'rental_records': rental_records, 'rental_plans':rental_plans, 'unit_conditions':unit_conditions})


# add units.

def add_units(request):
    if request.method == 'POST':
        unit_color = request.POST.get('unit_color')
        unit_type = request.POST.get('unit_type')
        unit_info = request.POST.get('unit_info')
        unit_condition_id = request.POST.get('unit_condition')
        unit_image = request.FILES.get('unit_image')

        existing_unit = Units.objects.filter(unit_color=unit_color).first()
        
        if existing_unit:
            return render(request, 'admin.html', {
                'error_message': 'Unit color already exists', 
                'units': Units.objects.all(),
                'unit_conditions': Units_conditions.objects.all()
            })
        else:
            unit_condition = Units_conditions.objects.get(id=unit_condition_id)
            new_unit = Units(
                unit_color=unit_color,
                unit_type=unit_type,
                unit_info=unit_info,
                unit_cdt_condition=unit_condition,
                unit_image=unit_image
            )
            new_unit.save()
            return redirect('admin_dashboard')
    else: 
        return HttpResponseRedirect(reverse('admin_dashboard'))

# update units.

def update_unit(request):
    if request.method == 'POST':
        unit_id = request.POST.get('unit_id')
        unit_color = request.POST.get('unit_color')
        unit_type = request.POST.get('unit_type')
        unit_info = request.POST.get('unit_info')

        try:
            unit = Units.objects.get(pk=unit_id)
        except Units.DoesNotExist:
            error_message = "Unit does not exist."
            return render(request, 'admin.html', {'error_message': error_message})

        unit.unit_color = unit_color
        unit.unit_type = unit_type
        unit.unit_info = unit_info
        unit.save()

        return redirect('admin_dashboard') 
    else: 
        return redirect('admin_dashboard')  

# function that save all the data in rental record from rental schedule.


def my_schedule_selected(request):
    if request.method == 'POST':
        schedule_id = request.POST.get('schedule_id')
        
        try:
            schedule = RentalSchedule.objects.get(pk=schedule_id)
            
            customer = schedule.rs_customer
            units = schedule.rs_units
            
            click_count = request.session.get('schedule_click_count', 0)
            
            if click_count >= 2:
                schedule.delete()
                request.session['schedule_click_count'] = 0
                return redirect('admin_dashboard')
            
            request.session['schedule_click_count'] = click_count + 1
            
            rental_record = RentalRecord.objects.create(
                rr_customer=customer,
                rr_units=units,
                present_time=timezone.now()
            )
            
            rental_record.rs_date = schedule.rs_date
            rental_record.rs_timeStart = schedule.rs_timeStart
            rental_record.rr_plan = schedule.rs_plan
            
            rental_record.save()
            
            return redirect('admin_dashboard') 
        except RentalSchedule.DoesNotExist:
            return redirect('admin_dashboard')  
    else:
        return redirect('admin_dashboard')

    
# add price to bajaj
def add_price(request):
    if request.method == 'POST':
        plan_name = request.POST.get('plan_name')
        plan_description = request.POST.get('plan_description')
        plan_hours = request.POST.get('plan_hours')
        plan_cost = request.POST.get('plan_cost')

        new_plan = Rental_Plans.objects.create(
            plan_name=plan_name,
            plan_description=plan_description,
            plan_hours=plan_hours,
            plan_cost=plan_cost,
        )
        new_plan.save()

        return redirect('admin_dashboard') 
    else: 
        return redirect('admin_dashboard')  



# function for update the pricing
def update_plan(request, id):
    if request.method == 'POST':
        plan_name = request.POST.get('plan_name')
        plan_description = request.POST.get('plan_description')
        plan_hours = request.POST.get('plan_hours')
        plan_cost = request.POST.get('plan_cost')

        plan = Rental_Plans.objects.get(pk=id)


        plan.plan_name = plan_name
        plan.plan_description = plan_description
        plan.plan_hours = plan_hours
        plan.plan_cost = plan_cost
        plan.save()

        return redirect('admin_dashboard') 
    else: 
        return redirect('admin_dashboard')
    


    