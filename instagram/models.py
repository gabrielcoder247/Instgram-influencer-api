# from django.db import models

# Create your models here.


from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, List, Union
from django.conf import settings
from django.db import models
from pydantic import AnyUrl
from accounts.models import CustomUser
from instagram.managers import CategoryManager, PostManager

# def upload_image_path(instance: Any, filename: str) -> Union[str, Callable, Path]:
#     """
#     Set up the default thumbnail upload path.
#     """
#     ext = filename.split('.')[-1]
#     filename = "%s.%s" %(instance.slug, ext)
#     return "blog_post_thumbnails/%s/%s" %(instance.slug, filename)


class Post(models.Model):
    """
    Model for Blog Posts.
    """
    user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_DEFAULT, related_name="posts")
    username = models.CharField(max_length=50, unique=True)
    description: str = models.TextField(null=True, blank=True)
    follower_count:int = models.PositiveIntegerField(default=0)
    created_on: datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects: PostManager = PostManager()

    class Meta:
        verbose_name: str = "post"
        verbose_name_plural: str = "posts"
        ordering: list = ["-publish", "title"]

    def __repr__(self) -> str:
        return "<Post %r>" % self.title

    def __str__(self) -> str:
        return f"{self.title}"

    def get_thumbnail_url(self) -> Union[Path, str, AnyUrl]:
        timestamp = "%s%s%s%s%s" % (datetime.now().year, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second)
        if self.thumbnail and hasattr(self.thumbnail, 'url'):
            return "%s?enc=%s" % (self.thumbnail.url, timestamp)
