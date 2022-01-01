from django.views import generic

from .models import Project


class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.order_by('-date')[:5]


class DetailView(generic.DetailView):
    model = Project
    template_name = 'projects/project.html'
