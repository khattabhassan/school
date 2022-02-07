from re import M
from django.db import models

# Create your models here.

class Student(models.Model): 
    student_Name = models.CharField(max_length=200)
    student_Email = models.EmailField(max_length=200)
    student_Password = models.IntegerField
    student_address = models.CharField(max_length=200)
    student_phone = models.IntegerField
    student_id = models.IntegerField
    student_photo = models.FileField
    def __str__(self):
        return self.Student_Name

class School (models.Model): 
    school_Name = models.CharField(max_length=200)
    school_Email = models.EmailField(max_length=200)
    school_Password = models.IntegerField
    school_address = models.CharField(max_length=200)
    school_phone = models.IntegerField
    school_id = models.IntegerField
    school_photo = models.FileField 
    school_type = models.CharField 
    school_stage = models.CharField  
    def __str__(self): 
        return self.school_Name
