from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class FieldsListView(ListView):
    model = Post
    template_name = 'home.html'

class FieldDetailView(DetailView): 
    model = Post
    template_name = 'field_detail.html'

class FieldCreateView(CreateView): 
    model = Post
    template_name = 'field_new.html'
    fields = ['title', 'price', 'body', 'adress']