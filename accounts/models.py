# from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager


class CustomUser(AbstractUser):
		first_name = None
		last_name = None
		password2 = None
		name = models.CharField(max_length=50, unique=True)
		email = models.EmailField(max_length=55, unique=True)

		objects = UserManager()

		USERNAME_FIELD = 'email'
		REQUIRED_FIELDS = ['name']

		def __str__(self):
			return self.email

