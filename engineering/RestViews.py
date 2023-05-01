from rest_framework.views import Response
from rest_framework.views import APIView
from .serializers import *
from .models import Movie, Reviews, Category, Actor, Genre

class MoviesListView(APIView):
    def get(self, request):
        movies=Movie.objects.filter(draft=False)
        serializer=MovieListSerilizer(movies, many=True)
        return Response(serializer.data)
    
class MoviesDetailView(APIView):
    def get(self, request, pk):
        movie=Movie.objects.get(id=pk, draft=False)
        serializer=MovieDetailSerilizer(movie)
        return Response(serializer.data)
    def post(self, request):
        movie=MovieDetailSerilizer(data=request.data)
        if movie.is_valid():
            movie.save()
        return Response(status=201)
    def put(self, request, pk, format=None):
        instance = Movie.objects.get(pk=pk)
        serializer = MovieDetailSerilizer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)
    def delete(self, request, pk):
        my_instance = Movie.objects.get(pk=pk)
        my_instance.delete()
        return Response(status=204)

class ReviewView(APIView):
    def post(self, request):
        review=ReviewsCreateSerializer(data=request.data)
        if review.is_valid():
            review.save
        return Response(status=201)
     
    def get(self, request):
        review=Reviews.objects.all()
        serializer=ReviewsSerializer(review, many=True)
        return Response(serializer.data)
        
class ReviewUpdateView(APIView):   
    def put(self, request, pk, format=None):
        instance = Reviews.objects.get(pk=pk)
        serializer = ReviewsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=200)
    def delete(self, request, pk):
        my_instance = Reviews.objects.get(pk=pk)
        my_instance.delete()
        return Response(status=204)

class CategoryView(APIView):
        def post(self, request):
            category=CategorySerializer(data=request.data)
            if category.is_valid():
                category.save()
            return Response(status=201)
        
        def get(self, request):
            review=Category.objects.all()
            serializer=CategorySerializer(review, many=True)
            return Response(serializer.data)
class CategoryPutDelView(APIView):
        def put(self, request, pk, format=None):
            instance = Category.objects.get(pk=pk)
            serializer = CategorySerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=200)
        def delete(self, request, pk):
            my_instance = Category.objects.get(pk=pk)
            my_instance.delete()
            return Response(status=204)
        
class ActorView(APIView):
        def post(self, request):
            actor=ActorSerializer(data=request.data)
            if actor.is_valid():
                actor.save()
            return Response(status=201)
        
        def get(self, request):
            review=Actor.objects.all()
            serializer=ActorSerializer(review, many=True)
            return Response(serializer.data)
class ActorPutDelView(APIView):
        def put(self, request, pk, format=None):
            instance = Actor.objects.get(pk=pk)
            serializer = ActorSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=200)
        def delete(self, request, pk):
            my_instance = Actor.objects.get(pk=pk)
            my_instance.delete()
            return Response(status=204)
        
class GenreView(APIView):
    def post(self, request):
        genre=GenreSerializer(data=request.data)
        if genre.is_valid():
            genre.save()
        return Response(genre.data, status=201)
    
    def get(self, request):
        review=Genre.objects.all()
        serializer=GenreSerializer(review, many=True)
        return Response(serializer.data)

class GenrePutDelView(APIView):
        def put(self, request, pk, format=None):
            instance = Genre.objects.get(pk=pk)
            serializer = GenreSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(status=200)
        def delete(self, request, pk):
            my_instance = Genre.objects.get(pk=pk)
            my_instance.delete()
            return Response(status=204)
