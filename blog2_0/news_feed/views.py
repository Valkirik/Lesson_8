from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Post, Page





#BESE VIEWS FOR PAGE(CBV)
"""class PageListView(ListView):
    model = Page
    template_name = "all_pages.html"


class PageCreateView(CreateView):
    model = Page
    fields = ["title", "description", "owner"]
    template_name = "page_create.html"
    success_url = "all_pages.html"


class PageDeleteView(DeleteView):
    model = Page
    template_name = "page_delete.html"
    success_url = "/"


class PageUpdateView(UpdateView):
    model = Page
    template_name = "page_update.html"
    fields = ["title", "description"]
    success_url = "/"


class PageDetailView(DetailView):
    model = Page
    template_name = "page_detail.html"
    success_url = "/"




#BESE VIEWS FOR POST (CBV)
class PostListView(ListView):
    model = Post
    template_name = "all_posts.html"


class PostCreateView(CreateView):
    model = Post
    fields = ["name", "content", "page"]
    template_name = "post_create.html"
    success_url = "/admin"

#to get one certain object
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["name", "content"]
    success_url = "/admin"

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/admin""""


