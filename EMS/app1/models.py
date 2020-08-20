from django.db import models
from django.utils.timezone import now

# Create your models here.

    fno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    uname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dept = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    password= models.CharField(max_length=50)


class Studentreg(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=50)
    uname = models.CharField(max_length=30)
    depart = models.CharField(max_length=49)
    emailid = models.EmailField(unique=True)
    contactno = models.IntegerField(unique=True)
    pwd = models.CharField(max_length=30)

class SessionModel(models.Model):
    cid = models.AutoField(primary_key=True)
    subn=models.CharField(max_length=49)
    facname=models.CharField(max_length=49)
    date = models.DateField()
    time = models.TimeField()
    duration= models.CharField(max_length=50)

class SchdexamsModel(models.Model):
    eno = models.AutoField(primary_key=True)
    sem = models.CharField(max_length=49)
    date = models.DateField()
    time = models.TimeField()
    fee = models.FloatField()
    duration = models.CharField(max_length=50)
    timetable = models.FileField(upload_to="timetable/")

class AssignmentModel(models.Model):
    ano = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=49)
    date = models.DateField()
    assign = models.FileField(upload_to="assignment/")

class SubmitAssignment(models.Model):
    subno = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=50)
    date = models.DateTimeField(default=now, editable=False)
    submit = models.FileField(upload_to="Sub Assign/")
    student_reg = models.ForeignKey(Studentreg,on_delete=models.CASCADE)

#class SubmitAssignment(models.Model):




