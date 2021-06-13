from django.contrib import admin

from .models import *
from django.contrib import admin
from .models import *

# Register your models here.

class SmartProPost(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']
    list_display_links = ['title']

    class Meta:
        model = SmartPro

admin.site.register( SmartPro,SmartProPost  )
admin.site.register(Event)
