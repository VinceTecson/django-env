from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import BRecords

# call data from database
def records(request):
    records = BRecords.objects.all().values()
    template = loader.get_template('home_page.html')
    context = {
        'home_page': records,
    }
    return HttpResponse(template.render(context, request))

# add customer

def add_customer(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        lastcredits = request.POST.get('lastcredits')
        lastpayment = request.POST.get('lastpayment')
        totalbalance = request.POST.get('totalbalance')

        records = BRecords(firstname=firstname, lastname=lastname, lastcredits=lastcredits, lastpayment=lastpayment, totalbalance=totalbalance)
        records.save()
        return HttpResponseRedirect(reverse('records'))
    else:
        return render(request, 'add_customer.html')

# delete functions 
def delete(request, id):
    records = BRecords.objects.get(id=id)
    records.delete()
    return HttpResponseRedirect(reverse('records'))

#update students details
def update(request, id):
  records = BRecords.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'home_page': records,
  }
  return HttpResponse(template.render(context, request))

#update record send to data base the new input details of students
def updaterecord(request, id):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  lastcredits = request.POST['lastcredits']
  lastpayment = request.POST['lastpayment']
  totalbalance = request.POST['totalbalance']
  records = BRecords.objects.get(id=id)
  records.firstname = firstname
  records.lastname = lastname
  records.lastcredits = lastcredits
  records.lastpayment = lastpayment
  records.totalbalance = totalbalance
  records.save()
  return HttpResponseRedirect(reverse('records'))
