from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from farms.forms import SignUpForm


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


def login(request):
    template_path = 'registration/login.html'
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
    }
    return render(request, template_path, context)


def signup(request):
    template_path = 'registration/signup.html'
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    context = {
        'title': "Hawaiian Soil",
        'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
        'form': form,
    }
    return render(request, template_path, context)

