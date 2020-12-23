from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User



class image_upload(models.Model): 
	COUNTRY_CHOICES = (
    ('Mubaarak','Mubaarak'),
    ('Nabeel','Nabeel'),
    ('Abdul-Mujeeb','Abdul-Mujeeb'),
   
    )
	user= models.ForeignKey(User, on_delete= models.CASCADE, editable= False, blank= True, null=True)
	name = models.CharField(max_length=50, choices= COUNTRY_CHOICES, blank=True) 
	Img = models.ImageField(upload_to='images/') 
	
	def __str__(self): 
		return self.name
	

