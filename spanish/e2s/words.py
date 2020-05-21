from enum import Enum
from bank_utils import VocabError
import unittest
import re
from spanish import Spanish
import datetime

class WordTextAttribute():
    def __init__(self, attrib, word):
        self.word = word
        self.attrib = attrib
        self.key = attrib.key

    def assign(self, text):
        self.word.node[self.key] = text

    @property
    def value(self):
        if self.word.exists:
            if self.key in self.word.node:
                return self.word.node[self.key]
        return None

    def remove(self, text):
        if self.word.node[self.key] == text:
            del self.word.node[self.key]

    def append(self, text):
        if isinstance(text, list):
            if len(text) != 1:
                raise VocabError("Can not append more than one value: " + ','.join(text))
            text = text[0]
        if self.key in self.word.node:
            self.word.node[self.key] += text
        else:
            self.word.node[self.key] = text

    def delete(self):
        del self.word.node[self.key]


class WordListAttribute():
    def __init__(self, attrib, attribute_idx, word):
        self.word = word
        self.attribute = attrib
        self.index = attribute_idx
        self.key = attrib.key

    def __getitem__(self, item):
        if self.index != 0:
            raise VocabError("Can not index into an already indexed attribute")

        if isinstance(item, int):
            if self.key in self.word.node and 0 < item <= len(self.word.node[self.key]):
                return self.word.node[self.key][item-1]

        raise VocabError("Out of bounds index: " + str(item))


    def assign(self, value):
        if isinstance(value, list):
            if self.index == 0:
                self.word.node[self.key] = value
            else:
                raise VocabError("Can not assign a list to index: " + str(self))
        elif self.index != 0:
            self.word.node[self.key][self.index-1] = value
        else:
            self.word.node[self.key] = [value]

    def append(self, value):
        if self.index != 0:
            raise VocabError("Can not append to indexed attribute: " + str(self))
        if isinstance(value, list):
            if self.key in self.word.node:
                self.word.node[self.key].extend(value)
            else:
                self.word.node[self.key] = value
        else:
            if self.key in self.word.node:
                self.word.node[self.key].append(value)
            else:
                self.word.node[self.key] = [value]

    def remove(self, value):
        if self.index != 0:
            raise VocabError("Can not append to indexed attribute: " + str(self))
        if isinstance(value, list):
            if self.key in self.word.node:
                for v in value:
                    self.word.node[self.key].remove(v)
        else:
            if self.key in self.word.node:
                self.word.node[self.key].remove(value)

    def __str__(self):
        if self.index == 0:
            return str(self.word) + str(self.attribute)
        else:
            return str(self.word) + str(self.attribute) + "[" + self.index + "]"

    @property
    def value(self):
        if self.word.exists:
            if self.key in self.word.node:
                return ','.join(self.word.node[self.key])
        return None

    def delete(self):
        if self.index == 0:
            del self.word.node[self.key]
        else:
            del self.word.node[self.key][self.index-1]

class WordMeaningIterator():
    def __init__(self, word):
        if word.index != 0:
            raise VocabError("Can not iterate indexed word: " + str(word))
        self.word = word
        self.current = 0
        self.limit = len(self.word.meanings)

    def __iter__(self):
        self.current = 0
        self.limit = len(self.word.meanings)
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            return Word(self.word.name, WordKind.Unknown, self.current, self.word.words, self.word.bank)
        raise StopIteration

