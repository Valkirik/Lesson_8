from django.urls import path
from .endpoints import PageListApiView, PageCreateAPIView, PageListCreateAPIView, PageUpdateAPIView



urlpatterns = [
    path("page-list/", PageListApiView.as_view()),
    path("page-create/", PageCreateAPIView.as_view()),
    path("page-list-create/", PageListCreateAPIView.as_view()),
    path("page-update/<int:pk>", PageUpdateAPIView.as_view())
]