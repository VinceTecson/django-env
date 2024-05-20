from django.db import models


    
class Units_conditions(models.Model):
    cdt_unit_condition = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.cdt_unit_condition}"
    

class Units(models.Model):
    unit_color = models.CharField(max_length=100)
    unit_type = models.CharField(max_length=100, null=True)
    unit_info = models.CharField(max_length=300)
    unit_image = models.ImageField(upload_to='picture/')
    unit_cdt_condition = models.ForeignKey(Units_conditions, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.unit_color} {self.unit_type}"
    
class Customer(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    ct_profile = models.ImageField(upload_to='picture/')
    ct_fname = models.CharField(max_length=100)
    ct_mname = models.CharField(max_length=100)
    ct_lname = models.CharField(max_length=100)
    ct_birthday = models.DateField(max_length=100, null=True)
    ct_address = models.CharField(max_length=100, null=True)
    ct_contact = models.IntegerField(null=True)
    ct_units = models.ForeignKey(Units, null=True, on_delete=models.CASCADE)
    myadmin = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.ct_fname} {self.ct_lname}"

class Rental_Plans(models.Model):
    plan_name = models.CharField(max_length=100)
    plan_description = models.CharField(max_length=200)
    plan_hours = models.IntegerField(null=True)
    plan_cost = models.IntegerField(null=True)

class RentalSchedule(models.Model):
    rs_timeStart = models.TimeField(max_length=100, null=True)
    rs_date = models.DateField(max_length=100, null=True)
    rs_type = models.CharField(max_length=100)
    rs_payment = models.IntegerField(null=True)
    rs_plan = models.ForeignKey(Rental_Plans, null=True, on_delete=models.CASCADE)
    rs_customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    rs_units = models.ForeignKey(Units, null=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.rs_timeStart} {self.rs_timeEnd}"

class RentalRecord(models.Model):
    rr_customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    rr_units = models.ForeignKey(Units, null=True, on_delete=models.CASCADE)
    rr_plan = models.ForeignKey(Rental_Plans, null=True, on_delete=models.CASCADE)  # Ensure this field is added
    present_time = models.DateTimeField(auto_now=True)

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, null=True)
    message = models.CharField(max_length=100, null=True)