class Word():
    @property
    def exists(self):
        return self.node != None

    @property
    def meaning_count(self):
        return len(self.meanings)

    @property
    def since_creation(self):
        d = datetime.datetime.fromtimestamp(self.node['tc'])
        n = datetime.datetime.utcnow()
        return (n - d).days

    @property
    def since_last_access(self):
        d = datetime.datetime.fromtimestamp(self.node['tl'])
        n = datetime.datetime.utcnow()
        return (n - d).days

    @property
    def tags(self):
        return self.node['t'][:]

    def remove_tag(self, tag):
        if self.node:
            self.node['t'].remove(tag)

    def add_tag(self, tag):
        if self.node and tag not in self.node['t']:
            self.node['t'].append(tag)

    def __iter__(self):
        return WordMeaningIterator(self)

    @property
    def pretty_name(self):
        return WordKind.get_prefix(self.kind) + self.name

    @classmethod
    def parse(cls, name):
        word = name
        kind = WordKind.Unknown
        if word.startswith("el "):
            kind = WordKind.Male
            word = word[3:]
        elif word.startswith("la "):
            kind = WordKind.Female
            word = word[3:]
        elif word.startswith("los "):
            kind = WordKind.PluralMale
            word = word[4:]
        elif word.startswith('las '):
            kind = WordKind.PluralFemale
            word = word[4:]

        index = 0
        if word.endswith(']'):
            idx = word.find('[')
            if idx == -1:
                raise InvalidWordObjName("Missing [ in " + name)
            index = word[idx+1:-1]
            if not index.isnumeric():
                raise InvalidWordObjName("Not a valid index: " + name)
            index = int(index)
            word = word[:idx]

        return [word, kind, index]

    def __init__(self, word, kind, index, words, bank, throw = True):
        self.kind = kind
        self.words = words
        self.bank = bank
        self.index = index

        self.name = word
        self.normalized = Spanish.normalize(self.name)
        self.word_key = self.normalized
        self.meanings = []
        self.real_index = -1
        self.node = None
        self.find(throw)
        if self.real_index != -1:
            self.node = self.meanings[self.real_index]

    def __str__(self):
        if self.index != 0:
            return self.name + "[" + str(self.index) + "]"
        else:
            return self.name

    def delete(self):
        if self.exists:
            # TODO: complete this
            # update other stuff
            if self.index != 0:
                normalized = self.name + "[" + str(self.real_index+1) + "]"
                for tag in self.node['t']:
                    t = self.bank.tags[tag]
                    if t.exists:
                        t.remove_word(normalized, False)

                for rw in self.node['m']:
                    self.bank.words.remove_rword(rw, normalized)

                del self.meanings[self.real_index]
                # handle tgs
                # handle rwords
                if len(self.meanings) == 0:
                    del self.words[self.word_key]
            else:
                normalized = []
                i = 0
                while i < len(self.meanings):
                    normalized.append(self.name + "[" + str(i+1) + "]")
                    i+=1
                for tag in self.node['t']:
                    t = self.bank.tags[tag]
                    if t.exists:
                        t.remove_words(normalized, False)
                i = 0
                for mnode in self.meanings:
                    for rw in mnode['m']:
                        self.bank.words.remove_rword(rw, normalized[i])
                    i += 1

                del self.words[self.word_key]

            self.node = None
            self.real_index = -1

    @property
    def meaning(self):
        if self.exists:
            return ', '.join(self.node['m'])
        else:
            return ''

    def assign_meaning(self, meaning):
        if self.index == 0:
            raise VocabError("Can not update a word without an index: " + str(self))

        normalized = self.name + '[' + str(self.real_index+1) + ']'
        for rw in self.node['m']:
            self.bank.words.remove_rword(rw, normalized)

        for w in meaning:
            self.bank.words.add_rword(w, normalized)

        if isinstance(meaning, list):
            self.node['m'] = meaning
        else:
            self.node['m'] = [meaning]

    def remove_meaning(self, meaning):
        normalized = self.name + '[' + str(self.real_index+1) + ']'
        if isinstance(meaning, list):
            for m in meaning:
                self.bank.words.remove_rword(m, normalized)
                self.node['m'].remove(m)
        else:
            self.bank.words.remove_rword(meaning, normalized)
            self.node['m'].remove(meaning)
        if len(self.node['m']) == 0:
            self.delete()

    def append_meaning(self, meaning):
        normalized = self.name + '[' + str(self.real_index+1) + ']'
        if isinstance(meaning, list):
            for w in meaning:
                self.bank.words.add_rword(w, normalized)
            self.node['m'].extend(meaning)
        else:
            self.bank.words.add_rword(meaning, normalized)
            self.node['m'].append(meaning)


    def create_word_node(self, meaning):
        t = datetime.datetime.utcnow().timestamp()
        return {
            'm': meaning,
            's': [],
            'a': [],
            'tc': t,
            'tl': t,
            't': []
        }

    def create(self, meaning):
        if self.index != 0:
            raise VocabError("Can not create a word with an index: " + str(self))

        if self.kind == WordKind.Unknown and meaning[0].startswith('to '):
            self.kind = WordKind.Verb

        word_node = self.words.get(self.word_key, None)
        if not word_node:
            word_node = [self.name, str(self.kind), []]
            self.words[self.word_key] = word_node
        elif word_node[0] != self.name:
            if self.word_key == self.name: # already normalized
                self.name = word_node[0]
            else: # try another node
                word_node = self.words.get(self.name, None)
                if not word_node:
                    word_node = [self.name, str(self.kind), []]
                    self.words[self.word_key] = word_node
                self.word_key = self.name

        kind = WordKind.parse(word_node[1])
        self.meanings = word_node[2]
        self.node = self.create_word_node(meaning)
        if kind != self.kind:
            self.node['wk'] = self.kind.value
        self.meanings.append(self.node)
        self.real_index = len(self.meanings) - 1
        normalized = self.name + '[' + str(self.real_index+1) + ']'
        for rw in meaning:
            self.bank.words.add_rword(rw, normalized)


    def find(self, throw):
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
        elif self.kind != kind and throw:
            raise VocabError("Mismatched kinds: " + str(self) + ": " + self.kind.value + " vs " + kind.value)

    def __getitem__(self, idx):
        if not self.node:
            return None
        if isinstance(idx, int):
            if self.index != 0:
                raise VocabError("This word is already indexed: " + str(self))
            if 0 < idx <= len(self.meanings):
                return Word(self.name, WordKind.Unknown, idx, self.words, self.bank)
        elif isinstance(idx, str):
            attrib = WordAttribs.parse(idx, idx)
            return self.get_attribute(attrib, 0)
        elif isinstance(idx, WordAttribs):
            return self.get_attribute(idx, 0)
        return None

    def get_attribute(self, attrib, attrib_index):
        if not attrib or not self.node:
            return None
        key = attrib.key
        a = self.node.get(key, None)

        if WordAttribs.is_list(attrib):
            if attrib_index == 0:
                return WordListAttribute(attrib, attrib_index, self)
            elif a and 0 < attrib_index <= len(a):
                return WordListAttribute(attrib, attrib_index, self)
            else:
                raise InvalidWordObjName("Invalid index: " + attrib + " " + attrib_index + " for word " + str(self))
        else:
            return WordTextAttribute(attrib, self)


