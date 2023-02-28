from django import forms
from django.forms import fields, widgets

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control custom-text", "cols": "40", "rows": "4"}), label=""
    )

    class Meta:
        model = Comment
        fields = [
            "content",
        ]
