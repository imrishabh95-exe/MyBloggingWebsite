from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

theme = 'light'
# Create your views here.
def index(request):
    #return HttpResponse("This is home page")
    args = {
        'theme' : 'dark',
        #'theme' : 'light',
        'variable' : 'This is sent',
    }
    return render(request, 'index.html', args)

def services(request):
    #return HttpResponse("This is services page")
    args = {
        'theme' : 'dark',
        #'theme' : 'light',
        'variable' : 'This is sent',
    }
    return render(request, 'services.html', args)

def about(request):
    #return HttpResponse("This is about page")
    args = {
        'theme' : 'dark',
        #'theme' : 'light',
        'variable' : 'This is sent',
    }
    return render(request, 'about.html', args)

def contact(request):
    #return HttpResponse("This is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thanks for the feedback!')
    args = {
        'theme' : 'dark',
        #'theme' : 'light',
        'variable' : 'This is sent',
    }
    return render(request, 'contact.html', args)

def donate(request):
    #return HttpResponse("This is contact page")
    args = {
        'theme' : 'dark',
        #'theme' : 'light',
        'variable' : 'This is sent',
    }
    return render(request, 'donate.html', args)