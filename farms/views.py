from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from farms.forms import SignUpForm, ProfileForm, FarmForm


base_context = {
    'title': 'Hawaiian Soil',
    'crops': ['Potatoes', 'Tomatoes', 'Spinach'],
}


def index(request):
    template_path = 'farms/index.html'
    context = base_context
    return render(request, template_path, context)


@login_required
def home(request):
    template_path = 'farms/home.html'
    context = base_context
    return render(request, template_path, context)


@login_required
def farm(request):
    template_path = 'farms/farm.html'
    # Upon submission / a POST request from the Farm form
    if request.method == 'POST':
        form = FarmForm(data=request.POST)

        # Check if the form is valid with the model constraints
        print("Form is valid?: " + str(form.is_valid()))
        if form.is_valid():
            farm = form.save(commit=False)  # Save the data from the signup
            if farm.username is None:
                farm.username = request.user.get_username()
                print("Added username to " + farm.farm_name)
            farm.refresh_from_db()  # load the profile instance created by the signal
            farm.save()
            return redirect('/')  # Redirect the user to the home page
    # Request was probably a GET request and the user wants to see the form
    else:
        form = FarmForm()
    # Set context to the base
    context = base_context
    context['form'] = form
    return render(request, template_path, context)



@login_required
def profile(request):
    template_path = 'farms/profile.html'
    # Upon submission / a POST request from the SignUpForm
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)

        # Check if the form is valid with the model constraints
        if form.is_valid():
            user = form.save()  # Save the data from the signup
            user.refresh_from_db()  # load the profile instance created by the signal
            user.save()

            return redirect('/')  # Redirect the user to the home page
        print(form.is_valid())
    # Request was probably a GET request and the user wants to see the form
    else:
        form = ProfileForm()
    # Set context to the base
    context = base_context
    context['form'] = form
    return render(request, template_path, context)



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
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)    # Login the user to their new account
            return redirect('/')   # Redirect the user to the home page
    # Request was probably a GET request and the user wants to see the form
    else:
        form = SignUpForm()
    # Set context to the base
    context = base_context
    context['form'] = form
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

