from rest_framework import serializers
from IamCodeAddicted_Base.models import Movie, MoviesPurchase


class MoviesSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class MoviePurchaseSerializer(serializers.ModelSerializer):
    date_of_purchase = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    class Meta:
        model = MoviesPurchase
        fields = '__all__'