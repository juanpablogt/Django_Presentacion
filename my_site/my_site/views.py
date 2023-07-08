from django.http.response import HttpResponse
from . import views
from django.urls import path
from django.urls.conf import include
from django.shortcuts import render


# Create your views here.
def home_view(request):
    return HttpResponse("<h1> 666 Juan Pablo </h1>")

def my_custom_page_error_view(request, exception):
    return render(request, 'Error.html', status=404)
