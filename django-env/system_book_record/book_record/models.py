from django.db import models

class BRecords(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dateofcredits = models.DateTimeField(auto_now_add=True)
    lastcredits = models.IntegerField()
    lastpayment = models.IntegerField()
    dateofpayment = models.DateTimeField(auto_now_add=True)
    totalbalance = models.IntegerField()