class WordIterator():
    def __init__(self, words):
        self.words = words
        self.iter = iter(words.words)
        self.current = 0
        self.limit = len(self.words.words)

    def __iter__(self):
        self.current = 0
        self.limit = len(self.words.words)
        self.iter = iter(self.words.words)
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            key = next(self.iter)
            return self.words[key]
        raise StopIteration

class Words():

    def __iter__(self):
        return WordIterator(self)

    def __len__(self):
        return len(self.words)

    def reverse_complete(self, line, text, matches):
        mtext = text
        if text.startswith('?'):
            mtext = text[1:]
        idx = line.rfind(',')
        if idx != -1:
            to_be_completed = line[idx+1:]
            if to_be_completed.find('  ') != -1:
                key = ' '.join(to_be_completed.strip().split())
            else:
                key = to_be_completed.strip()
        else:
            key = mtext

        for rw in self.rwords:
            if rw.startswith(key):
                if mtext != text:
                    matches.append('?' + rw)
                else:
                    matches.append(rw)
                if len(matches) > 10:
                    return False
        return True


    def complete(self, line, text, matches):
        if text.startswith('-'):
            return False
        if line.startswith('more ') or line.startswith('put '):
            if line.startswith('put ') and not self.bank.course:
                return False
            idx = line.rfind(',')
            if idx != -1:
                to_be_completed = line[idx+1:]
                if to_be_completed.find('  ') != -1:
                    key = ' '.join(to_be_completed.strip().split())
                else:
                    key = to_be_completed.strip()
            else:
                key = text

            for w in self.words:
                if w.startswith(key):
                    matches.append(w)
                    if len(matches) > 10:
                        return False
            return True


    # https://github.com/barrust/pyspellchecker/
    def edit_distance_1(self, word):
        letters = self.letters
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [L + R[1:] for L, R in splits if R]
        transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
        replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
        inserts = [L + c + R for L, R in splits for c in letters]
        return set(deletes + transposes + replaces + inserts)

    def __init__(self, bank):
        self.bank = bank
        self.words = bank.data['words']
        self.rwords = bank.data['rwords']
        self.letters = set(bank.data['letters'])

    def remove_rword(self, rword, normalized):
        rword = Spanish.reverse_normalize(rword)
        r = self.rwords.get(rword, None)
        if not r:
            return
        r['w'].remove(normalized)
        if len(r['w']) == 0:
            del self.rwords[rword]

    def add_rword(self, rword, normalized):
        rword = Spanish.reverse_normalize(rword)
        r = self.rwords.get(rword, None)
        if not r:
            r = {'w': []}
            self.rwords[rword] = r
        if not normalized in r['w']:
            r['w'].append(normalized)

    def reverse_lookup(self, rword):
        rword = Spanish.reverse_normalize(rword)
        r = self.rwords.get(rword, None)
        if r:
            return r['w']

    @classmethod
    def denormalize_name(cls, name):
        if name.endswith('[1]'):
            return name[:-3]
        else:
            return name

    def normalize(self, word):
        name, mkind, meaning_idx, attrib, attrib_idx = tuple(WordObjName.parse_object_name(word))
        word_key = Spanish.normalize(name)
        word_node = self.words.get(word_key, None)
        if not word_node:
            word_node = self.words.get(name, None)
            if not word_node:
                return None
        elif word_node[0] != name:
            if word_key != name:
                word_node = self.words.get(name, None)
                if not word_node:
                    return None
            else:
                name = word_node[0]

        meanings = word_node[2]

        kind = WordKind.parse(word_node[1])
        if 0 < meaning_idx <= len(meanings):
            if meanings[meaning_idx-1].get('wk', None):
                kind =  WordKind.parse(meanings[meaning_idx-1]['wk'])
            real_index = meaning_idx - 1
        else:
            if meaning_idx != 0:
                raise VocabError("Invalid index: " + word)
            real_index = 0

        if kind.unknown:
            pass
        elif not mkind.unknown and kind != mkind:
            raise VocabError("Mismatched kinds: " + word)
        node = meanings[real_index]
        if not attrib:
            if meaning_idx == 0:
                meaning_idx = 1
            return name + '[' + str(meaning_idx) + ']'
        attrib_key = WordAttribs.get_json_key(attrib)
        if not attrib_key in node:
            return None
        node = node[attrib_key]
        if meaning_idx == 0:
            meaning_idx = 1
        if attrib_idx == 0:
            attrib_idx = 1
        if not (0 < attrib_idx <= len(node)):
            return None
        return name + '[' + str(meaning_idx) + ']:' + WordAttribs.get_json_key(attrib) + '[' + str(attrib_idx) + ']'




    def __getitem__(self, word):
        name, kind, index, attrib, attrib_index = tuple(WordObjName.parse_object_name(word))
        if not attrib:
            w = Word(name, kind, index, self.words, self.bank)
            if w.exists:
                return w
        else:
            w = Word(name, kind, index, self.words, self.bank)
            if w.exists:
                return w.get_attribute(attrib, attrib_index)
        return None

    def del_word(self, word, kind, index):
        w = Word(word, kind, index, self.words, self.bank, False)
        w.delete()

    def add_word(self, word, kind, index, meaning):
        w = Word(word, kind, index, self.words, self.bank, False)
        w.create(meaning)
        return w


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

    @classmethod
    def parse(cls, attrib, message):
        for a in WordAttribs:
            if a.value.startswith(attrib):
                return a
        else:
            raise InvalidWordObjName("Not a valid word attribute: " + attrib + " in "+ message)

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
            attrib = WordAttribs.parse(attrib, word)

        if attrib and not WordAttribs.is_list(attrib) and attrib_idx != 0:
            raise InvalidWordObjName("Not a list attribute: " + attrib + " in " + word)

        kind = WordKind.Unknown
        if name.startswith("el "):
            kind = WordKind.Male
            name = name[3:]
        elif name.startswith("la "):
            kind = WordKind.Female
            name = name[3:]
        elif name.startswith("los "):
            kind = WordKind.PluralMale
            name = name[4:]
        elif word.startswith('las '):
            kind = WordKind.PluralFemale
            name = name[4:]

        return [name, kind, meaning_idx, attrib, attrib_idx]


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
    def get_prefix(cls, kind):
        if kind == WordKind.Male:
            return "el "
        elif kind == WordKind.Female:
            return "la "
        elif kind == WordKind.PluralFemale:
            return "las "
        elif kind == WordKind.PluralMale:
            return "los "
        elif kind == WordKind.Verb:
            return "(v) "
        elif kind == WordKind.PronominalVerb:
            return "(pv) "
        elif kind == WordKind.Adjective:
            return "(adj) "
        elif kind == WordKind.Pronoun:
            return "(pro) "
        elif kind == WordKind.Interjection:
            return "(inj) "
        elif kind == WordKind.Conjuction:
            return "(coj) "
        elif kind == WordKind.Adverb:
            return "(adv) "
        else:
            return ""

    @classmethod
    def parse(cls, str):
        global w2kind
        return w2kind.get(str.strip().lower(), None)

    @property
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

