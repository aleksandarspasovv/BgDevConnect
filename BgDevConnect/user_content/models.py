from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="programist_profile")
    bio = models.TextField(max_length=500, blank=True)
    github_profile = models.URLField(max_length=200, blank=True)
    programming_languages = models.CharField(max_length=100, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="programist_posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="programist_likes", blank=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="programist_comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
