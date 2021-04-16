from django.urls import path, include
from .views import (
    MoviesListApiView,
    UserMovieDetail,
    MoviesPurchaseApiView,
    MoviePurchaseUserApi
)


urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', UserMovieDetail.as_view()),
    path('purchase/', MoviesPurchaseApiView.as_view()),
    path('purchase/<int:movie_id>', MoviePurchaseUserApi.as_view()),
]

