from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Farmer, Farm

# Register your models here.
admin.site.register(Farmer, UserAdmin)
admin.site.register(Farm)
