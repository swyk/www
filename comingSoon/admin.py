from django.contrib import admin

from .models import *

# Register your models here.


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['pk','email','timestamp']


class EmailAdmin(admin.ModelAdmin):
    list_display = ['id','subject','timestamp']

admin.site.register(Subscriber,SubscriberAdmin)
admin.site.register(Email,EmailAdmin)