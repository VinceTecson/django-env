from django.contrib import admin
from .models import Course, YearLevel, Student, Teacher, Subject, Schedule, Attendance

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course', 'description')

class YearLevelAdmin(admin.ModelAdmin):
    list_display = ('Year_level',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'gender', 'address', 'contact_number', 'course_id', 'year_id')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'description', 'section')

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('time_start', 'time_end', 'days', 'subject', 'teacher')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('status', 'date', 'time')



admin.site.register(Course, CourseAdmin)
admin.site.register(YearLevel, YearLevelAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Attendance, AttendanceAdmin)
