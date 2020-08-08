from django.db import models
# Create your models here.
class Employee(models.Model):
	empno=models.IntegerField()
	ename=models.CharField(max_length=30)
	ejob=models.CharField(max_length=30,blank=True,null=0)
	esal=models.FloatField()
	deptno=models.IntegerField(default=0) #<==It will show 0 by default in the deptno textfield.

	def __str__(self):           # <==================added
		return self.ename

class Student(models.Model):
	sname=models.CharField(max_length=30)
	course=models.CharField(max_length=30)
	phno=models.IntegerField()
	email=models.EmailField(max_length=80)

	def __str__(self):          
		return self.sname
"""
class Name(models.Model):
	fname = models.CharField()
	lname = models.CharField()

	def __str__(self):
		return self.fname
"""
