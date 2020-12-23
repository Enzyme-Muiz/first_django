from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import widgets


class UserForm(forms.Form):
	
	first_name= forms.CharField(max_length=100)
	last_name= forms.CharField(max_length=100)
	email= forms.EmailField()
	number= forms.FloatField()
	another= forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '2'})) 
	filea= forms.FileField()

class NewUserForm(UserCreationForm):
	email= forms.EmailField(required= True)


	class Meta:
		model= User
		fields=("username", "email","password1", "password2")
	def save(self, commit= True):
		user= super(NewUserForm, self).save(commit= False)
		user.email= self.cleaned_data["email"]
		if commit:
			user.save()
		return user




class ImageForm(forms.ModelForm):
	#def __init__(self, *args, **kargs):
	#	super(ImageForm, self).__init__(*args, **kargs)
	name = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices= image_upload.COUNTRY_CHOICES,
    )
	class Meta:
		model = image_upload
		fields = ('name', 'Img')

		



		
