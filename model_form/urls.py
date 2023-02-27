from django.urls import path

from model_form import views

urlpatterns = [
    # path('author/create/', AuthorCreateView.as_view(), name='author-create'),
    path("author/create", views.author_create, name="author-create"),
    path("author/<int:pk>/detail/", views.AuthorDetailView.as_view(), name="author-detail"),
]
