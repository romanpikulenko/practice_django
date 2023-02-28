from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from .models import Post


def index(request):
    context = {"posts": Post.objects.all()}

    return render(request, "blog/index.html", context)


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
            user = get_object_or_404(get_user_model(), username=self.kwargs.get("username"))
            query = query.filter(author=user)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context


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


# https://docs.djangoproject.com/en/4.1/topics/auth/default/
# LoginRequiredMixin
# When using class-based views, you can achieve the same behavior as with login_required by using the LoginRequiredMixin.
# This mixin should be at the leftmost position in the inheritance list.
# UserPassesTestMixin
# When using class-based views, you can use the UserPassesTestMixin to do this.


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = "blog/post_delete.html"

    def test_func(self):

        post: Post = self.get_object()  # type: ignore

        return self.request.user == post.author
