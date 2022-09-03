import json
from collections import defaultdict
from langrec.core import codes


class Language:
    def __init__(self, code, name, data):
        self.code = code
        self.name = name
        self.data = data
        self.major = False

    def __str__(self):
        return str((self.name, self.code))

    def __repr__(self):
        return str((self.name, self.code))

    def to_json(self, value):
        return {
            "name": self.name,
            "code": self.code,
            "value": value,
            "major": self.major
        }


class LanguageRecommender:
    LANG_COUNT = 258

    def __init__(self):
        self.data_read = False
        self.data = {}
        self.languages = {}

    def read_data(self):
        if self.data_read:
            return
        for i, language in enumerate(codes.known_codes):
            try:
                with open('data/simtri-' + language + '.txt', 'r') as f:
                    for line in f.readlines():
                        lang_data = line.split(' ')
                        if lang_data[0] == language:
                            continue
                        if language not in self.data:
                            self.data[language] = {}
                        self.data[language][lang_data[0]] = float(lang_data[1].strip())
                    try:
                        self.languages[language] = Language(language, codes.languages[language],
                                                            self.data[language])
                    except KeyError:
                        pass
            except FileNotFoundError:
                print('File not found: ' + language)
        self.data_read = True

    def read_from_db(self, objects):
        if self.data_read:
            return
        for language in objects:
            self.languages[language.code] = Language(language.code, language.name, language.data)
        self.data_read = True

    def dump_to_json(self, path):
        with open(path, 'w') as f:
            f.write('')
            index = 0
            output = []
            for language in self.languages:
                index += 1
                output.append({
                    "model": "langrec.language",
                    "pk": index,
                    "fields": {
                        "name": language.name,
                        "code": language.code,
                        "data": language.data,
                        "major": language.major
                    }})
            json.dump(output, f)

    def get_recommendations(self, max_count=5, *lang_code, major=False):
        recommendations = []
        data_dict = defaultdict(float)
        avg_count = defaultdict(int)
        for code in lang_code:
            lang_data = self.languages[code].data
            for dcode, value in lang_data.items():
                if dcode != code and dcode in codes.known_codes and dcode not in lang_code and (
                        not major or (major and self.languages[dcode].major)):
                    # Keep a running average
                    data_dict[dcode] = (data_dict[dcode] * avg_count[dcode] + value) / (avg_count[dcode] + 1)
                    avg_count[dcode] += 1
        sorted_data_dict = dict(sorted(data_dict.items(), key=lambda x: x[1], reverse=True))
        count = 0
        for code, value in sorted_data_dict.items():
            if code in codes.known_codes:
                count += 1
                recommendations.append((self.languages[code], value))
                if count == max_count:
                    break
        return recommendations

    def reverse_lookup(self, *names):
        codes = []
        for code, language in self.languages.items():
            if language.name in names:
                codes.append(code)
        return codes


if __name__ == '__main__':
    lr = LanguageRecommender()
    lr.read_data()
    print(lr.reverse_lookup('English', 'German', 'Spanish', 'French'))
    # lr.dump_to_json('languages_dump.json')
    # print(lr.data)
    # for language in lr.languages:
    #     print(f"'{language.name}',")
