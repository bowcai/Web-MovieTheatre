from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='aboutus-index'),
    path('movies', include('movies.urls')),
]
