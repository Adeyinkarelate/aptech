
from .views import *
from django.urls import path 

urlpatterns = [
    path('',IndexView, name="index"),
    path('contact/',ContactView, name="contact"),
    path('about/',AboutView, name="about"),
    path('WhyAptech/',WhyAptechView, name="aptech"),
    path('course/',CourseView, name="course"),
    path('pro/',proView, name="pro"),
    path('adse/',adseView, name="adse"),
    path('acns/',acnsView , name="network"),
  
]  
