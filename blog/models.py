from django.db import models


# Model is the father of category.
class Category(models.Model):
    """
    CharField means string
    """
    name = models.CharField(max_length=100)


# the tag of articles.
class Tag(models.Model):
    name = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
