from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farms.forms import FarmerForm


def index(request):
    template_path = 'farms/index.html'
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
    }
    return render(request, template_path, context)


def profile(request):
    template_path = 'farms/profile.html'
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
    }
    return render(request, template_path, context)


def profile_form(request):
    template_path = 'farms/profile_form.html'
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
    }
    return render(request, template_path, context)
    # return HttpResponse(template.render({}, request))


def about(request):
    template_path = 'farms/about.html'
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
    }
    return render(request, template_path, context)

#
# def login(request):
#     template_path = 'farms/login.html'
#     context = {
#         'title': "Hawaiian Soil",
#         'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
#     }
#     return render(request, template_path, context)


def signup(request):
    template_path = 'farms/signup.html'
    if request.method == 'POST':
        form = FarmerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            login(request, user)
            return redirect('..')
    else:
        form = FarmerForm()
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
        'form': form,
    }
    return render(request, template_path, context)

