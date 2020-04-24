
from word_kind import WordKind
from spanish import Spanish

class ReverseWord():

    @property
    def exists(self):
        return self.reverse_meanings != None

    def get_meanings(self):
        if self.reverse_meanings:
            return self.reverse_meanings
        else:
            return []

    def __str__(self):
        return self.rw

    def __init__(self, rw, bank):
        self.rw = rw
        self.bank = bank

        self.reverse_meanings = self.bank.rwords.get(rw, None)


class Word():

    def mark_questionable(self):
        if self.real_index != -1:
            self.meanings[self.real_index]['q'] = 'T'

    def mark_unquestionable(self):
        if self.real_index != -1:
            self.meanings[self.real_index]['q'] = 'F'

    @property
    def questionable(self):
        if self.real_index != -1:
            return self.meanings[self.real_index].get("q", 'T') == 'T'
        return True

    @property
    def simple_name(self):
        if self.index == 0:
            return self.name + "(" + WordKind.simple_name(self.kind) + ")"
        else:
            return self.name + "(" + WordKind.simple_name(self.kind) + ")[" + str(self.index) + "]"

    def __str__(self):
        if self.index == 0:
            if self.is_noun:
                return WordKind.noun_prefix(self.kind) + " " + self.name
            else:
                return self.name
        else:
            if self.is_noun:
                return WordKind.noun_prefix(self.kind) + " " + self.name + "[" + str(self.index) + "]"
            else:
                return self.name + "[" + str(self.index) + "]"


    @property
    def is_noun(self):
        return WordKind.is_noun(self.kind)

    @property
    def exists(self):
        return self.real_index != -1

    @property
    def is_general_word(self):
        return self.index == 0

    @property
    def meaning_count(self):
        if self.meanings:
            return len(self.meanings)
        else:
            return 0

    def get_meanings(self):
        if self.real_index != -1:
            return self.meanings[self.real_index]['m']
        else:
            return []

    def get_list_attrib(self, attribute):
        if self.real_index != -1:
            return self.meanings[self.real_index].get(attribute, [])
        return []

    def get_string_attrib(self, attribute):
        if self.real_index != -1:
            return self.meanings[self.real_index].get(attribute, "")
        return ""

    @classmethod
    def get_attribute(cls, attribute):
        if "synonyms".startswith(attribute):
            return "s"
        elif "antonyms".startswith(attribute):
            return "a"
        elif "files".startswith(attribute):
            return "f"
        elif "keyword".startswith(attribute):
            return "k"
        else:
            raise Exception("No such attribute: " + attribute)

    @classmethod
    def is_attribute_list(cls, attribute):
        if "synonyms".startswith(attribute):
            return True
        elif "antonyms".startswith(attribute):
            return True
        elif "files".startswith(attribute):
            return True
        elif "keyword".startswith(attribute):
            return False
        else:
            raise Exception("No such attribute: " + attribute)

    def attr_append(self, attribute, values):
        if self.exists:
            attribute = Word.get_attribute(attribute)
            if attribute:
                if Word.is_attribute_list(attribute):
                    stored = self.meanings[self.real_index].get(attribute, None)
                    if not stored:
                        self.meanings[self.real_index][attribute] = values
                    else:
                        for value in values:
                            if value not in stored:
                                stored.append(value)
                else:
                    stored = self.meanings[self.real_index].get(attribute, None)
                    if not stored:
                        self.meanings[self.real_index][attribute] = ''.join(values)
                    else:
                        self.meanings[self.real_index][attribute] = stored + ''.join(values)
                return True
            else:
                return False
        return False

    def attr_remove(self, attribute, values):
        r = []
        if self.exists:
            attribute = Word.get_attribute(attribute)
            if attribute:
                if Word.is_attribute_list(attribute):
                    stored = self.meanings[self.real_index].get(attribute, None)
                    if not stored:
                        return False
                    else:
                        for value in values:
                            if value in stored:
                                stored.remove(value)
                            else:
                                r.append(value)
                    if len(self.meanings[self.real_index][attribute]) == 0:
                        del self.meanings[self.real_index][attribute]
                else:
                    stored = self.meanings[self.real_index].get(attribute, None)
                    if stored == ''.join(values):
                        del self.meanings[self.real_index][attribute]
                    else:
                        return [''.join(values)]
                return r
        return ['']

    def attr_assign(self, attribute, values):
        if self.exists:
            attribute = Word.get_attribute(attribute)
            if Word.is_attribute_list(attribute):
                self.meanings[self.real_index][attribute] = values
            else:
                self.meanings[self.real_index][attribute] = ''.join(values)
            return True
        return False

    def add_tag(self, tag):
        if self.exists:
            tags = self.meanings[self.real_index].get('t', None)
            if not tags:
                self.meanings[self.real_index]['t'] = [tag]
            elif tag not in tags:
                tags.append(tag)
            return True
        return False

    def remove_tag(self, tag):
        if self.exists:
            tags = self.meanings[self.real_index].get('t', None)
            if not tags:
                return
            elif tag in tags:
                tags.remove(tag)
            return True
        return False

    def add_phrase(self, sid):
        if self.exists:
            examples = self.meanings[self.real_index].get('x', None)
            if not examples:
                self.meanings[self.real_index]['x'] = [sid]
            elif sid not in examples:
                examples.append(sid)
            return True
        return False

    def remove_phrase(self, sid):
        if self.exists:
            examples = self.meanings[self.real_index].get('x', None)
            if not examples:
                return
            elif sid in examples:
                examples.remove(sid)
            return True
        return False

    def remove_meanings(self, meanings):
        r = []
        if self.real_index != -1:
            for m in meanings:
                if m in self.meanings[self.real_index]['m']:
                    self.meanings[self.real_index]['m'].remove(m)
                    rwl = self.bank.rwords.get(m, None)
                    if rwl:
                        try:
                            rwl.remove(self.simple_name)
                        except:
                            pass
                    if len(rwl) == 0:
                        del self.bank.rwords[m]
                else:
                    r.append(m)
            if len(self.meanings[self.real_index]['m']) == 0:
                del self.meanings[self.real_index]
                i = self.real_index
                while i < len(self.meanings): # handle the shifting
                    self.real_index = i
                    self.index = i+2
                    meanings = self.get_meanings()
                    for rw in meanings:
                        self.bank.update_reverse_word(rw, self, i+1)
                    i+=1
                if len(self.bank.words[self.word_key][1]) == 0:
                    del self.bank.words[self.word_key]

            return r
        else:
            return r

    def append_meanings(self, meanings):
        if self.real_index != -1:
            for m in meanings:
                if m not in self.meanings[self.real_index]['m']:
                    self.meanings[self.real_index]['m'].append(m)
                    rwl = self.bank.rwords.get(m, None)
                    if not rwl:
                        self.bank.rwords[m] = [self.simple_name]
                    else:
                        rwl.append(self.simple_name)
            return True
        else:
            return False

    def set_meanings(self, meanings):
        if self.real_index != -1:
            self.meanings[self.real_index]['m'] = meanings
            for m in meanings:
                rwl = self.bank.rwords.get(m, None)
                if not rwl:
                    self.bank.rwords[m] = [self.simple_name]
                else:
                    rwl.append(self.simple_name)
            return True
        else:
            return False

    def __init__(self, word, bank):
        self.bank = bank
        word = word.lower()
        self.index = 0
        self.real_index = -1
        if word.endswith(']'):
            idx = word.find('[')
            if idx == -1:
                raise Exception("Invalid word: " + word)
            no = word[idx+1:-1]
            if not no.isnumeric():
                raise Exception("Invalid index in " + word)
            self.index = int(no)
            word = word[:idx]

        self.kind = WordKind.Unknown

        if word.endswith(')'):
            idx = word.find('(')
            if idx == -1:
                raise Exception("Invalid word: " + word)
            self.kind = WordKind.parse(word[idx+1:-1])
            word = word[:idx]

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
        if len(word) == 0:
            raise Exception("Invalid word: " + word)

        self.name = word
        self.normalized = Spanish.normalize(self.name)
        self.word_key = self.normalized
        self.find()

    def create(self):
        if self.real_index != -1:
            return False

        if not self.meanings:
            self.bank.words[self.word_key] = [self.name, []]
            self.meanings = self.bank.words[self.word_key][1]

        # we have the meanings node, we just need to extend it
        self.meanings.append({'m': [],
                              'wk': WordKind.simple_name(self.kind),
                              })
        self.real_index = len(self.meanings) - 1
        return True


    def find(self):
        self.meanings = None
        word_node = self.bank.words.get(self.word_key, None)
        if not word_node:
            # in case the other word is deleted
            word_node = self.bank.words.get(self.name, None)
            if not word_node:
                return None
            self.word_key = self.name
        elif word_node[0] != self.name:
            if self.word_key == self.name:
                self.name = word_node[0]
            else:
                word_node = self.bank.words.get(self.name, None)
                if not word_node:
                    return None
                self.word_key = self.name

        self.meanings = word_node[1]
        assert len(self.meanings) != 0

        if 0 < self.index <= len(self.meanings):
            kind =  WordKind.parse(self.meanings[self.index-1]['wk'])
            if self.kind.unknown:
                self.kind = kind
                self.real_index = self.index-1
            elif self.kind != kind:
                raise Exception("Mismatched word kind with the given index: " + self.simple_name)
        elif self.index == 0:
            kind =  WordKind.parse(self.meanings[0]['wk'])
            if self.kind.unknown or self.kind == kind:
                self.kind = kind
                self.real_index = 0
            elif self.kind != kind:
                i = 1
                while i < len(self.meanings):
                    if self.kind == WordKind.parse(self.meanings[i]['wk']):
                        break
                    i+=1
                if i != len(self.meanings):
                    self.real_index = i
                else:
                    # this must be a new meaning assignment
                    self.real_index = -1
                    pass







