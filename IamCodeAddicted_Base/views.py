from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import csrf
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.template.context import RequestContext

import requests
from datetime import datetime

from .forms import LoginForm, RegisterForm, CustomUserCreationForm

# class MovieList(ListView):
#     model = Movie
#     context_object_name = 'movies'

class MovieDetail(LoginRequiredMixin ,DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'IamCodeAddicted_Base/movie.html'


def movies(request):
    return render(request, 'IamCodeAddicted_Base/movie_list.html')


def bought_movies(request):
    return render(request, 'IamCodeAddicted_Base/bought.html')

# class LoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'IamCodeAddicted_Base/login.html'
#     success_url = reverse_lazy('movies')


def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            
            login(request, user)

            data =  {
                "email":username,
                "password":password
            }
            resp = requests.post('http://127.0.0.1:8000/api/login/', data=data)

            in_return = resp.json()

            print(in_return)
            return redirect('movies')

    context = {}
    return render(request, 'IamCodeAddicted_Base/login.html', context)

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'IamCodeAddicted_Base/register.html'
    success_url = reverse_lazy('login')
