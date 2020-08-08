from django import forms

class ContactForm(forms.Form) :
	contact_name=forms.CharField(max_length=30,required=True)
	contact_email=forms.CharField(required=True)
	phno=forms.IntegerField()
	text=forms.CharField(widget=forms.Textarea())	


from .models import EnqDB

class EnqDBForm(forms.ModelForm) :
    class Meta :
        model = EnqDB
        fields = ('name','mail','mno','message')# Write only the attributes of the EnqDB class

from .models import Post   #<====added from here

class PostForm(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ('author','title','text','created_date')
