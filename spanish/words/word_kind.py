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
    Conjunction = 'conjunction'
    Interjection = 'interjection'
    PronominalVerb = 'pronominal-verb'
    Unknown = 'unknown'

    @classmethod
    def get_noun_prefix(cls, kind):
        if kind == WordKind.Male:
            return 'el '
        elif kind == WordKind.Female:
            return 'la '
        elif kind == WordKind.PluralFemale:
            return 'las '
        elif kind == WordKind.PluralMale:
            return 'los '
        else:
            return ''

    @classmethod
    def is_noun(cls, kind):
        return kind == WordKind.Male or kind == WordKind.Female or \
               kind == WordKind.PluralFemale or kind == WordKind.PluralMale

    @classmethod
    def is_verb(cls, kind):
        return kind == WordKind.Verb or kind == WordKind.PronominalVerb

    @classmethod
    def is_unknown(cls, kind):
        return kind == WordKind.Unknown

    @classmethod
    def parse_string(cls, string):
        global w2kind
        return w2kind.get(string.strip().lower(), None)

    @classmethod
    def to_string(cls, kind):
        global kind2w
        return kind2w.get(kind, None)

    def __str__(self):
        return WordKind.to_string(self)

    def __repr__(self):
        return WordKind.to_string(self)

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
    'pv': WordKind.PronominalVerb,
    'preposition': WordKind.Preposition,
    'pre': WordKind.Preposition,
    'prep': WordKind.Preposition,
    'Conjunction': WordKind.Conjunction,
    'conj': WordKind.Conjunction,
    'interjection': WordKind.Interjection,
    'inter': WordKind.Interjection,
    'unknown': WordKind.Unknown,
    'u': WordKind.Unknown
}

kind2w = {
    WordKind.Male: 'm',
    WordKind.Female: 'f',
    WordKind.PluralMale: 'pm',
    WordKind.PluralFemale: 'pf',
    WordKind.Adjective: 'adj',
    WordKind.Adverb: 'adv',
    WordKind.Pronoun: 'pro',
    WordKind.Verb: 'v',
    WordKind.PronominalVerb: 'pv',
    WordKind.Preposition: 'pre',
    WordKind.Conjunction: 'conj',
    WordKind.Interjection: 'inter',
    WordKind.Unknown: 'u'
}

class WordKindTesting(unittest.TestCase):
    def test_is_noun(self):
        assert WordKind.is_noun(WordKind.parse_string('male'))
        assert WordKind.is_noun(WordKind.parse_string('m'))
        assert WordKind.is_noun(WordKind.parse_string('female'))
        assert WordKind.is_noun(WordKind.parse_string('f'))
        assert WordKind.is_noun(WordKind.parse_string('pm'))
        assert WordKind.is_noun(WordKind.parse_string('pf'))
        assert WordKind.is_noun(WordKind.parse_string('plural-male'))
        assert WordKind.is_noun(WordKind.parse_string('plural-female'))
        assert WordKind.is_noun(WordKind.parse_string('pluralfemale'))
        assert WordKind.is_noun(WordKind.parse_string('pluralmale'))

    def test_is_verb(self):
        assert WordKind.is_verb(WordKind.parse_string('v'))
        assert WordKind.is_verb(WordKind.parse_string('pv'))
        assert WordKind.is_verb(WordKind.parse_string('verb'))
        assert WordKind.is_verb(WordKind.parse_string('pronominal-verb'))
        assert not WordKind.is_verb(WordKind.parse_string('pronominal-ver'))

    def test_parse_string(self):
        assert str(WordKind.Male) == 'm'
        assert str(WordKind.Female) == 'f'
        assert str(WordKind.PluralFemale) == 'pf'
        assert str(WordKind.PluralMale) == 'pm'

if __name__ == 'main':
    word_kind_suite = unittest.TestSuite()
    word_kind_suite.addTest(WordKindTesting("test_is_noun"))
    word_kind_suite.addTest(WordKindTesting("test_is_verb"))
    word_kind_suite.addTest(WordKindTesting("test_parse_string"))
    runner = unittest.TextTestRunner()
    runner.run(word_kind_suite)
