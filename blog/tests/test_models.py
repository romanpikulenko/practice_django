import pytest

from blog.models import Post


@pytest.mark.django_db
def test_title_create():
    article = Post.objects.create(title="article")
    assert article.title == "article"
