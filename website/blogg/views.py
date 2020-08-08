
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Product(request):
	return HttpResponse('<body bgcolor="yellow"> Welcome to my Product page<br></body>')

def Hello(request):
	return HttpResponse('<body bgcolor="yellow"> Hello!!! Welcome to my blog page<br></body>')

def HelloTemplate(request):
	context={}
	return render(request,'hello.html',context)

def ProductStatic(request):
    context={}
    return render(request,'prod.html',context)

def ProductDynamicOneRecord(request):
    context={'pid':1001,'pname':'Django Framework','price':450,'author':'Milton'}
    return render(request,'prodonedy.html',context)
    
def Products(request):
    context={'proddb':[
    {'pid':101,'pname':'Dive into python 3','price':450,'author':'Milton'},
    {'pid':102,'pname':'Python algorithms','price':550,'author':'Charles'},
    {'pid':103,'pname':'Networking python','price':650,'author':'Miller'},
    {'pid':104,'pname':'Advanced python','price':350,'author':'Robert'},
    {'pid':105,'pname':'Python for automation','price':367,'author':'Smith'}
                      ]}

    return render(request,'productsmultiple.html',context)

from .models import Post   

def BlogData(request):  #<==========Added
    context={'blogdb':Post.objects.all()}
    return render(request,'blog_data.html',context)

from django.shortcuts import render

def bloggTest(request):
    context={}
    return render(request,'blogg/test.html',context)


def Thanks(request): #<==========added
    return HttpResponse("Thank you and Have a great day!!!,I will inform you soon")

from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import EmailMessage

from .forms import ContactForm

def Contact(request):  #<==========added
    
    # GET REQUEST
    form_class = ContactForm  # class not a instance
    context = {'form':form_class}
    
    # POST REQUEST
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            phno=form.cleaned_data['phno']
            content = form.cleaned_data['text']
            subject = "A new contact or lead - {}".format(contact_name)
            email = EmailMessage(subject, contact_name + '\n' + contact_email + '\n' + str(phno) +'\n'+content , to=['home.giri1909@gmail.com'])
            email.send()
            return HttpResponseRedirect('/blog/thanks/') #project-url/app-url       
    return render(request,'blogg/blog_contact.html',context)



from .forms import EnqDBForm
from .models import EnqDB

def  StudentInsert(request) :   
    

    # POST
    if request.method == 'POST':
        form = EnqDBForm(request.POST)
        #print(form.is_valid())
        # when your form is valid
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            mno = form.cleaned_data['mno']
            message = form.cleaned_data['message']
            EnqDB.objects.create(name=name,mail=mail,mno=mno,message=message) #To create the                                                                                     #table in the                                                                                     #database
            return HttpResponseRedirect('/blog/thanks/')
        # when my form is not valid
        else:
            context = {'form':form}
            return render(request,'blogg/contactform.html',context)
    # GET
    else:
        form = EnqDBForm
        context={'form':form}
        return render(request,'blogg/contactform.html',context)


from .forms import PostForm  # <==========Added from here
from .models import Post


def BlogPost(request):
    print(request.method)  # To see which method has been called
    # GET REQUEST
    form_class = PostForm  # class not a instance
    context = {'form': form_class}

    # POST REQUEST
    if request.method == 'POST':
        form = PostForm(request.POST)
        # print(form.is_valid())
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            created_date = form.cleaned_data['created_date']
            Post.objects.create(author=author, title=title, text=text, created_date=created_date)
            return HttpResponseRedirect('/blog/thanks/')
    return render(request, 'blogg/post_blog.html', context)


def Home(request):
    context={}
    return render(request,'home.html',context)

