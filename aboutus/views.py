from django.shortcuts import render
from django.http import HttpResponse, HttpResponsePermanentRedirect


# Create your views here.
def index_redirect(request):
    return HttpResponsePermanentRedirect('/about-us/')


def index(request):
    return render(request, 'about-us.html')
