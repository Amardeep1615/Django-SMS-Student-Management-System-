from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse,HttpResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework import mixins,generics,viewsets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from .paginators import CustomPagination
from employees.filters import EmployeeFilter
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
         
# class Employees(APIView):
#    def get(self,request):
#       employees = Employee.objects.all()
#       serializers = EmployeeSerializer(employees,many=True)
#       return Response(serializers.data,status=status.HTTP_200_OK)
   
#    def post(self,request):
#       serializers = EmployeeSerializer(data=request.data)
#       if serializers.is_valid():
#          serializers.save()
#          return Response(serializers.data,status=status.HTTP_201_CREATED)
#       return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
   

# class EmployeeDetail(APIView):
#    def get_object(self,id):
#       try:
#          return Employee.objects.get(id=id)
#       except Employee.DoesNotExist:
#          raise Http404
      
#    def get(self,request,id):
#       employee = self.get_object(id)
#       serializer = EmployeeSerializer(employee)
#       return Response(serializer.data,status=status.HTTP_200_OK)
   
#    def put(self,request,id):
#       employee = self.get_object(id)
#       serializer = EmployeeSerializer(employee,data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
#    def patch(self,request,id):
#       employee = self.get_object(id)
#       serializer = EmployeeSerializer(employee,data=request.data,partial=True)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
#    def delete(self,request,id):
#       employee = self.get_object(id)
#       employee.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)
   
# #Mixins
# class Employees(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#    queryset = Employee.objects.all()
#    serializer_class = EmployeeSerializer

#    def get(self,request):
#       return self.list(request)
   
#    def post(self,request):
#       return self.create(request)
   
# #Mixins
# class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

#    queryset = Employee.objects.all()
#    serializer_class = EmployeeSerializer
#    lookup_field = 'id'
  
   
#    def get(self,request,id):
#       return self.retrieve(request,id)
   
#    def put(self,request,id):
#       return self.update(request,id)
   
#    def delete(self,request,id):
#       return self.destroy(request,id)


      
"""
#Generics
class Employees(generics.ListCreateAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer

#Generics
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   lookup_field = 'id'
"""


"""
#ViewSets
class EmployeeViewSet(viewsets.ViewSet):
   lookup_field = 'id'
   def list(self,request):
      queryset = Employee.objects.all()
      serializer = EmployeeSerializer(queryset,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def create(self,request):
      serializer = EmployeeSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   
   def retrieve(self,request,id = None):
      employee = get_object_or_404(Employee,id = id )
      serializer = EmployeeSerializer(employee)
      return Response(serializer.data,status=status.HTTP_200_OK)
   
   def update(self,request,id = None):
      employee = get_object_or_404(Employee,id = id)
      serializer = EmployeeSerializer(employee)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

   def delete(self,request,id = None):
      employee = get_object_or_404(Employee,id=id)
      employee.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

"""   

class EmployeeViewSet(viewsets.ModelViewSet):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializer
   pagination_class = CustomPagination
   filterset_class = EmployeeFilter



class BlogsView(generics.ListCreateAPIView):
   queryset = Blog.objects.all()
   serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Blog.objects.all()
   serializer_class= BlogSerializer
   lookup_field = 'id'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializer
   lookup_field = 'id'
   





