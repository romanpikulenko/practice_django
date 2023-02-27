from django.urls import path

from blog.views import PostCreateView, PostDetailView, UserPostListView, index

urlpatterns = [
    path("", index, name="blog-home"),
    path("posts/user/", UserPostListView.as_view(), name="all-user-posts"),
    path("posts/user/<str:username>/", UserPostListView.as_view(), name="user-posts"),
    path("posts/new/", PostCreateView.as_view(), name="new-post"),
    path("posts/<int:pk>/detail/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<slug:slug>/detail/", PostDetailView.as_view(), name="post-detail"),
]
