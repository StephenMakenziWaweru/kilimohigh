from dataclasses import field
from re import template
from django.shortcuts import render
from django.views.generic import (ListView, CreateView, UpdateView,
                                    DetailView, DeleteView)
from .models import Student
# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    template_name = 'student/create.html'
    fields = '__all__'
    success_url = '/'

class StudentListView(ListView):
    model = Student
    template_name = 'student/home.html'
    context_object_name = 'student_list'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/delete.html'
    success_url = '/'

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student/update.html'
    fields = '__all__'
    success_url = '/'
