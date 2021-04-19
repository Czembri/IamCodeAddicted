from django.urls import path, include
from .views import movies, MovieDetail, login_, LoginView, RegisterView, bought_movies
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', movies, name='movies'),
    path('login/', login_,  name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie'),
    path('api/', include('IamCodeAddicted_Base.api.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('bought/', bought_movies, name='bought'),
]

