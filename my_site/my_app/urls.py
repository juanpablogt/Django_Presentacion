from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),
    path('social/', views.social_view, name='social'),
    path('projects/', views.projects_view, name='projects'),

]
