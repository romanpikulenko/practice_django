from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Post


# Create your views here.
# Realisation with get_queryset
class UserPostListView(ListView):
    # Model
    model = Post

    # Template name
    template_name = "blog/user_posts.html"

    # Context variable name with all data which is sent to the template
    context_object_name = "blog_post_user_list"

    def get_queryset(self) -> QuerySet[Any]:
        username = self.kwargs.get("username")
        query = Post.objects.order_by("-date_created")

        if username:
            user = get_object_or_404(User, username=self.kwargs.get("username"))
            query = query.filter(author=user)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context


"""
# Realisation with get_context_data
class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"

    # This is necessary as get_context_data uses default get_queryset which fetches all records from the table
    def get_queryset(self) -> QuerySet[Any]:
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        query = Post.objects.filter(author=user).order_by("-date_created")
        context["username"] = self.kwargs.get("username")
        context["blog_post_user_list"] = query
        return context
"""


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "title",
        "content",
    ]

    # success_url = reverse_lazy("all-user-posts")

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "blog_post_detail"
