from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# App Forms
from accounts.forms import RegisterForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save(commit=False)

            email = register_form.cleaned_data['email']
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)

            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            print register_form.errors
            return render(request, 'login.html', {'form': register_form})
    else:
        register_form = RegisterForm()
    return render(request, 'signup.html', {'form': register_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('frontend:home'))
        except:
            return render(request, 'login.html')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("frontend:home"))
