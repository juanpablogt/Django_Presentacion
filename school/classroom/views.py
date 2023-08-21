from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView
from classroom.models import teacher
from classroom.forms import ContactForm
from django.urls import reverse_lazy

def home_view(request):
    return render(request, 'classroom/home.html')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thanks')

    def form_valid(self, form):
        print(form.cleaned_data["name"])
        return super().form_valid(form)

class ThanksPage(TemplateView):
    template_name = 'classroom/thanks.html'

class TeacherCreateView(CreateView):
    model = teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:thanks')

    def form_valid(self, form):
        print(form.cleaned_data["first_name"])
        return super().form_valid(form)

class TeacherListView(ListView):
    model = teacher
    queryset = teacher.objects.all()
    context_object_name = 'teacher_list'
    template_name = 'classroom/teacher_list.html'

class TeacherDetailView(DetailView):
    model = teacher
    
 