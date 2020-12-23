from django.contrib import admin


from .models import image_upload


from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.









class image_uploadadmin(admin.ModelAdmin):
	list_display = ("user", "name","Img")
	actions = None



	#fields=[
	#"user_id",
	#"name",
	#"Img",
	#]
	def save_model(self, request, obj, form, change):
		if not obj.user:
			obj.user = request.user
		obj.save()

	#def save_model(self, request, obj, form, change):
	#	if getattr(obj, 'user_id', None) is None:
	#	  obj.user_id = request.user.id
	#	obj.save()




admin.site.register(image_upload, image_uploadadmin)