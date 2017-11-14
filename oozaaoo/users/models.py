# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from oozaaoo.constant import USER_TYPE


# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(verbose_name = "User type", max_length = 50, choices = USER_TYPE, blank = False, null = False)

    def __str__(self):
        return self.user.username
