from rest_framework import serializers
from IamCodeAddicted_Base.models import Movie, MoviesPurchase


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MoviePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesPurchase
        fields = '__all__'