from django.shortcuts import render
from django.views.generic import (ListView, CreateView,
                                    DetailView)
from .models import Stream
# Create your views here.
class StreamCreateView(CreateView):
    model = Stream
    template_name = 'stream/streamcreate.html'
    fields = '__all__'
    success_url = '/'

class StreamListView(ListView):
    model = Stream
    template_name = 'stream/streamhome.html'
    context_object_name = 'stream_list'

class StreamDetailView(DetailView):
    model = Stream
    template_name = 'stream/streamdetail.html'
    context_object_name = 'stream'
