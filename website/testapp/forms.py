from django import forms

class ContactForm(forms.Form) :
	contact_name=forms.CharField(max_length=30,required=True)
	contact_email=forms.CharField(required=True)
	phno=forms.IntegerField()
	text=forms.CharField(widget=forms.Textarea())

"""
from .models import Name  #<====added from here

class NameForm(forms.Form) :
	fname = forms.CharField(max_length=30)
	lname = forms.CharField(max_length=30)

"""
