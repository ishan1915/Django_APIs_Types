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
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE,related_name="students")
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


    def __str__(self):
        return self.name


class TimeTable(models.Model):
    DAYS=[
          ("monday","monday"),
          ("tuesday","tuesday"),
          ("wednesday","wednesday"),
          ("thursday","thursday"),
          ("friday","friday"),
          ("saturday","saturday"),
        ]
    
    Time=[
        ("09:00-10:00","09:00 - 10:00 AM"),
        ("10:00-11:00","10:00 - 11:00 AM"),
        ("11:00-12:00","11:00 - 12:00 PM"),
        ("12:00-01:00","12:00 - 01:00 PM"),
        ("01:00-02:00","01:00 - 02:00 PM"),
        ("02:00-03:00","02:00 - 03:00 PM"),
        ("03:00-04:00","03:00 - 04:00 PM"),
    ]

    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    classroom=models.ForeignKey(Classroom,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    days=models.CharField(max_length=20,choices=DAYS)
    time=models.CharField(max_length=20,choices=Time)


    def __str__(self):
        return f"{self.subject}-{self.classroom}-{self.days}-{self.time}"
    


class Exam(models.Model):
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    date=models.CharField(max_length=20)



    def __str__(self):
        return f"{self.name}-{self.subject}-{self.date}"