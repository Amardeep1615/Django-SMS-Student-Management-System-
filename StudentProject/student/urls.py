
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('student/',views.home),
   


    
]
admin.site.site_title = 'Student Management System'
admin.site.site_header = 'Student Admin'
admin.site.index_title = 'Student Portal'