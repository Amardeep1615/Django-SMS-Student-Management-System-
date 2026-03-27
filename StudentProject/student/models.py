from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=10)
    student_name = models.CharField(max_length=50)
    student_branch = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=20)
    student_phone = models.CharField(max_length=10)


def __str__(self):
    return self.name


