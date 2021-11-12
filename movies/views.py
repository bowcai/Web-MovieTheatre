from django.shortcuts import render
from .models import Movie


# Create your views here.
def index(request):
    movies_all = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies_all': movies_all})
