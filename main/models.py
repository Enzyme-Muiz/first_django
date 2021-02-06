from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.utils import timezone




class image_upload(models.Model): 
	COUNTRY_CHOICES = (
    ('Mubaarak','Mubaarak'),
    ('Nabeel','Nabeel'),
    ('Abdul-Mujeeb','Abdul-Mujeeb'),
   
    )
	user= models.ForeignKey(User, on_delete= models.CASCADE, editable= False, blank= True, null=True)
	name = models.CharField(max_length=50, choices= COUNTRY_CHOICES, blank=True) 
	Img = models.ImageField(upload_to='images/')
	date= models.DateTimeField(auto_now_add= True)
	
	def __str__(self): 
		return self.name
	
class login_time(models.Model):
    user=  models.ForeignKey(User, on_delete= models.CASCADE, editable= False, blank= True, null=True)
    date= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return str(self.user) + ': ' + str(self.date)