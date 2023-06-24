from django.shortcuts import render
from django.http.response import HttpResponse

def home_view(request):
    return render(request, 'my_app/maqueta1.html ')

def contact_view(request):
    return render(request, 'my_app/maqueta1.html ')

def about_view(request):
    return render(request, 'my_app/maqueta1.html ')

def projects_view(request):
    return render(request, 'my_app/maqueta1.html ')

def social_view(request):
    return render(request, 'my_app/maqueta1.html ')

