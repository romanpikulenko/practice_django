from typing import Any

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import DiscussionCreateForm
from .models import Discussion


@login_required
def discussion_create(request):
    if request.method == "POST":
        form = DiscussionCreateForm(request.POST, request.FILES)

        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.author = request.user
            discussion.save()

            # in case of a model redirect uses model.get_absolute_url()
            messages.success(request, "Discussion was successfully added")

            return redirect(discussion)
        else:
            for error in form.errors.values():
                messages.error(request, error)

    else:
        form = DiscussionCreateForm()

    return render(
        request,
        "discussions/discussion_create.html",
        {
            "form": form,
        },
    )


class UserDiscussionListView(ListView):
    # Model
    model = Discussion

    # Template name
    template_name = "discussions/user_discussions.html"

    # Context variable name with all data which is sent to the template
    context_object_name = "blog_discussion_user_list"

    def get_queryset(self) -> QuerySet[Any]:
        username = self.kwargs.get("username")
        query = Discussion.objects.order_by("-date_created")

        if username:
            user = get_object_or_404(User, username=self.kwargs.get("username"))
            query = query.filter(author=user)

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["username"] = self.kwargs.get("username")
        return context


class PostDiscussionView(DetailView):
    model = Discussion
    context_object_name = "blog_discussion_detail"
