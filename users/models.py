from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="friend_suggestions", blank=True)
    bio = models.CharField(max_length=150, blank=True)
    date_of_birth = models.CharField(max_length=5, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(default="default_profile.jpg", upload_to="profiles_img", blank=True, null=True)

    def profile_posts(self):
        # Default related_name is original model's name in lowcase + _set
        # https://docs.djangoproject.com/en/4.1/topics/db/queries/#following-relationships-backward
        return self.user.post_set.all()

    def get_friends(self):
        return self.friends.all()

    def __str__(self):
        return f"{self.user.username} Profile"


STATUS_CHOICES = (
    ("send", "send"),
    ("accepted", "accepted"),
)


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friend_senders")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="friend_receivers")
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
