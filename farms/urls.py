from django.urls import include, path
from django.contrib import admin
from . import views


app_name = 'farms'
urlpatterns = [
    # Hawaiian Soil Urls
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('form/', views.profile_form, name='profile_form'),


    # Registration Urls
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]