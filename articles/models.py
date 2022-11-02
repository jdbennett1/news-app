from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def _str_(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail",kwargs={"pk":self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def _str_(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")