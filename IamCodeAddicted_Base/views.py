from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Movie


class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'


class MovieDetail(DetailView):
    model = Movie