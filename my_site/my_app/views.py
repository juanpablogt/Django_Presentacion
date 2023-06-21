from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseNotFound



articles = {
    "home": " 666 Juan Pablo",
    "contact": "Contact Page",
    "about": "About Page",
    "social": "Social Page",
    "projects": "Projects Page",
    "error": "Error Page" 
}

# Create your views here.
def home_view(request,topics):
    try:
        result = articles[topics]
        return HttpResponse(articles[topics])
    except:
       raise Http404("no existe la pagina")

def contact_view(request,topics):
    try:
        result = articles[topics]
        return HttpResponse(articles[topics])
    except:
       raise Http404("no existe la pagina")
    
def about_view(request,topics):
    try:
        result = articles[topics]
        return HttpResponse(articles[topics])
    except:
       raise Http404("no existe la pagina")

def social_view(request,topics):

    try:
        result = articles[topics]
        return HttpResponse(articles[topics])
    except:
       raise Http404("no existe la pagina")
    
def projects_view(request,topics):

    try:
        result = articles[topics]
        return HttpResponse(articles[topics])
    except:
       raise Http404("no existe la pagina")

