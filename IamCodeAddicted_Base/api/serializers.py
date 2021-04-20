from django.contrib.auth import authenticate
from rest_framework import serializers
from IamCodeAddicted_Base.models import Movie, MoviesPurchase, CustomUser
from IamCodeAddicted_Base.models import CustomUser
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import update_last_login

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MoviePurchaseSerializer(serializers.ModelSerializer):
    movies = MoviesSerializer(source='movie')
    class Meta:
        model = MoviesPurchase
        fields = '__all__'
        movies = None


class RegisterUserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only':True}}

        def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance
            


class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }