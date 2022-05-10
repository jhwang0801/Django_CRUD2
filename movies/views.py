import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie


class ActorsView(View):

    def get(self, request):
        
        results = [
            {
                'first_name' : actor.first_name,
                'last_name' : actor.last_name,
                'movie_list' : [{
                    'title': movie.title
                } for movie in actor.movie.all()]
            } for actor in Actor.objects.all()
        ]
        return JsonResponse({"results" : results}, status=200)


class MoviesView(View):

    def get(self, request):

        results = [
            {
                'title' : movie.title,
                'running_time' : movie.running_time,
                'actor_list' : [{
                    'actor': actor.first_name
                } for actor in movie.actor_set.all()]
            } for movie in Movie.objects.all()
        ]
        return JsonResponse({"results" : results}, status=200)