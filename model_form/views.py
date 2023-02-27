from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .forms import AuthorForm
from .models import Author, Book

# class AuthorCreateView(LoginRequiredMixin, CreateView):


def author_create(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data["name"]
            title = form.cleaned_data["title"]
            birth_date = form.cleaned_data["birth_date"]

            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("author-detail")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthorForm()

    return render(request, "author_form.html", {"form": form})


class AuthorDetailView(DetailView):
    model = Author
