from django.urls import path, include
from rest_framework import routers

from movies.views import movie_list_view, MovieListView, MovieViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    # path('', movie_list_view, name="movie_list"),
    # path('', MovieListView.as_view(), name='movie_list')
    path("", include(router.urls))
]

app_name = "movie"
