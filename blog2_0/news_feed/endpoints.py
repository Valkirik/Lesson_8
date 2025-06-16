from itertools import chain

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Page, Post
from .serializers import PageSerializer, PostSerializer, PostPageSerializer



class PageListApiView(ListAPIView):
    queryset = Page.objects.all() #getting objects
    serializer_class = PageSerializer #turn them into json(XML)


class PageCreateAPIView(CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageListCreateAPIView(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageUpdateAPIView(UpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PageRetrivUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrivDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageRetrivUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class PagePostListApiView(ListAPIView):
    post = Post.objects.all()
    page = Page.objects.all()
    queryset = chain(post, page)
    serializer_class = PostPageSerializer