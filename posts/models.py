# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from accounts.models import User

# Create your models here.

class Posts(models.Model):
	author = models.ForeignKey(User, default=1)
	post_title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.post_title

	class Meta:
		verbose_name_plural = "Posts"