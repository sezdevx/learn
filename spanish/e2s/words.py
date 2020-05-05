from enum import Enum
from bank_utils import VocabError
import unittest
import re
from spanish import Spanish

class WordTextAttribute():
    def __init__(self, attrib, word):
        self.word = word
        self.attrib = attrib
        self.key = attrib.key

    def assign(self, text):
        self.word.node[self.key] = text

    def remove(self):
        del self.word.node[self.key]


class WordListAttribute():
    def __init__(self, attrib, attribute_idx, word):
        self.word = word
        self.attribute = attrib
        self.index = attribute_idx
        self.key = attrib.key

    def assign(self, value):
        if isinstance(value, list):
            if self.index == 0:
                self.word.node[self.key] = value
            else:
                raise VocabError("Can not assign a list to index: " + str(self))
        elif self.index != 0:
            node = self.word.node[self.key]
            node[self.index-1] = value
        else:
            self.word.node[self.key] = [value]

    def __str__(self):
        if self.index == 0:
            return str(self.word) + str(self.attribute)
        else:
            return str(self.word) + str(self.attribute) + "[" + self.index + "]"

    def remove(self):
        if self.index == 0:
            del self.word.node[self.key]
        else:
            self.word.node[self.key].remove(self.index-1)

class Word():
    @property
    def exists(self):
        return self.node != None

    def __init__(self, word, index, words, bank):
        self.words = words
        self.bank = bank
        self.index = index
        self.kind = WordKind.Unknown

        if word.startswith("el "):
            self.kind = WordKind.Male
            word = word[3:]
        elif word.startswith("la "):
            self.kind = WordKind.Female
            word = word[3:]
        elif word.startswith("los "):
            self.kind = WordKind.PluralMale
            word = word[4:]
        elif word.startswith('las '):
            self.kind = WordKind.PluralFemale
            word = word[4:]

        self.name = word
        self.normalized = Spanish.normalize(self.name)
        self.word_key = self.normalized
        self.meanings = None
        self.real_index = -1
        self.node = None
        self.find()
        if self.real_index != -1:
            self.node = self.meanings[self.real_index]

    def create(self, kind, meaning):
        if self.index != 0:
            raise VocabError("Can not create a word with an index: " + str(self))

        word_node = self.words.get(self.word_key, None)
        if not word_node:
            word_node = [self.name, self.kind, []]
            self.words[self.word_key] = word_node
        elif word_node[0] != self.name:
            if self.word_key == self.name: # already normalized
                self.name = word_node[0]
            else: # try another node
                word_node = self.words.get(self.name, None)
                if not word_node:
                    word_node = [self.name, self.kind, []]
                    self.words[self.word_key] = word_node
                self.word_key = self.name

        self.meanings = word_node[2]


    def find(self):
        word_node = self.words.get(self.word_key, None)
        if not word_node:
            # in case the other word is deleted
            word_node = self.words.get(self.name, None)
            if not word_node:
                return None
            self.word_key = self.name
        elif word_node[0] != self.name:
            if self.word_key == self.name: # already normalized
                self.name = word_node[0]
            else: # try another node
                word_node = self.words.get(self.name, None)
                if not word_node:
                    return None
                self.word_key = self.name

        self.meanings = word_node[2]

        kind = WordKind.parse(word_node[1])
        if 0 < self.index <= len(self.meanings):
            if self.meanings[self.index-1].get('wk', None):
                kind =  WordKind.parse(self.meanings[self.index-1]['wk'])
            self.real_index = self.index - 1
        else:
            if self.index != 0:
                raise VocabError("Invalid index: " + str(self))
            self.real_index = 0

        if self.kind.unknown:
            self.kind = kind
        elif self.kind != kind:
            raise VocabError("Mismatched kinds: " + str(self))

    def get_attribute(self, attrib, attrib_index):
        if not attrib or not self.node:
            return None
        key = attrib.key
        a = self.node.get(key, None)
        if not a:
            return None

        if WordAttribs.is_list(attrib):
            if 0 <= attrib_index <= len(a):
                return WordListAttribute(attrib, attrib_index, self)
            else:
                raise InvalidWordObjName("Invalid index: " + attrib + " " + attrib_index + " for word " + str(self))
        else:
            return WordTextAttribute(attrib, self)


class Words():

    def __init__(self, words, bank):
        self.bank = bank
        self.words = words

    def __getitem__(self, word):
        name, index, attrib, attrib_index = WordObjName.parse_object_name(word)
        if not attrib:
            w = Word(name, index, self.words, self.bank)
            if w.exists:
                return w
        else:
            w = Word(name, index, self.words, self.bank)
            if w.exists:
                return w.get_attribute(attrib, attrib_index)
        return None

    @property
    def count(self):
        return len(self.words)

    def add(self, word, index, meaning):
        w = Word(word, index, self.words, self.bank)
        w.create()


class InvalidWordObjName(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message


class WordAttribs(Enum):
    SYNONYMS = 'synonyms'
    ANONYMS = 'anonyms'
    IMAGES = 'images'
    KEYWORD = 'keyword'

    @property
    def key(self):
        return WordAttribs.get_json_key(self)

    @classmethod
    def get_json_key(cls, attrib):
        if attrib == WordAttribs.SYNONYMS:
            return 's'
        elif attrib == WordAttribs.IMAGES:
            return 'i'
        elif attrib == WordAttribs.ANONYMS:
            return 'a'
        elif attrib == WordAttribs.KEYWORD:
            return 'k'
        else:
            return None

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

    def unknown(self):
        return self.value == 'u'

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
    def test_words(self):
        words = Words({}, None)
        words.add("el padre", ["father"])
        assert words.count == 1

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

