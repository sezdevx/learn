from enum import Enum
from bank_utils import VocabError
import unittest
import re

class InvalidWordObjName(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message


class WordAttribs(Enum):
    SYNONYMS = 'synonyms'
    ANONYMS = 'anonyms'
    IMAGES = 'images'
    SOUNDS = 'sounds'
    KEYWORD = 'keyword'

    @classmethod
    def is_list(cls, attrib):
        return (attrib == WordAttribs.SYNONYMS or
                attrib == WordAttribs.ANONYMS or
                attrib == WordAttribs.IMAGES
                )

class WordObjName():
    # el fin de semana[1]:images[1]
    name_regex = re.compile(r'^\w+(\s\w+)?(\s\w+)?(\s\w+)?(\[\d+\])?(:\w+)?(\[\d+\])?$')

    @classmethod
    def is_valid(cls, name):
        return WordObjName.name_regex.match(name)

    @classmethod
    def parse_object_name(cls, word):
        name = word
        meaning_idx = 0
        attrib = None
        attrib_idx = 0
        idx = name.find(':')
        if idx == -1:
            if name.endswith(']'):
                idx = name.find('[')
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidWordObjName("Not a valid index: " + str + " in " + word)
                meaning_idx = int(str)
                name = name[:idx]
        else:
            attrib = name[idx+1:].lower()
            name = name[:idx]
            if name.endswith(']'):
                idx = name.find('[')
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidWordObjName("Not a valid meaning index: " + str + " in " + word)
                meaning_idx = int(str)
                if meaning_idx == 0:
                    raise InvalidWordObjName("Not a valid meaning index: " + str + " in " + word)
                name = name[:idx]
            if attrib.endswith(']'):
                idx = attrib.find('[')
                str = attrib[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidWordObjName("Not a valid attribute index: " + str + " in " + word)
                attrib_idx = int(str)
                if attrib_idx == 0:
                    raise InvalidWordObjName("Not a valid attribute index: " + str + " in " + word)
                attrib = attrib[:idx]

        if attrib:
            for a in WordAttribs:
                if a.value.startswith(attrib):
                    attrib = a
                    break
            else:
                raise InvalidWordObjName("Not a valid word attribute: " + attrib + " in "+ word)

        if attrib and not WordAttribs.is_list(attrib) and attrib_idx != 0:
            raise InvalidWordObjName("Not a list attribute: " + attrib + " in " + word)

        return [name, meaning_idx, attrib, attrib_idx]


class WordKind(Enum):
    Male = "m"
    Female = "f"
    PluralMale = "pm"
    PluralFemale = "pf"
    Adjective = "adj"
    Adverb = "adv"
    Pronoun = "pro"
    Preposition = 'prep'
    Conjuction = 'conj'
    Interjection = 'inter'
    Verb = "v"
    PronominalVerb = "pv"
    Unknown = "u"

    @classmethod
    def parse(cls, str):
        global w2kind
        return w2kind.get(str.strip().lower(), None)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

w2kind = {
    'male': WordKind.Male,
    'm': WordKind.Male,
    'female': WordKind.Female,
    'f': WordKind.Female,
    'plural-male': WordKind.PluralMale,
    'pluralmale': WordKind.PluralMale,
    'pmale': WordKind.PluralMale,
    'pm': WordKind.PluralMale,
    'plural-female': WordKind.PluralFemale,
    'pluralfemale': WordKind.PluralFemale,
    'pfemale': WordKind.PluralFemale,
    'pf': WordKind.PluralFemale,
    'adjective': WordKind.Adjective,
    'adj': WordKind.Adjective,
    'adverb': WordKind.Adverb,
    'adv': WordKind.Adverb,
    'pronoun': WordKind.Pronoun,
    'pro': WordKind.Pronoun,
    'verb': WordKind.Verb,
    'v': WordKind.Verb,
    'pronominal-verb': WordKind.PronominalVerb,
    'pverb': WordKind.PronominalVerb,
    'preposition': WordKind.Preposition,
    'pre': WordKind.Preposition,
    'prep': WordKind.Preposition,
    'conjuction': WordKind.Conjuction,
    'conj': WordKind.Conjuction,
    'interjection': WordKind.Interjection,
    'inter': WordKind.Interjection,
    'unknown': WordKind.Unknown,
    'u': WordKind.Unknown
}

class Testing(unittest.TestCase):
    def test_word_kind_parse(self):
        assert WordKind.parse("v") == WordKind.Verb
        assert WordKind.parse("verb") == WordKind.Verb
        assert WordKind.parse("inter") == WordKind.Interjection
        assert WordKind.parse("u") == WordKind.Unknown
        assert WordKind.parse("unknown") == WordKind.Unknown

    def test_word_obj_name_parse(self):
        assert WordObjName.parse_object_name("el padre") == ["el padre", 0, None, 0]
        assert WordObjName.parse_object_name("el padre[1]") == ["el padre", 1, None, 0]
        assert WordObjName.parse_object_name("el padre:images") == ["el padre", 0, WordAttribs.IMAGES, 0]
        assert WordObjName.parse_object_name("el padre:images[1]") == ["el padre", 0, WordAttribs.IMAGES, 1]
        assert WordObjName.parse_object_name("el padre[2]:images[1]") == ["el padre", 2, WordAttribs.IMAGES, 1]
        try:
            assert WordObjName.parse_object_name("el padre[2]:doesnotexist[1]") == ["el padre", 2, WordAttribs.IMAGES, 1]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid word attribute: doesnotexist in el padre[2]:doesnotexist[1]'
        try:
            assert WordObjName.parse_object_name("el padre[2]:images[0]") == ["el padre", 2, WordAttribs.IMAGES, 0]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid attribute index: 0 in el padre[2]:images[0]'
        try:
            assert WordObjName.parse_object_name("el padre[0]:images") == ["el padre", 0, WordAttribs.IMAGES, 0]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid meaning index: 0 in el padre[0]:images'


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_word_kind_parse"))
    test_suite.addTest(Testing("test_word_obj_name_parse"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

