""" Add courses models to admin """
from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin

from courses.models import Course, Category, Module

TokenAdmin.raw_id_fields = ['user']
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Module)
