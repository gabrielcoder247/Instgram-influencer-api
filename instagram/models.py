# from django.db import models

# Create your models here.


from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, List, Union
from django.conf import settings
from django.db import models
from pydantic import AnyUrl
# from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
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
    user: Any = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, null=True, on_delete=models.SET_DEFAULT, related_name="user")
    username: str = models.CharField(max_length=50, unique=True)
    description: str = models.TextField(null=True, blank=True)
    follower_count:int = models.PositiveIntegerField(default=0)
    created_on:datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects: PostManager = PostManager()
    # user = CustomUser()

    # class Meta:
    #     verbose_name: str = "post"
    #     verbose_name_plural: str = "posts"
    #     ordering: list = ["created_on",]

    def __repr__(self) -> str:
        return "<Post %r>" % self.title

    def __str__(self) -> str:
        return f"{self.title}"

    def save_data(self):
        self.save()


        # if request.user.is_authenticated:
        #     user.username = username
        #     user.description = description
        #     user.follower_count = follower_count
        #     user.created_on = created_on
        #     user.save()

    # def get_thumbnail_url(self) -> Union[Path, str, AnyUrl]:
    #     timestamp = "%s%s%s%s%s" % (datetime.now().year, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second)
    #     if self.thumbnail and hasattr(self.thumbnail, 'url'):
    #         return "%s?enc=%s" % (self.thumbnail.url, timestamp)

    @classmethod
    def search_users(cls, search_term):
        usernames = cls.objects.filter(username__icontains=search_term)
        return username


    @login_required(login_url='/accounts/login/')
    def search_results(request):

        #query all username to find search_term
        if 'username' in request.GET and request.GET["username"]:
            search_term =request.GET.get("username")
            search_user = self.search_users(search_term)
            message = f"{search_term}"

            return search_user

        else:

            message = "You haven't searched for any term"
            return render(request, 'search.html', {"message":message})