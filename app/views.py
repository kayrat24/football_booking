from django.views.generic import ListView, DetailView, CreateView
from .models import Post, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render


def post_list(request):
    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query)| Q(body__icontains=search_query))

    else:
        posts = Post.objects.all()

    paginator = Paginator(posts,2)

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previus_url = '?page={}'.format(page.previous_page_number())
    else:
        previus_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'object':page[0:2],
        'is_paginated':is_paginated,
        'next_url': next_url,
        'previus_url':previus_url
    }

    return render(request,'index.html',context=context)
    
def field_list(request):
    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query)| Q(body__icontains=search_query))

    else:
        posts = Post.objects.all()

    paginator = Paginator(posts,2)

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previus_url = '?page={}'.format(page.previous_page_number())
    else:
        previus_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object':page,
        'is_paginated':is_paginated,
        'next_url': next_url,
        'previus_url':previus_url
    }

    return render(request,'field_list.html',context=context)
 


# class FieldsListView(ListView):
#     model = Post
#     template_name = 'home.html'

class FieldDetailView(DetailView): 
    model = Post
    template_name = 'about.html'

class FieldCreateView(CreateView): 
    model = Post
    template_name = 'field_new.html'
    fields = ['title', 'price', 'body', 'adress']