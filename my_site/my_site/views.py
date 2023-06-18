from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.response import HttpResponseNotFound
from django.http.response import HttpResponseServerError 
from django.http.response import Http404    




articles = {
    "home": "I'm Juan Pablo GT ",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",

}
def home_view(request):
    
    return HttpResponse(articles["home"])

def contact_view(request):
    return HttpResponse(articles["contact"])

def about_view(request):
    return HttpResponse(articles["about"])

def social_view(request):
    return HttpResponse(articles["social"])

def projects_view(request):
    return HttpResponse(articles["projects"])

