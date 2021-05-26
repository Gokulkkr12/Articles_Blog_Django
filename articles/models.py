# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    slug=models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # we will add thumbnail soon
    # adding the author soon
    def __str__(self):
        return self.title
    def snippet(self):
        return self.body[:50]+"..."
