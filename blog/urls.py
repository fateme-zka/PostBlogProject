from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home-blog'),

    path('<str:username>/posts/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    path('about/', about, name='about-blog'),

]
