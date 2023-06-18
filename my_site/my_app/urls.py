from django.urls import path
from .views import home_view, contact_view, about_view, social_view, projects_view, error_view

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('social/', social_view, name='social'),
    path('projects/', projects_view, name='projects'),
    path('error/', error_view, name='error')
]
