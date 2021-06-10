
from django.urls import path
from blogapp import views

urlpatterns = [
    
    path('index/' , views.IndexPageView.as_view()),
    path('' , views.PostListView.as_view() , name = 'blog-posts'),
    path('userpost/<username>/' , views.UserPostListView.as_view() , name = 'user-posts'),
    path('post/<int:pk>/' , views.PostDetailView.as_view() , name = 'post-detail'),
    path('create/' , views.PostCreateView.as_view() , name = 'post-create'),
    path('update/<int:pk>/' , views.PostUpdateView.as_view() , name = 'post-update'),
    path('delete/<int:pk>/' , views.PostDeleteView.as_view() , name = 'post-delete'),
]
