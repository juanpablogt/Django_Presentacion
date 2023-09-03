from django.urls import path
from . import views
app_name = 'classroom'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('teacher/', views.TeacherCreateView.as_view(), name='create_teacher'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('teacher_list/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teacher_detail/<int:pk>', views.TeacherDetailView.as_view(), name='detail_teacher'),
    path('update_teacher/<int:pk>', views.TeacherUpdateView.as_view(), name='update_teacher'),
    path('delete_teacher/<int:pk>', views.TeacherDeleteView.as_view(), name='delete_teacher'),
]
