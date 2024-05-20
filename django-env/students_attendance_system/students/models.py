from django.db import models

class Course(models.Model):
    course = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.course}"
    
class YearLevel(models.Model):
    Year_level = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Year_level}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=255, null=True)
    course_id=  models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    year_id= models.ForeignKey(YearLevel, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentYearLevel(models.Model):
    Student_id =  models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    Yearlevel_id=  models.ForeignKey(YearLevel, null=True, on_delete=models.CASCADE)

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    section = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subject}, {self.description}, {self.section}"

class Schedule(models.Model):
    time_start = models.CharField(max_length=255)
    time_end = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    subject=  models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    teacher=  models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id}"
    
class Attendance(models.Model):
    status = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
    time = models.TimeField(max_length=255)
    Student_id =  models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    Schedule_id =  models.ForeignKey(Schedule, null=True, on_delete=models.CASCADE)
    