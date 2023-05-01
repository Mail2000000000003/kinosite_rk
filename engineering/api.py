from django.forms import ValidationError
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'name': ['exact']
    }
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'year': ['exact', 'gt', 'lt', 'gte', 'lte'],
        'title': ['exact'],
        'category': ['exact'],
        'fees_in_usa':['exact', 'gt', 'lt', 'gte', 'lte'],
        'budget':['exact', 'gt', 'lt', 'gte', 'lte'],
    }
    ordering_fields = ['title', 'price']
    ordering = ['title']
    search_fields = ['title']

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'id': ['exact'],
        'name': ['exact'],
        'age':['exact', 'gt', 'lt', 'gte', 'lte'],
    }
    ordering_fields = ['name', 'age']
    ordering = ['name']
    search_fields = ['name']