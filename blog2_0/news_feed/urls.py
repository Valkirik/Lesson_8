from django.urls import path, include
from .endpoints import PageListApiView, PageCreateAPIView, \
    PageListCreateAPIView, PageUpdateAPIView, PageRetrivUpdateAPIView, \
    PageRetrivDestroyAPIView, PageRetrivUpdateDestroyAPIView, PagePostListApiView, PageViewSet, PostViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register("page_viewset", PageViewSet)
router.register("post_viewset", PostViewSet)


urlpatterns = [
    #with generics
    path("page-list/", PageListApiView.as_view()),
    path("page-create/", PageCreateAPIView.as_view()),
    path("page-list-create/", PageListCreateAPIView.as_view()),
    path("page-update/<int:pk>", PageUpdateAPIView.as_view()),
    path("page-detail-update/<int:pk>", PageRetrivUpdateAPIView.as_view()),
    path("page-delete-update/<int:pk>", PageRetrivDestroyAPIView.as_view()),
    path("page-retrieve-delete-update/<int:pk>", PageRetrivUpdateDestroyAPIView.as_view()),
    path("page-post-list/", PagePostListApiView.as_view()),

    #with viewsets
    path("", include(router.urls))

]