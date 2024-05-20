from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .models import Student, Course, YearLevel, Subject, Schedule


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})


#students details function
def details(request, id):
    students = Student.objects.get(id=id)
    template = loader.get_template('student_details.html')
    context = {
        'students_list': students,
    }
    return HttpResponse(template.render(context, request))

 
def add_information(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        contact_number = request.POST.get('contact_number')
        course_name = request.POST.get('course')
        year_level_name = request.POST.get('Year_level')
        subject_name = request.POST.get('subject')
        days = request.POST.get('days')
        time_start = request.POST.get('time_start')
        time_end = request.POST.get('time_end')


        course = Course.objects.filter(course=course_name).first()

        year_level, _ = YearLevel.objects.get_or_create(Year_level=year_level_name)

        student = Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            gender=gender,
            address=address,
            contact_number=contact_number,
            course_id=course,
            year_id=year_level
        )

        subject, _ = Subject.objects.get_or_create(subject=subject_name)

        schedule = Schedule.objects.create(
            time_start=time_start,
            time_end=time_end,
            days=days,
            subject=subject
        )

        return HttpResponseRedirect(reverse('student_list')) 
    else:
        return render(request, 'my_admin.html')

#delete students function
def delete(request, id):
    students = Student.objects.get(id=id)
    students.delete()
    return HttpResponseRedirect(reverse('students'))


#update students details
def update(request, id):
  students = Student.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'students_list': students,
  }
  return HttpResponse(template.render(context, request))

#update record send to data base the new input details of students
def updaterecord(request, id):
  firstname = request.POST['firstname']
  lastname = request.POST['lastname']
  age = request.POST['age']
  course = request.POST['course']
  students = Student.objects.get(id=id)
  students.firstname = firstname
  students.lastname = lastname
  students.age = age
  students.course = course
  students.save()
  return HttpResponseRedirect(reverse('students'))