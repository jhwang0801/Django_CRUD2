from django.urls import path
from movies.views import ActorsView, MoviesView

urlpatterns = [
    path('actors', ActorsView.as_view()),
    path('movies', MoviesView.as_view()),
]