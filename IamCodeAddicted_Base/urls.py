from django.urls import path, include
from .views import MovieList, MovieDetail, LoginView, RegisterView, MoviePurchaseList, buy_ticket 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MovieList.as_view(), name='movies'),
    path('login/', LoginView.as_view(),  name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('movie/<int:pk>/', MovieDetail.as_view(), name='movie'),
    path('api/', include('IamCodeAddicted_Base.api.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('bought/', MoviePurchaseList.as_view(), name='bought'),
    path('buy/', buy_ticket, name='buy'),
]

