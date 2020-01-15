""" Blog models """
from django.db import models

class Category(models.Model):
    """ Category model to classify courses """
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=60)

    def __str__(self):
        return self.name

class Module(models.Model):
    """ Modules of each course """
    name = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    sort_order = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    """ Course model """
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    modules = models.ManyToManyField(Module)
    slug = models.SlugField(max_length=60, blank=True)
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
