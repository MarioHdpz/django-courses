""" Course views """
from django.views.generic import ListView

from .models import Course

class AllCourses(ListView):
    """ Render all courses """
    template_name = "courses_list.html"
    context_object_name = "courses"
    model = Course

class CourseByCategory(AllCourses):
    """ Render courses by category """
    def get_queryset(self):
        return Course.objects.filter(category__slug=self.kwargs['slug'])
