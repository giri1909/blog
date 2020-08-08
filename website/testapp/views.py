from django.http import HttpResponse, HttpResponseRedirect


def Home(request):
	return HttpResponse('<body bgcolor="yellow"> Welcome to test app page home page<br></body>')

from django.shortcuts import render
from .models import Employee

def Employees(request):
	context={'empdb':Employee.objects.all()}
	return render(request,'emp.html',context)


def testappTest(request):
    context={}
    return render(request,'testapp/test.html',context)

"""

from .forms import NameForm
def Name(request):

	if request.method == 'POST':
		form = Name(request.POST)
		# print(form.is_valid())
		# when your form is valid
		if form.is_valid():
			name = form.cleaned_data['name']
			mail = form.cleaned_data['mail']
			mno = form.cleaned_data['mno']
			message = form.cleaned_data['message']
			Name.objects.create(name=name, mail=mail, mno=mno,message=message)
			# To create the                                                                                     #table in the                                                                                     #database
			return HttpResponseRedirect('/blog/thanks/')
		# when my form is not valid
		else:
			context = {'form': form}
			return render(request, 'testapp/contactform.html', context)
	# GET
	else:
		form = NameForm
		context = {'form': form}
		return render(request, 'testapp/contactform.html', context)
"""
