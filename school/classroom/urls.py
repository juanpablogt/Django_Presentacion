from django.urls import path
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('thanks/', views.thanksPage.as_view(), name='thanks'),
]
