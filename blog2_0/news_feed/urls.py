from django.urls import path
from .endpoints import PageListApiView, PageCreateAPIView, \
    PageListCreateAPIView, PageUpdateAPIView, PageRetrivUpdateAPIView, \
    PageRetrivDestroyAPIView, PageRetrivUpdateDestroyAPIView

urlpatterns = [
    path("page-list/", PageListApiView.as_view()),
    path("page-create/", PageCreateAPIView.as_view()),
    path("page-list-create/", PageListCreateAPIView.as_view()),
    path("page-update/<int:pk>", PageUpdateAPIView.as_view()),
    path("page-detail-update/<int:pk>", PageRetrivUpdateAPIView.as_view()),
    path("page-delete-update/<int:pk>", PageRetrivDestroyAPIView.as_view()),
    path("page-retrieve-delete-update/<int:pk>", PageRetrivUpdateDestroyAPIView.as_view()),

]