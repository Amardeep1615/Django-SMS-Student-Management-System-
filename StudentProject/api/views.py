from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

# def apiv1 (request):

    # students = Student.objects.all()
    # #Simple Usecase Serializer not recommended for the restapis just a manual use
    # student_list = list(students.values())
    # return JsonResponse(student_list,safe=False)

@api_view(['GET','POST'])
def studentsView(request):
   if request.method == 'GET':
      students = Student.objects.all()
      serializer = StudentSerializer(students,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   elif request.method == 'POST':
      serializer = StudentSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      print(serializer.errors)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])    
def studentsDetailView(request,id):
   try:
      student = Student.objects.get(id=id)
   except Student.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      serializer = StudentSerializer(student)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   elif request.method == 'PUT':
      serializer = StudentSerializer(student,data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      else:
         return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
   elif request.method == 'DELETE':
      student.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
         
