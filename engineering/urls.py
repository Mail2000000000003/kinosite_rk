from django.urls import path
from . import views
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


    path("", views.MoviesView.as_view(), name="home"),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
     path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]
