from django.http.response import HttpResponse
from . import views 

# Create your views here.
def home_view(request):
    return HttpResponse("<h1> 666 Juan Pablo </h1>")
