from django.urls import path
from .views import MovieList, MovieDetail


urlpatterns = [
    path('', MovieList.as_view(), name='movies'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie')
]

