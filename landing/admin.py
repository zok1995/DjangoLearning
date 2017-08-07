from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"] #hand made
    list_display = [field.name for field in Subscriber._meta.fields] #use itertor for every field name from DB
    # exclude = ["email"] #hide field
    list_filter = ['name', 'email']  #filter record in admin
    search_fields = ["name"] #find by in admin

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)