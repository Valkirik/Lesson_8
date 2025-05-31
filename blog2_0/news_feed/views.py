from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from .models import Page, Post

def say_hello(request):
    return HttpResponse("Hello")


def get_pages_list(request):
    context = {}
    context["all_pages"] = Page.objects.all()
    return render(request, "all_pages.html", context)



class PostListView(ListView):
    model = Post
    template_name = "all_posts.html"



class PostCreateView(CreateView):
    model = Post
    fields = ["name", "content", "page"]
    template_name = "post_create.html"
    success_url = "/admin"

