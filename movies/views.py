from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


# Create your views here.
def index(request):
    movies_all = Movie.objects.all()
    return render(request, 'movies.html', {'movies_all': movies_all})
