from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(is_hidden=False).order_by('-date')


class ProjectView(generic.DetailView):
    model = Project
    template_name = 'projects/project.html'
