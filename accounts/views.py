# Django http and shortcuts import
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# From Contrib
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Django User
from django.contrib.auth.models import User

# App Forms
from accounts.forms import RegisterForm


# Create your views here.
def signup_view(request):
    """
    POST method with email and username and password register new user
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)

            # Successfull login redirect to login page
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            # If error found we need to show to the frontend using form errors
            # Returning same form contains context of errors attripute
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        # Get method should return empty Form
        register_form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': register_form})


def login_view(request):
    """
    Login view function takes no arguemnt if supplied username and password
    matches then request will authenticate with login and return with User context
    """
    if request.method == 'POST':

        # Will not throw error because input have value=""
        username = request.POST['username']
        password = request.POST['password']

        # Check the user in database or return
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user:
                # Password matching and user found with authenticate
                login(request, user)
                return HttpResponseRedirect(reverse('frontend:home'))
            else:
                # Password wrong
                messages.error(request, 'Username or Password is wrong')
        except:
            messages.error(request, "User not found")
            return HttpResponseRedirect(reverse('accounts:login'))
    return render(request, 'accounts/login.html')


def logout_view(request):
    """ Remove user from the request """
    logout(request)
    return HttpResponseRedirect(reverse("frontend:home"))


def profile(request):
    """
    Profile takes no arugment and returns the listings attripute
    """
    listings = [1,2,3,4,5,5]
    return render(request, 'accounts/profile.html', {'listings': listings})
