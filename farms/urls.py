from django.urls import include, path
from django.contrib import admin
from . import views


app_name = 'farms'
urlpatterns = [
    # Hawaiian Soil Urls
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.profile_form, name='profile_form'),
    path('profile/', views.profile, name='profile'),

    # Registration Urls
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]