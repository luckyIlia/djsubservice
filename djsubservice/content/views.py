from django.views import generic
from .models import Course


class CourseListView(generic.ListView):
    template_name = "content/course_list.html"
    queryset = Course.objects.all()
