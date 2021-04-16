from django.urls import path, include
from .views import (
    MoviesListApiView,
    UserMovieDetail,
    MoviesPurchaseApiView,
    MoviePurchaseUserApi,
    HelloView
)
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', MoviesListApiView.as_view()),
    path('<int:movie_id>/', UserMovieDetail.as_view()),
    path('purchase/', MoviesPurchaseApiView.as_view()),
    path('purchase/<int:movie_id>', MoviePurchaseUserApi.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloView.as_view(), name='hello'),
]

