from rest_framework import serializers
from .models import Movie, Reviews, Category, Actor, Genre

class MovieListSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=("title", "tagline", "category")

class MovieDetailSerilizer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    directors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    
    class Meta:
        model=Movie
        exclude=("draft",)

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields=("email", "name", "text", "movie")

class ReviewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reviews
        fields="__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=("name", "url")

class ActorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields=("name", "age", "image")

class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields=("name", "description", "url")