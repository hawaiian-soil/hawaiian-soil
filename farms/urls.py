from django.urls import path
from . import views


app_name = 'farms'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.profile_form, name='profile_form'),
    path('profile/', views.profile, name='profile'),

    # Registration Urls
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]