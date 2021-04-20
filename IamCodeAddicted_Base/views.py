from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie, MoviesPurchase, CustomUser
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context_processors import csrf
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.template.context import RequestContext
import logging
from django.db import IntegrityError
from django.contrib import messages

from .forms import LoginForm, CustomUserCreationForm,MoviePurchaseForm


logger = logging.getLogger(__name__)

class MovieDetail(LoginRequiredMixin ,DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'IamCodeAddicted_Base/movie.html'



# class BuyTicket(LoginRequiredMixin, CreateView):
#     model = MoviesPurchase
#     fields = ['user', 'movie']
#     template_name = 'IamCodeAddicted_Base/buyticket.html'
#     success_url = reverse_lazy('bought')


def buy_ticket(request):
    model = Movie.objects.all()
    user_id = request.user.id
    template_name = 'IamCodeAddicted_Base/buyticket.html'
    if request.method == 'POST':
        mp = MoviesPurchase(movie_id=request.POST.get('movie', None), user_id=user_id)
        if request.user.is_authenticated:
            try:
                mp.save()
            except IntegrityError as err:
                messages.add_message(request, messages.ERROR, "Już kupiłeś bilet na ten film")
                redirect('bought')         
        return redirect('bought')

    return render(request, template_name, {"model":model})



class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'IamCodeAddicted_Base/movie_list.html'
    



class MoviePurchaseList(LoginRequiredMixin, ListView):
    model = MoviesPurchase
    context_object_name = 'movies'
    template_name = 'IamCodeAddicted_Base/bought.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = context['movies'].filter(user=self.request.user)
        return context


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'IamCodeAddicted_Base/login.html'
    success_url = reverse_lazy('movies')



# def login_(request):
#     context = {}
#     response = render(request, 'IamCodeAddicted_Base/login.html', context)
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
            
#             login(request, user)
#             # data =  {
#             #     "email":username,
#             #     "password":password
#             # }
#             # token = handle_token_request(data)
#             # resp_2 = HttpResponseRedirect('/')
#             # resp_2.set_cookie('jwt_token', token['token'])
#             return redirect('movies')

#     context = {}
#     return response

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'IamCodeAddicted_Base/register.html'
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('movies')
        return super(RegisterView, self).get(*args, **kwargs)