from django.db import models

# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    grade=models.CharField(max_length=10)
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return f"{self.name} is in grade {self.grade}"
    
class Teacher(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='teachers')

    def __str__(self):
        return f"{self.name} teaches {self.subject}"  