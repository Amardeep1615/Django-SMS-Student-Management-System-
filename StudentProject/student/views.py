from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def  home(request):
    url=f'''
    <h1> Hi My Name is Robert Mark </h1>
    <p> This is a Student App </p>
    <h2>Welcome to Student Management Application</h2>'''
    return render (request,'student/home.html')


    