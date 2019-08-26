# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
import uuid
from django.db.models import signals
from .tasks import send_verification_email


class UserManager(BaseUserManager):

    def create_user(self, email, full_name=None, password=None, is_active=True, is_staff=False, is_admin=False, is_verified=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user.set_password(password) # also to change password
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.verified = is_verified    
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True,
            is_verified=True
            
        )
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=False) #can login
    staff       = models.BooleanField(default=False) #staff user non superuser
    admin       = models.BooleanField(default=False) #superuser
    created_at  = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField('is_verified', default=False) # 'is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4) #verification code

    
    USERNAME_FIELD = 'email' #username
    # email and password are reqired by default
    REQUIRED_FIELDS = [] #['full_name']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, accounts):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
    
    @property
    def is_verified(self):
        return self.verified

def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)
 
signals.post_save.connect(user_post_save, sender=User)
