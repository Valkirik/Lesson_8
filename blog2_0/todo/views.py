from django.shortcuts import render
from django.views.generic import ListView
from .models import TodoListItem


class TaskListView(ListView):
    model = TodoListItem
    template_name = "main.html"