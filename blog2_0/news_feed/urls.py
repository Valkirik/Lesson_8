from django.urls import path
from .views import say_hello, get_pages_list, PostListView, \
    PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, \
    PageListView, PageCreateView, PageDeleteView, PageDetailView, PageUpdateView


urlpatterns = [
    path('index/', say_hello),
    path('pages/', get_pages_list),
    path('posts_list/', PostListView.as_view()),
    path('post_create/', PostCreateView.as_view()),
    path('post/<int:pk>', PostDetailView.as_view()),
    path('post_update/<int:pk>', PostUpdateView.as_view()),
    path('post_delete/<int:pk>', PostDeleteView.as_view()),
    path('pages_list/', PageListView.as_view()),
    path('pages_create/', PageCreateView.as_view()),
    path('pages_delete/<int:pk>', PageDeleteView.as_view()),
    path('pages_detail/<int:pk>', PageDetailView.as_view()),
    path('pages_update/<int:pk>', PageUpdateView.as_view()),

]