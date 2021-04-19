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
import logging
import requests
from datetime import datetime

from .forms import LoginForm, RegisterForm, CustomUserCreationForm


logger = logging.getLogger(__name__)

class MovieDetail(LoginRequiredMixin ,DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'IamCodeAddicted_Base/movie.html'


def movies(request):
    context = {}
    try:                     
        response = render(request, "IamCodeAddicted_Base/movie_list.html", context)
    except Exception as err:
        print(err)

    return response


def bought_movies(request):
    return render(request, 'IamCodeAddicted_Base/bought.html')

# class LoginView(LoginView):
#     form_class = LoginForm
#     template_name = 'IamCodeAddicted_Base/login.html'
#     success_url = reverse_lazy('movies')

def handle_token_request(data):
    resp = requests.post('http://127.0.0.1:8000/api/login/', data=data)
    in_return = resp.json()
    return in_return


def login_(request):
    context = {}
    response = render(request, 'IamCodeAddicted_Base/login.html', context)
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
            token = handle_token_request(data)
            resp_2 = HttpResponseRedirect('/')
            resp_2.set_cookie('jwt_token', token['token'])
            return resp_2

    context = {}
    return response

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'IamCodeAddicted_Base/register.html'
    success_url = reverse_lazy('login')
