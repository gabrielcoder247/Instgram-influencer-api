from datetime import date, datetime
from typing import Any, Generic, List, Optional, Type, Union
from accounts.schemas import UserOut
from pydantic import BaseModel, validator
from blog.models import Category

	def confirm_title(value: str) -> str:
		"""
		Validation to prevent empty title field.
		Called by the helper function below;
		"""
		if not value:
			raise ValueError("Please provide a title.")
		return value

	def confirm_slug(value: str) -> str:
		"""
		Validation to prevent empty slug field.
		Called by the helper function below;
		"""
		if not value:
			raise ValueError("Slug cannot be empty.")
		return value

	class PostBase(BaseModel):
		"""Base fields for blog posts."""

		user: UserOut
		title: str

		# Validation for title and slug
		_check_title = validator("title", allow_reuse=True)(confirm_title)

	class CreatePost(PostBase):
		"""
		Fields for creating a blog post.
		"""
	...

	class UpdatePost(PostBase):
		"""
		Fields for updating blog posts.
		"""
		view_count: int
		active: bool

	class SinglePost(PostBase):
		"""
		Response for a blog post.
		"""

		id: int
		slug: str
		view_count: int
		draft: bool = False
		publish: date
		description: Optional[str] = None
		content: Optional[str] = ...
		read_time: int
		category: CategoryOut

		class Config:
			orm_mode = True

	class AllPostList(PostBase):\
		"""
		Response for listing all blog posts.
		Custom for just these few fields
		"""
		id: int
		slug: str
		draft: bool = False
		category: CategoryListOut

		class Config:
			orm_mode = True

	class PostByCategoryList(PostBase):
		"""
		Response for all blog posts listing.
		Custom for just these few fields.
		"""
		id: int
		slug: str
		draft: bool = False
		class Config:
			orm_mode = True
Create pydantic schema validation.
