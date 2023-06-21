from django.urls import path
from . import views


urlpatterns = [
    path('<topics>/', views.home_view, name='home'),
    path('<topics>/contact/', views.contact_view, name='contact'),
    path('<topics>/about/', views.about_view, name='about'),
    path('<topics>/social/', views.social_view, name='social'),
    path('<topics>/projects/', views.projects_view, name='projects')
]
