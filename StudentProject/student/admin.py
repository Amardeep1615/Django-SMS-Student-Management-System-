from django.contrib import admin
from .models import Student
# Register your models here.

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["student_id", "student_name","student_branch","student_email","student_phone" ]
    search_fields = ["student_id", "student_name","student_branch"]
    list_filter = ["student_email","student_branch"]

