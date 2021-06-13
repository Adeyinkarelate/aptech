from django.shortcuts import  render 
from .models import *
from django.core.mail import message, send_mail
from django.conf import settings

def IndexView(request):
    event = Event.objects.get()
    context = {
        'event':event
    }
    return render(request,'app/index.html',context)



def ContactView(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        comment = request.POST.get('comment')
        email = request.POST.get('email')
      
        
        send_mail(
            fname,
            comment,
            email,
            ['aptechotacentre@gmail.com'],
            fail_silently=False,
            )
        return render(request,'app/email_sent.html',{'email':email})  
    return render(request,'app/contact.html',{})

def AboutView(request):
    return render(request,'app/about.html')

def WhyAptechView(request):
    return render(request,'app/whyaptech.html')

def CourseView(request):
    return render(request,'app/course.html')

def proView(request):
    context = {
        'pros' :SmartPro.objects.all()    
    }
    return render(request,'app/professional.html',context)

def adseView(request):
    return render(request,'app/adse.html')


def acnsView(request):
    return render(request,'app/acns.html')