""" Blog serializers for API """
from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    """ Courses data serializer """

    class Meta():
        model = Course
        fields = "__all__"
