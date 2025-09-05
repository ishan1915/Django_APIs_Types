from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#classroom is use instead of class,because class is a keyword and cannot use as variable name
class Classroom(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10,null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)


    def __str__(self):
        return f"{self.name}-{self.classroom}"



class Teacher(models.Model):
    name=models.CharField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE) 
    phone=models.CharField(max_length=10,null=True)
    email=models.EmailField(null=True)
    address=models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student=models.ManyToManyField(Student)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
