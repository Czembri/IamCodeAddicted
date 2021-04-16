from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from IamCodeAddicted_Base.models import Movie, MoviesPurchase
from .serializers import MoviesSerializer, MoviePurchaseSerializer
from datetime import  datetime


class MoviesPurchaseApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def get(self, request,*args, **kwargs):
        user_purchase = MoviesPurchase.objects.all().filter(user_id=request.user.id)
        if not user_purchase:
            return Response(
                {"res":"Object does not exist or is not accessible"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MoviePurchaseSerializer(user_purchase, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MoviePurchaseUserApi(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def get(self, request, movie_id, *args, **kwargs):
        user_purchase = MoviesPurchase.objects.get(movie_id=movie_id, user_id=request.user.id)
        if not user_purchase:
            return Response(
                {"res":"Object does not exist or is not accessible"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MoviePurchaseSerializer(user_purchase)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, movie_id,*args, **kwargs):
        data = {
            'date_of_purchase': datetime.now(),
            'movie_id': movie_id,
            'user_id':request.user.id
        }

        serializer = MoviePurchaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, movie_id, *args, **kwargs):
        user_purchase = MoviesPurchase.objects.get(movie_id=movie_id, user_id=request.user.id)
        if not user_purchase:
            return Response(
                {"res": "Object does not exist or is not accessible"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        user_purchase.delete()
        return Response(
            {"res":"Object deleted"},
            status=status.HTTP_200_OK
        )


class MoviesListApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description':request.data.get('description'),
            'date_of_release':request.data.get('date_of_release'),
            'image_url':request.data.get('image_url'),
            'added_by':request.user.id

        }

        serializer = MoviesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserMovieDetail(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def validate_if_user_in_movie(self, movie_id, user_id):
        movie = Movie.objects.get(id=movie_id)
        if movie.added_by_id == user_id:
            return True
        return False


    def get_user_object(self, movie_id, user_id):
        if self.validate_if_user_in_movie(movie_id, user_id):
            try:
                return Movie.objects.get(id=movie_id, added_by_id=user_id)
            except Movie.DoesNotExist:
                return status.HTTP_400_BAD_REQUEST
        return None


    def get(self, request, movie_id, *args, **kwargs):
        movies_instance = self.get_user_object(movie_id, request.user.id)
        if not movies_instance:
            return Response(
                {"res":"Object with movie id does not exist or is not accessible"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MoviesSerializer(movies_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, movie_id, *args, **kwargs):
        movie_instance = self.get_user_object(movie_id, request.user.id)
        if not movie_instance:
            return Response(
                {"res":"Object with movie id does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'description':request.data.get('description'),
            'date_of_release':request.data.get('date_of_release'),
            'image_url':request.data.get('image_url'),
            'added_by':request.user.id

        }

        serializer = MoviesSerializer(instance=movie_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, movie_id, *args, **kwargs):
        movie_instance = self.get_user_object(movie_id, request.user.id)
        if not movie_instance:
            return Response(
                {"res": "Object with movie id does not exist"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        movie_instance.delete()
        return Response(
            {"res":"Object deleted"},
            status=status.HTTP_200_OK
        )