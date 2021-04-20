from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from IamCodeAddicted_Base.models import Movie, MoviesPurchase, CustomUser
from .serializers import MoviesSerializer, MoviePurchaseSerializer, RegisterUserSerializer, UserLoginSerializer
from datetime import  datetime
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import logging

logger = logging.getLogger(__name__)


class MoviesPurchaseApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def get(self, request,*args, **kwargs):
        try:
            user_purchase = MoviesPurchase.objects.filter(user_id=request.user.id)
            logger.debug(f'Database query result: [{user_purchase}]')
        except Exception as err:
            logger.error(f"Domething went wrong: [{err}]")
        if not user_purchase:
            return Response(
                {"res":"Object does not exist or is not accessible"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MoviePurchaseSerializer(user_purchase, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, *args, **kwargs):
        permissions_classes = [permissions.IsAuthenticated]
        data = {
            'date_of_purchase':request.data.get('date_of_purchase'),
            'movie':request.data.get('movie'),
            'user':request.user.id
        }
        try:
            movies = Movie.objects.get(id=data['movie'])
            logger.debug(f'Database query result: [{movies}]')
        except Exception as err:
            logger.error(f"Domething went wrong: [{err}]")
        data['movies'] = movies.__dict__
        logger.debug(f'Data: [{data}]')
        serializer = MoviePurchaseSerializer(data=data)
        logger.debug(f'Serializer: [{serializer}]; IS_VALID: [{serializer.is_valid()}]')
        if serializer.is_valid():
            logger.debug(f'DATA_VALIDATED: [{serializer.validated_data}]')
            if serializer.validated_data:
                serializer.save()
                return Response(serializer.errors, status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

class MoviePurchaseUserApi(APIView):
    permissions_classes = [permissions.IsAuthenticated]


    def get(self, request, movie_id, *args, **kwargs):
        try:
            user_purchase = MoviesPurchase.objects.get(movie_id=movie_id, user_id=request.user.id)
            logger.debug(f'Database query result: [{user_purchase}]')
        except Exception as err:
            logger.error(f"Domething went wrong: [{err}]")
        if not user_purchase:
            return Response(
                {"res":"Object does not exist or is not accessible"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = MoviePurchaseSerializer(user_purchase)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
            'price':request.data.get('price'),
            'rating':request.data.get('rating'),
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


# auth section!!!
class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        data = {}
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                data['response'] = "Successfully registered a new user"
                data['email'] = newuser.email
                data['username'] = newuser.username
                return Response(status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
