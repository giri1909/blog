from django.db import models

# Create your models here.
from django.utils import timezone
 
class Post(models.Model):
	author=models.ForeignKey('auth.user')
	title=models.CharField(max_length=30)
	text=models.TextField()                      
	created_date=models.DateTimeField(default=timezone.now()) 
	published_date=models.DateField(blank=True,null=True) 
	
	def __str__(self):
		return self.title


from django.db import models
from django.utils import timezone
from django import forms
class EnqDB(models.Model) :
	name=models.CharField(max_length=30)
	mail=models.CharField(max_length=30)
	mno=models.IntegerField()
	message=models.CharField(max_length=60)
	
	def __str__(self):
		return self.name


