""" Add courses models to admin """
from django.contrib import admin

from courses.models import Course, Category, Module

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Module)
