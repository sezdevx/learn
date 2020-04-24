from enum import Enum
import unittest

class WordKind(Enum):
    Male = 'male'
    Female = 'female'
    PluralMale = 'plural-male'
    PluralFemale = 'plural-female'
    Adjective = 'adjective'
    Adverb = 'adverb'
    Pronoun = 'pronoun'
    Verb = 'verb'
    Preposition = 'preposition'
    Conjuction = 'conjuction'
    Interjection = 'interjection'
    PronominalVerb = 'pronominal-verb'
    Unknown = 'unknown'

    @classmethod
    def noun_prefix(cls, kind):
        if kind == WordKind.Male:
            return 'el'
        elif kind == WordKind.Female:
            return 'la'
        elif kind == WordKind.PluralFemale:
            return 'las'
        elif kind == WordKind.PluralMale:
            return 'los'
        else:
            return ''

    @classmethod
    def parse(cls, str):
        global w2kind
        return w2kind.get(str.strip().lower(), None)

    @classmethod
    def simple_name(cls, kind):
        global kind2w
        return kind2w.get(kind, None)

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    @classmethod
    def is_noun(cls, kind):
        return kind == WordKind.Male.value or kind == WordKind.Female.value or \
               kind == WordKind.PluralFemale.value or kind == WordKind.PluralMale.value

    @classmethod
    def is_verb(cls, kind):
        return kind == WordKind.Verb.value or kind == WordKind.PronominalVerb.value

    @property
    def noun(self):
        return WordKind.is_noun(self.value)

    @property
    def verb(self):
        return WordKind.is_verb(self.value)

    @property
    def unknown(self):
        return self.value == WordKind.Unknown.value

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
    'unknown': WordKind.Unknown
}


kind2w = {
    WordKind.Male: 'male',
    WordKind.Female: 'female',
    WordKind.PluralMale: 'plural-male',
    WordKind.PluralFemale: 'plural-female',
    WordKind.Adjective: 'adj',
    WordKind.Adverb: 'adv',
    WordKind.Pronoun: 'pro',
    WordKind.Verb: 'v',
    WordKind.PronominalVerb: 'pv',
    WordKind.Preposition: 'pre',
    WordKind.Conjuction: 'conj',
    WordKind.Interjection: 'inter',
    WordKind.Unknown: 'unknown'
}

class WordKindTesting(unittest.TestCase):
    def test_is_noun(self):
        assert WordKind.is_noun('male')
        assert WordKind.is_noun('female')
        assert WordKind.is_noun('plural-male')
        assert WordKind.is_noun('plural-female')
        assert WordKind.Male.noun
        assert WordKind.Female.noun
        assert WordKind.PluralMale.noun
        assert WordKind.PluralFemale.noun
        assert not WordKind.Verb.noun
        assert not WordKind.Adjective.noun

    def test_is_verb(self):
        assert WordKind.is_verb('verb')
        assert WordKind.is_verb('pronominal-verb')
        assert not WordKind.Male.verb
        assert not WordKind.Female.verb

    def test_parse(self):
        assert WordKind.parse('m') == WordKind.Male
        assert WordKind.parse('male') == WordKind.Male
        assert WordKind.parse('f') == WordKind.Female
        assert WordKind.parse('female') == WordKind.Female
        assert WordKind.parse('plural-male') == WordKind.PluralMale
        assert WordKind.parse('pluralmale') == WordKind.PluralMale
        assert WordKind.parse('pmale') == WordKind.PluralMale
        assert WordKind.parse('pm') == WordKind.PluralMale
        assert WordKind.parse('plural-female') == WordKind.PluralFemale
        assert WordKind.parse('pluralfemale') == WordKind.PluralFemale
        assert WordKind.parse('pfemale') == WordKind.PluralFemale
        assert WordKind.parse('pf') == WordKind.PluralFemale

        assert WordKind.parse('adj') == WordKind.Adjective
        assert WordKind.parse('adjective') == WordKind.Adjective

        assert WordKind.parse('adv') == WordKind.Adverb
        assert WordKind.parse('adverb') == WordKind.Adverb

        assert WordKind.parse('pronoun') == WordKind.Pronoun
        assert WordKind.parse('pro') == WordKind.Pronoun

        assert WordKind.parse('conj') == WordKind.Conjuction
        assert WordKind.parse('conjuction') == WordKind.Conjuction

        assert WordKind.parse('verb') == WordKind.Verb
        assert WordKind.parse('v') == WordKind.Verb

if __name__ == 'main':
    word_kind_suite = unittest.TestSuite()
    word_kind_suite.addTest(WordKindTesting("test_is_noun"))
    word_kind_suite.addTest(WordKindTesting("test_is_verb"))
    word_kind_suite.addTest(WordKindTesting("test_parse"))
    runner = unittest.TextTestRunner()
    runner.run(word_kind_suite)


