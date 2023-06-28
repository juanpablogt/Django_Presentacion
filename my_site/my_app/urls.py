from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.simple_view, name='home'),
    path('contact/', views.contact_view, name='contact')
]

