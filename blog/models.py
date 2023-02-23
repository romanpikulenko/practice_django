from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50)
    liked_users = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    saved_users = models.ManyToManyField(User, related_name="saved_posts", blank=True)

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


@receiver(pre_save, sender=Post)
def slug_populator(sender, instance, **kwargs):
    instance.slug = slugify(unidecode(instance.title))
