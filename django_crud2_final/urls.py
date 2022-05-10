
from django.urls import path, include

urlpatterns = [
    path('', include('owners.urls')),

    path('', include('movies.urls')),

]
