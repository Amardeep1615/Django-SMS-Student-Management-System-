
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewSet,basename='employee')

urlpatterns = [
    path('apis/',views.studentsView),
    path('api/<int:id>/',views.studentsDetailView),

    # path('employees/',views.Employees.as_view()),
    # path('employee/<int:id>/',views.EmployeeDetail.as_view()),

    path('',include(router.urls))
    
    ]