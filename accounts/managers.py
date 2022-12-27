    from core.utils import get_username
	from django.contrib.auth.models import BaseUserManager
	from django.core.exceptions import ValidationError
	from django.db import models
	from django.utils.translation import gettext_lazy as _


	class UserQuerySet(models.QuerySet):
		pass


	class UserManager(BaseUserManager):
		use_in_migrations = True

		def get_queryset(self):
			return UserQuerySet(self.model, using=self._db)

		def _create_user(self, username, email, password, **extra_fields):
			"""
			Create and save a user with the given username, email, and password.
			"""
			if not email and username:
				raise ValueError(_("Users must have an email address and username"))

			# fullname = name.split()
			# if len(fullname) <= 1:
			# 	raise ValidationError(
			# 		_('Kindly enter more than one name.'),
			# 		code='invalid',
			# 		params={'value': self},
			# 	)
			# for x in fullname:
			# 	if len(x) < 2:
			# 		raise ValidationError(
			# 			_('Kindly give us your full name.'),
			# 			code='invalid',
			# 			params={'value': self},
			# 		)
			email = self.normalize_email(email)
			# name = ' '.join(map(str, fullname))
			user = self.model(username=username, email=email, **extra_fields)
			user.set_password(password)
			user.save(using=self._db)
			return user

		def create_user(self, name, email=None, password=None, **extra_fields):
			extra_fields.setdefault('is_staff', False)
			extra_fields.setdefault('is_superuser', False)
			return self._create_user(username, email, password, **extra_fields)

		# def create_staff(self, username, email, password, **extra_fields):
		# 	extra_fields.setdefault('is_staff', True)
		# 	extra_fields.setdefault('is_superuser', False)

		# 	if extra_fields.get('is_staff') is not True:
		# 		raise ValueError('Staff must have is_staff=True.')

		# 	return self._create_user(name, email, password, **extra_fields)

		def create_superuser(self, username, email, password, **extra_fields):
			extra_fields.setdefault('is_staff', True)
			extra_fields.setdefault('is_superuser', True)

			if extra_fields.get('is_staff') is not True:
				raise ValueError('Admin must have is_staff=True.')
			if extra_fields.get('is_superuser') is not True:
				raise ValueError('Admin must have is_superuser=True.')

			return self._create_user(username, email, password, **extra_fields)

		def get_username(self):
			return self.username

		# def get_short_name(self):
		# 	return get_first_name(self.name)

		# def get_first_name(self):
		# 	return get_first_name(self.name)

		# def get_last_name(self):
		# 	return get_last_name(self.name)