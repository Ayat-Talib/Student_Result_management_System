from django.contrib import admin
from .models import Student, Subject, Result

# Register Student model
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'email', 'class_name']
    search_fields = ['name', 'roll_no']

# Register Subject model (YEH IMPORTANT HAI!)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    search_fields = ['name']

# Register Result model
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks_obtained', 'percentage']
    list_filter = ['student', 'subject']