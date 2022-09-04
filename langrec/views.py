import json

from django.http import HttpResponse
from django.views import generic

from langrec.forms import RecommendationForm
# Create your views here.
from langrec.models import Language


class ListView(generic.ListView):
    template_name = 'langrec/list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        return Language.objects.order_by('name')

    async def get(self, request, *args, **kwargs):
        if request.GET.get('json', 'false') == 'true':
            return HttpResponse(await self.get_language_names_json(), content_type='text/json')

        return super().get(request, *args, **kwargs)

    @staticmethod
    async def get_language_names_json():
        names = [lang.name async for lang in Language.objects.all()]
        return json.dumps(names)


class IndexView(generic.FormView):
    template_name = 'langrec/index.html'
    form_class = RecommendationForm
    success_url = '/'


async def recommend(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        await form.cache()
        if form.is_valid():
            return form.get_response()
        else:
            return HttpResponse('Invalid form', status=400)
    return HttpResponse('Invalid request', status=400)

