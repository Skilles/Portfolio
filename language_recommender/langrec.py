import language_recommender.codes as codes
import json
from collections import defaultdict


class Language:
    def __init__(self, code, name, data):
        self.code = code
        self.name = name
        self.data = data
        self.major = False

    def __str__(self):
        return self.name, self.code

    def __repr__(self):
        return str((self.name, self.code))


class LanguageRecommender:
    LANG_COUNT = 202
    RECOMMENDATIONS_COUNT = 5

    def __init__(self):
        self.data = {}
        self.languages = []

    def read_data(self):
        for i, language in enumerate(codes.known_codes):
            try:
                with open('data/simtri-' + language + '.txt', 'r') as f:
                    for line in f.readlines():
                        lang_data = line.split(' ')
                        if language not in self.data:
                            self.data[language] = []
                        self.data[language].append((lang_data[0], float(lang_data[1].strip())))
                    try:
                        self.languages.append(Language(language, codes.languages[language],
                                                       self.data[language]))
                    except KeyError:
                        pass
            except FileNotFoundError:
                print('File not found: ' + language)

    def dump_to_json(self, path):
        with open(path, 'w') as f:
            f.write('')
            index = 0
            output = []
            for language in self.languages:
                index += 1
                code = language.code
                name = language.name
                output.append({"model": "langrec.language", "pk": index, "fields": {
                    "name": name,
                    "code": code,
                }})
            json.dump(output, f)

    def get_recommendations(self, *lang_code):
        recommendations = []
        data_dict = defaultdict(float)
        for code in lang_code:
            lang_data = self.data[code]
            for i in range(1, len(lang_data)):
                code = lang_data[i][0]
                value = lang_data[i][1]
                data_dict[code] += value

        sorted_data_dict = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(self.RECOMMENDATIONS_COUNT):
            code = sorted_data_dict[i][0]
            name = codes.languages[code]
            recommendations.append(name)
        return recommendations

    def reverse_lookup(self, name):
        for language in self.languages:
            if language.name == name:
                return language.code


if __name__ == '__main__':
    lr = LanguageRecommender()
    lr.read_data()
    # lr.dump_to_json('languages_dump.json')
    for language in lr.languages:
        print(f"'{language.name}',")
