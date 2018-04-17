from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Farmer

# Register your models here.
admin.site.register(Farmer, UserAdmin)
