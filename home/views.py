from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'home/index.html'
    context_object_name = 'home'


class ResumeView(generic.TemplateView):
    template_name = 'home/resume.html'
    context_object_name = 'resume'
