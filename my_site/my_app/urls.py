from django.urls import path
from . import views


urlpatterns = [
    path("<topic>/", views.home_view, name="home"),
    path("<topic>/", views.contact_view, name="contact"),
    path("<topic>/", views.about_view, name="about"),
    path("<topic>/", views.social_view, name="social"),
    path("<topic>/", views.projects_view], name="projects")   
]

