import json
import logging

from django.http import HttpResponse
from django.views import generic

from langrec.forms import RecommendationForm
# Create your views here.
from langrec.models import Language

logger = logging.getLogger('django')


class ListView(generic.ListView):
    template_name = 'langrec/list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        return Language.objects.order_by('name')


class IndexView(generic.FormView):
    template_name = 'langrec/index.html'
    form_class = RecommendationForm
    success_url = '/'

    def form_valid(self, form):
        logger.info('form_valid called')
        return super().form_valid(form)


def recommend(request):
    if request.method == 'GET':
        form = RecommendationForm(request.GET)
        # logger.log(logging.INFO, form.cleaned_data)
        if form.is_valid():
            logger.log(logging.INFO, 'form valid')
            form.cleaned_data = form.clean_data()
            recommendations = form.get_recommendations(*form.cleaned_data)
            data = []
            for r in recommendations:
                data.append(r[0].to_json(r[1]))
            return HttpResponse(json.dumps(data, indent=4), content_type='text/json')
        else:
            logger.log(logging.INFO, 'form invalid')
    else:
        print('not a get')
        form = RecommendationForm()
    return HttpResponse()
