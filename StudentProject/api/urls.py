
from django.urls import path
from . import views

urlpatterns = [
    path('apis/',views.studentsView),
    path('api/<int:id>/',views.studentsDetailView),
]