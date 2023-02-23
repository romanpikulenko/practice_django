from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.discussion_create, name="new-discussion"),
    path("<int:pk>/detail/", views.PostDiscussionView.as_view(), name="discussion-detail"),
]
