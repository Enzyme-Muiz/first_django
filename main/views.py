from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import login_time, image_upload

#from django.shortcuts import render
from .forms import UserForm, NewUserForm, ImageForm
from .methods import Allah
from .forms import *
from subprocess import run, PIPE, Popen
import sys
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def homepage(request):

    submitbutton= request.POST.get("submit")

    firstname=''
    lastname=''
    emailvalue=''
    number=''
    numberi=''
    another=''

    form= UserForm(request.POST or None)
    if form.is_valid():
        firstname= form.cleaned_data.get("first_name")
        lastname= form.cleaned_data.get("last_name")
        emailvalue= form.cleaned_data.get("email")
        number = form.cleaned_data.get("number")
        numberi= Allah(number)
        another = form.cleaned_data.get("another")
        

    context= {'form': form, 'firstname': firstname, 'lastname':lastname,
              'submitbutton': submitbutton, 'emailvalue':emailvalue, 
              'numberi': numberi, 'another': another}
        
    return render(request, 'main/home.html', context)
    




  
# Create your views here. 
def image_uploads(request): 
    list_name= ["Mubaarak", "Nabeel", "Abdul-Mujeeb"]
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            fs= form.save(commit=False)
            fs.user= request.user 
            fs.save()
            send_mail("Received",
                "This is an automated email. Do not respond please",
                "muizdeenoyebode@gmail.com",
               ["oaonatraji@gmail.com", "muizdeenraji@gmail.com"],
               fail_silently= False )
            name= form.cleaned_data.get("name")
            messages.success(request, f" {name}")
            

            return redirect('success') 
    else: 
        form = ImageForm() 
    return render(request, 'image_upload.html', {'form' : form, 'names': list_name}) 
def success(request): 
    return HttpResponse('successfully uploaded') 


def register(request):
    if request.method =="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            username= form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")

            return redirect('homepage')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")
    form = NewUserForm
    
    return render(request,
        'main/register.html',
        {'form': form}
        ) 
 

def logout_request(request):
    logout(request)
    messages.info(request, "logged out successfully!")
    return redirect("homepage")





def login_request(request):
    if request.method == "POST":
        form= AuthenticationForm(request, request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user= authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                user=request.user
                login_time.objects.create(user= request.user)
                response= redirect('homepage')
                response.set_cookie('username', username) 
                return response
            else:
                messages.error(request, "invalid username and password")
        else:
            messages.error(request, "invalid username and password")





    form = AuthenticationForm()
    if 'username' in request.COOKIES:
       username = request.COOKIES['username']
       return render(request,
        "main/login.html",
        {"form": form, "username" : username}
        )
    else:
        return render(request,
        "main/login.html",
        {"form": form,})


def account(request): 
    login_number = login_time.objects.filter(user= request.user).count()
    Mubaarak_picture = (image_upload.objects.filter(name= 'Mubaarak').count()*100)//100
    Nabeel_picture = (image_upload.objects.filter(name= 'Nabeel').count()*100)//100
    Abdul_Mujeeb_picture = (image_upload.objects.filter(name= 'Abdul-Mujeeb').count()*100)//100
    Products = image_upload.objects.all()
    context= {"number":login_number, "numberi": str(Mubaarak_picture)+ "%", "numberii": str(Nabeel_picture)+ "%", "numberiii": str(Abdul_Mujeeb_picture)+ "%",
    "class_mub": "c100 p"+str(Mubaarak_picture),
    "class_nab":"c100 p"+str(Nabeel_picture),
    "class_abs":"c100 p"+str(Abdul_Mujeeb_picture),
    'products':Products} 
    return render(request, 'main/account.html', context)



def delete(request, id):
    image_upload.objects.get(id=id).delete()
    return redirect(account)



   