import json

from django import forms
from django.http import HttpResponse

from langrec.models import Language

from langrec.core.langrec import LanguageRecommender

LANGUAGE_RECOMMENDER = LanguageRecommender()


class RecommendationForm(forms.Form):
    languages = forms.CharField(max_length=100, required=True)
    count = forms.IntegerField(min_value=1, max_value=5, required=True)

    def __init__(self, *args, **kwargs):
        super(RecommendationForm, self).__init__(*args, **kwargs)
        self.recommender = LANGUAGE_RECOMMENDER

    def clean_data(self):
        languages = self.cleaned_data['languages']
        count = self.cleaned_data['count']
        if len(languages) == 0:
            raise forms.ValidationError('Language(s) cannot be empty ' + str(self.cleaned_data))
        return count, languages

    def get_recommendations(self, count, languages):
        codes = self.recommender.reverse_lookup(*languages.split(','))
        recommendations = self.recommender.get_recommendations(count, *codes)
        return recommendations

    def get_response(self):
        self.cleaned_data = self.clean_data()
        recommendations = self.get_recommendations(*self.cleaned_data)
        data = []
        for r in recommendations:
            data.append(r[0].to_json(r[1]))
        return HttpResponse(json.dumps(data, indent=4), content_type='text/json')

    async def cache(self):
        await self.recommender.read_from_db(Language.objects.all())
