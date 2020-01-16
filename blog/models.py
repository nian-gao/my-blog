from django.db import models
from django.contrib.auth.models import User


# Model is the father of category.
class Category(models.Model):
    """
    CharField means string
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# the tag of articles.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
