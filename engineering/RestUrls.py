from django.urls import path
from . import RestViews

urlpatterns = [
    path("movie/", RestViews.MoviesListView.as_view()),
    path("movie/<int:pk>/", RestViews.MoviesDetailView.as_view()),
    path("review/", RestViews.ReviewView.as_view()),
    path("review/<int:pk>", RestViews.ReviewUpdateView.as_view()),
    path("category/", RestViews.CategoryView.as_view()),
    path("category/<int:pk>", RestViews.CategoryPutDelView.as_view()),
    path("actor/", RestViews.ActorView.as_view()),
    path("actor/<int:pk>", RestViews.ActorPutDelView.as_view()),
    path("genre/", RestViews.GenreView.as_view()),
    path("genre/<int:pk>", RestViews.GenrePutDelView.as_view()),
]