class DummyBank():

    def __init__(self):
        self.data = {
            'words': {},
        }


class Testing(unittest.TestCase):
    def test_word_index(self):
        bank = DummyBank()
        words = Words(bank)

        from commands import CommandParser
        parser = CommandParser(bank)
        assert not words.normalize("el padre")
        r = parser.parse_command("el padre = father")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("el padre = priest")
        w = words.add_word(r[1], r[2], r[3], r[6])

        w = words["padre"]
        assert w[1].meaning == 'father'
        assert w[2].meaning == 'priest'
        w[1].assign_meaning(['father', 'dad'])
        assert w[1].meaning == 'father, dad'
        w[1].delete()
        assert w[1].meaning == 'priest'

        w[1]["keyword"].assign("Religion")
        assert w[1]["keyword"].value == "Religion"

    def test_words_exists(self):
        bank = DummyBank()
        words = Words(bank)

        from commands import CommandParser
        parser = CommandParser(bank)
        assert not words.normalize("el padre")
        r = parser.parse_command("el padre = father")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("la madre = mother")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("el hermano = brother")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("la hermana = sister")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("el abuelo = grandfather")
        w = words.add_word(r[1], r[2], r[3], r[6])
        assert words.normalize("el padre")
        assert words.normalize("padre")
        assert words.normalize("padre[1]")
        try:
            assert words.normalize("el madre")
        except VocabError as e:
            assert e.message == 'Mismatched kinds: el madre'
        assert words.normalize("madre")
        assert words.normalize("la madre")
        assert words.normalize("la madre[1]")
        assert words["madre"].since_creation == 0
        assert words["madre"].since_last_access == 0

    def test_words_iterator(self):
        bank = DummyBank()
        words = Words(bank)

        from commands import CommandParser
        parser = CommandParser(bank)
        r = parser.parse_command("el padre = father")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("el padre = priest")
        w = words.add_word(r[1], r[2], r[3], r[6])
        i = 0
        meanings = ['father', 'priest']
        for m in w:
            assert m.meaning == meanings[i]
            i+=1
        assert i == 2

        r = parser.parse_command("la madre = mother")
        w = words.add_word(r[1], r[2], r[3], r[6])
        i = 0
        words2 = ['padre', 'madre']
        meanings = ['father', 'mother']
        for w in words:
            assert str(w) == words2[i]
            assert w.meaning == meanings[i]
            i+=1
        assert i == 2

    def test_words(self):
        bank = DummyBank()
        from commands import CommandParser
        parser = CommandParser(bank)
        words = Words(bank)
        r = parser.parse_command("el padre = father")
        #[CommandKind.WORD_ASSIGN, WordKind.Male, "padre", 0, None, 0, ["father"]],
        assert len(words) == 0
        w = words.add_word(r[1], r[2], r[3], r[6])
        assert len(words) == 1
        w.delete()
        assert len(words) == 0

        r = parser.parse_command("el padre = father")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("la madre = mother, mom")
        w2 = words.add_word(r[1], r[2], r[3], r[6])
        assert len(words) == 2

        w = words['padre']
        assert w.meaning == 'father'
        w = words['padre[1]']
        assert w.meaning == 'father'

        w['images'].assign(['/path/to/images.img'])
        assert w['images'].value == '/path/to/images.img'
        w['images'].delete()
        assert w['images'].value == None

        w['im'].assign('/path/to/images.img')
        assert w['images'].value == '/path/to/images.img'
        assert w['images'][1] == '/path/to/images.img'
        w['images'].delete()
        assert w['images'].value == None

        w['key'].assign('parent')
        assert w['key'].value == 'parent'
        w['key'].assign('new one')
        assert w['key'].value == 'new one'
        w['key'].delete()
        assert w['key'].value == None

        w.delete()
        w2.delete()
        assert len(words) == 0
        assert not w.exists
        assert not w2.exists


    def test_word_parse(self):
        assert Word.parse("la madre") == ["madre", WordKind.Female, 0]
        assert Word.parse("el padre") == ["padre", WordKind.Male, 0]
        assert Word.parse("padre[1]") == ["padre", WordKind.Unknown, 1]
        assert Word.parse("el padre[1]") == ["padre", WordKind.Male, 1]

    def test_word_kind_parse(self):
        assert WordKind.parse("v") == WordKind.Verb
        assert WordKind.parse("verb") == WordKind.Verb
        assert WordKind.parse("inter") == WordKind.Interjection
        assert WordKind.parse("u") == WordKind.Unknown
        assert WordKind.parse("unknown") == WordKind.Unknown

    def test_word_obj_name_parse(self):
        assert WordObjName.parse_object_name("el padre") == ["padre", WordKind.Male, 0, None, 0]
        assert WordObjName.parse_object_name("el padre[1]") == ["padre", WordKind.Male, 1, None, 0]
        assert WordObjName.parse_object_name("el padre:images") == ["padre", WordKind.Male, 0, WordAttribs.IMAGES, 0]
        assert WordObjName.parse_object_name("el padre:images[1]") == ["padre", WordKind.Male, 0, WordAttribs.IMAGES, 1]
        assert WordObjName.parse_object_name("el padre[2]:images[1]") == ["padre", WordKind.Male, 2, WordAttribs.IMAGES, 1]
        try:
            assert WordObjName.parse_object_name("el padre[2]:doesnotexist[1]") == ["padre", WordKind.Male, 2, WordAttribs.IMAGES, 1]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid word attribute: doesnotexist in el padre[2]:doesnotexist[1]'
        try:
            assert WordObjName.parse_object_name("el padre[2]:images[0]") == ["padre", WordKind.Male, 2, WordAttribs.IMAGES, 0]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid attribute index: 0 in el padre[2]:images[0]'
        try:
            assert WordObjName.parse_object_name("el padre[0]:images") == ["padre", WordKind.Male, 0, WordAttribs.IMAGES, 0]
        except InvalidWordObjName as e:
            assert e.message == 'Not a valid meaning index: 0 in el padre[0]:images'


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_word_kind_parse"))
    test_suite.addTest(Testing("test_word_obj_name_parse"))
    test_suite.addTest(Testing("test_word_parse"))
    test_suite.addTest(Testing("test_words"))
    test_suite.addTest(Testing("test_words_exists"))
    test_suite.addTest(Testing("test_words_iterator"))
    test_suite.addTest(Testing("test_word_index"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

