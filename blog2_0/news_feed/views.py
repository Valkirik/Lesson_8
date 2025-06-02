from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Page, Post

def say_hello(request):
    return HttpResponse("Hello")


def get_pages_list(request):
    context = {}
    context["all_pages"] = Page.objects.all()
    return render(request, "all_pages.html", context)

class PageCreateView(CreateView):
    model = Page
    fields = ["title", "description", "owner"]
    template_name = ""


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
    success_url = "/admin"


