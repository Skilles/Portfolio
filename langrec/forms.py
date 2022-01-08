from django import forms
from langrec.models import Language

import language_recommender.langrec

LANGUAGE_RECOMMENDER = language_recommender.langrec.LanguageRecommender()


class RecommendationForm(forms.Form):
    languages = forms.CharField(max_length=100, required=True)
    count = forms.IntegerField(min_value=1, max_value=5, required=True)

    def __init__(self, *args, **kwargs):
        super(RecommendationForm, self).__init__(*args, **kwargs)
        self.recommender = LANGUAGE_RECOMMENDER
        self.recommender.read_from_db(Language.objects.all())

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
