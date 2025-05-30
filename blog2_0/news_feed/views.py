from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello")
