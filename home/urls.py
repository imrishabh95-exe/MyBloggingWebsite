from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header  =  "Rishabh's Blog Admin"  
admin.site.site_title  =  "Rishabh's Blog Admin Portal"
admin.site.index_title  =  "Welcome to Rishabh's Blog"

urlpatterns = [
    path('', views.index, name= 'home'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),
    path('services', views.services, name= 'services'),
    path('donate', views.donate, name= 'donate'),
]