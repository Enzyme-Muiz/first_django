"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
appname = "main"

urlpatterns = [
    path('', views.homepage, name= "homepage"),
    path('image_uploads', views.image_uploads, name = 'image_uploads'), 
    path('success', views.success, name = 'success'),
    path('register', views.register),
    path('logout', views.logout_request, name= "logout"),
    path('login', views.login_request, name= "login"),
    path('account', views.account, name= "account"),
    path('delete/<int:id>', views.delete, name= "delete"),
    path('func', views.apisample.as_view(), name= "api_sample"),
    path('message', views.message, name= "message"),
    
    
    
    
    

]



if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 