from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farms.forms import SignUpForm, LoginForm


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


def signup(request):
    template_path = 'registration/signup.html'

    # Upon submission / a POST request from the SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Check if the form is valid with the model constraints
        if form.is_valid():
            user = form.save()      # Save the data from the signup
            user.refresh_from_db()  # load the profile instance created by the signal
            login(request, user)    # Login the user to their new account
            return redirect('..')   # Redirect the user to the home page
    else:
        form = SignUpForm()
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
        'form': form,
    }
    return render(request, template_path, context)


# def login(request):
#     template_path = 'farms/login.html'
#
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         # Check if the form is valid with the model constraints
#         if form.is_valid():
#             user = form.save()  # Save the data from the signup
#             #user.refresh_from_db()  # load the profile instance created by the signal
#             user = authenticate(request, username=user.username, password=user.password)
#             if user is not None:
#                 login(request, user)  # Login the user to their new account
#             return redirect('..')  # Redirect the user to the home page
#     else:
#         form = LoginForm()
#     context = {
#         'title': "Hawaiian Soil",
#         'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
#         'form': form,
#     }
#     return render(request, template_path, context)

