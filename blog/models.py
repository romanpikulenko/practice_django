from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Create a post"
        verbose_name_plural = "Create posts"

    title = models.CharField(max_length=200, db_index=True)
    content = RichTextField(max_length=4000, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_posts", blank=True)
    saved_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="saved_posts", blank=True)

    """
    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    """

    def total_likes_posts(self):
        return self.liked_users.count()

    def total_saves_posts(self):
        return self.saved_users.count()

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.title


# https://docs.djangoproject.com/en/4.1/topics/signals/
@receiver(pre_save, sender=Post)
def slug_populator(sender, instance, **kwargs):
    # unidecode is used to decode non-ANSI unicode symbols to their ANSI representations
    # as slugify works only with ANSI
    instance.slug = slugify(unidecode(instance.title))


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments_blog", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextField(max_length=4000)
    date_created = models.DateTimeField(auto_now_add=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked_comments_blog", blank=True)
    parent_comment = models.ForeignKey(
        "self", related_name="reply_comment_blog", null=True, blank=True, on_delete=models.CASCADE
    )

    def total_likes(self):
        return self.liked_users.count()

    def __str__(self):
        return f"{self.post.title} {self.author} {self.pk}"

    def get_absolute_url(self):
        # return reverse("post-detail", kwargs={"pk": self.pk})
        return reverse("post-detail", kwargs={"pk": self.post.pk})
