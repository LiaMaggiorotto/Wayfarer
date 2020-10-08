from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import City, Profile, Post
# Create your views here.

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cities_index')
        error_message +='\nInvalid sign up - try again'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)



def home(request):
    return render(request, 'home.html')

def cities_index(request):
    #handle index all cities
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request, 'cities/index.html', context)
