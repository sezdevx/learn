import json
import hashlib
import readline

from spanish import Spanish
from word_kind import WordKind
from command_kind import CommandKind
from word import Word
from word import ReverseWord
from tag import Tag
from course import Course

class WordIterator():
    def __init__(self, bank, page_limit):
        self.bank = bank
        self.iter = iter(bank.words)
        self.words = bank.words
        self.current = 0
        self.limit = len(bank.words)
        self.page_limit = page_limit

    def __iter__(self):
        self.current = 0
        self.limit = len(self.words)
        self.iter = iter(self.words)
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            key = next(self.iter)
            w = Word(self.words[key][0], self.bank)
            if self.page_limit > 0 and self.current > 1 and (self.current+1) % self.page_limit == 0:
                x = input("Press enter to continue, [eXit/Quit]: ").strip().lower()
                if x == 'exit' or x == 'quit' or x == 'q' or x == 'x':
                    raise StopIteration
            return w
        raise StopIteration


class WordBank():

    def get_courses(self):
        return self.courses.keys()

    def word_iterator(self, tag = None):
        if tag:
            pass
        else:
            return WordIterator(self, 10)
    @property
    def name(self):
        if self.pwd:
            return self.pwd.name
        else:
            return '/'

    @property
    def total_word_count(self):
        if self.pwd:
            return self.pwd.total_word_count
        else:
            return self.word_count

    @property
    def word_count(self):
        if self.pwd:
            return self.pwd.word_count
        else:
            return len(self.words)

    @property
    def tag_count(self):
        if self.pwd:
            return self.pwd.tag_count
        else:
            return len(self.tags)

    @property
    def phrase_count(self):
        if self.pwd:
            return self.pwd.phrase_count
        else:
            return len(self.p2p)

    def delete_words(self, words):
        r = []
        for w in words:
            word = Word(w, self)
            if word.normalize:
                if self.pwd:
                    self.pwd.remove_word(word.simple_name)
                meanings_root = self.words[word.word_key][1]
                if word.is_general_word:
                    for meanings in meanings_root:
                        for rw in meanings:
                            self.remove_reverse_word(rw, word)
                    del self.words[word.word_key]
                else:
                    meanings = word.get_meanings()
                    for rw in meanings:
                        self.remove_reverse_word(rw, word)
                    del self.words[word.word_key][1][word.real_index]
                    i = word.real_index
                    while i < len(meanings_root): # handle the shifting
                        word.real_index = i
                        word.index = i+2
                        meanings = word.get_meanings()
                        for rw in meanings:
                            self.update_reverse_word(rw, word, i+1)
                        i+=1
                    if len(self.words[word.word_key][1]) == 0:
                        del self.words[word.word_key]
            else:
                r.append(w)

        return r

    def delete_tag(self, tag):
        t = Tag(tag, self)
        if not t.normalize:
            return False
        t.delete()
        return True

    def get_course(self, course):
        c = self.courses.get(course, None)
        if not c:
            return None
        return Course(course, self)

    def change_course(self, course):
        if course == '..':
            self.ppwd = self.pwd
            self.pwd = None
            return True
        elif course == '-':
            (self.pwd, self.ppwd) = (self.ppwd, self.pwd)
            return True
        elif course.startswith('../'):
            course = course[3:]

        if self.pwd and self.pwd.name == course:
            return True

        c = self.courses.get(course, None)
        if not c:
            return False
        self.ppwd = self.pwd
        self.pwd = Course(course, self)
        return True

    def put_in_course(self, line):
        if not self.pwd:
            return False
        if line.startswith('>'):
            line = line[1:].strip()
            source_id = hashlib.md5(Spanish.normalize_phrase(line).encode()).hexdigest()
            s = self.phrases.get(source_id, None)
            if s:
                self.pwd.add_phrase(source_id)
            else:
                return False
        else:
            r = [a.strip() for a in line.split(',')]
            for a in r:
                if a.startswith('#'):
                    tag = Tag(a[1:], self)
                    if tag.normalize:
                        self.pwd.add_tag(tag.full_name)
                else:
                    word = Word(a, self)
                    if word.normalize:
                        self.pwd.add_word(word.simple_name)

        return True


    def create_course(self, course):
        if self.pwd and self.pwd.name == course:
            return True
        c = self.courses.get(course, None)
        if not c:
            self.pwd = Course(course, self)
            self.pwd.create()
        else:
            self.pwd = Course(course, self)
        return True

    def words_list(self, words):
        r = []
        for w in words:
            word = Word(w, self)
            r.append(word)

        return r

    def reverse_words_list(self, words):
        r = []
        for rw in words:
            word = ReverseWord(rw, self)
            r.append(word)

        return r

    def __correct_word_kind(self, word, meanings):
        if meanings and len(meanings) > 0 and meanings[0].startswith('to ') and word.kind.unknown:
            word.kind = WordKind.Verb
        elif meanings and len(meanings) > 0 and WordKind.is_verb(word.kind):
            i = 0
            while i < len(meanings):
                if not meanings[i].startswith('to ') and not meanings[i].startswith('To '):
                    meanings[i] = 'to ' + meanings[i]
                i += 1

    def meaning_append(self, cmd):
        meanings = list(set(cmd[3])) # to make sure that there is no repetition
        word = Word(cmd[2], self)
        self.__correct_word_kind(word, meanings)

        if word.normalize:
            word.append_meanings(meanings)
            self.add_to_history(word)
            if self.pwd:
                self.pwd.add_word(word.simple_name)

            return True

        return False

    def meaning_remove(self, cmd):
        meanings = list(set(cmd[3])) # to make sure that there is no repetition
        word = Word(cmd[2], self)
        self.__correct_word_kind(word, meanings)

        if word.normalize:
            return word.remove_meanings(meanings)

        return [cmd[2]]

    def meaning_attr_assign(self, cmd):
        values = list(set(cmd[4]))
        keyword = cmd[3]
        word = Word(cmd[2], self)

        if word.normalize:
            word.attr_assign(keyword, values)
            return True

        return False

    def meaning_attr_append(self, cmd):
        values = list(set(cmd[4]))
        keyword = cmd[3]
        word = Word(cmd[2], self)

        if word.normalize:
            return word.attr_append(keyword, values)

        return False

    def meaning_attr_remove(self, cmd):
        values = list(set(cmd[4]))
        keyword = cmd[3]
        word = Word(cmd[2], self)

        if word.normalize:
            return word.attr_remove(keyword, values)

        return ['']

    def meaning_assign(self, cmd):
        meanings = list(set(cmd[3])) # to make sure that there is no repetition
        word = Word(cmd[2], self)
        self.__correct_word_kind(word, meanings)

        if not word.create():
            # change the meaning of an existing one
            for rw in word.get_meanings():
                self.remove_reverse_word(rw, word)

        word.set_meanings(meanings)
        if self.pwd:
            self.pwd.add_word(word.simple_name)

        self.add_to_history(word)

        return word

    def clear_history(self):
        self.history.clear()

    def get_history(self):
        if self.pwd:
            return self.pwd.history
        else:
            return self.history

    def add_to_history(self, word):
        if self.pwd:
            self.pwd.add_to_history(word)
        else:
            if len(self.history) > 100:
                self.history.pop(0)
            self.history.append(word)

    def tag_append(self, cmd):
        tag = Tag(cmd[2], self)
        r = []
        if tag.normalize:
            words = cmd[3]
            for w in words:
                word = Word(w, self)
                if word.normalize:
                    word.add_tag(tag.full_name)
                    tag.add_word(word.simple_name)
                else:
                    r.append(w)
        return r

    def tag_remove(self, cmd):
        tag = Tag(cmd[2], self)
        r = []
        if tag.normalize:
            words = cmd[3]
            for w in words:
                word = Word(w, self)
                if word.normalize:
                    word.remove_tag(tag.full_name)
                    tag.remove_word(word.simple_name)
                else:
                    r.append(w)
        return r

    def tag_assign(self, cmd):
        tag = Tag(cmd[2], self)
        words = cmd[3]
        if len(words) > 0 and words[0] == '*':
            if len(self.get_history()) == 0:
                return []

        if tag.normalize:
            tag.delete()
        tag.create()
        r = []
        if len(words) > 0 and words[0] == '*':
            history = self.get_history()
            for w in history:
                w.find()
                if w.normalize:
                    w.add_tag(tag.full_name)
                    tag.add_word(w.simple_name)
                else:
                    r.append(w)
            return r
        else:
            for w in words:
                word = Word(w, self)
                if word.normalize:
                    word.add_tag(tag.full_name)
                    tag.add_word(word.simple_name)
                else:
                    r.append(w)

        if self.pwd:
            self.pwd.add_tag(tag.full_name)

        return r

    def tag_list(self, tag_name):
        tag = Tag(tag_name, self)
        if tag.normalize:
            return [Word(w, self) for w in tag.words]
        return []

    def phrase_list(self, phrase):
        source_id = hashlib.md5(Spanish.normalize_phrase(phrase).encode()).hexdigest()
        r = [phrase]
        s = self.phrases.get(source_id, None)
        if not s:
            return r
        r[0] = s['p']
        p2p = self.p2p.get(source_id, None)
        if not p2p:
            # impossible, but handle it anyway
            del self.phrases[source_id]
            return r
        ts = self.p2p[source_id]['t']
        for tid in ts:
            t = self.phrases.get(tid, None)
            r.append(t['p'])
        return r

    def reverse_phrase_list(self, phrase):
        source_id = hashlib.md5(Spanish.normalize_phrase(phrase).encode()).hexdigest()
        r = [phrase]
        s = self.phrases.get(source_id, None)
        if not s:
            return r
        r[0] = s['p']
        rp2p = self.rp2p.get(source_id, None)
        if not rp2p:
            # impossible, but handle it anyway
            del self.phrases[source_id]
            return r
        ts = self.rp2p[source_id]['s']
        for sid in ts:
            s = self.phrases.get(sid, None)
            r.append(s['p'])
        return r

    def delete_phrase(self, phrase):
        source_id = hashlib.md5(Spanish.normalize_phrase(phrase).encode()).hexdigest()
        s = self.phrases.get(source_id, None)
        if not s:
            return False
        p2p = self.p2p.get(source_id, None)
        if not p2p:
            # impossible, but handle it anyway
            del self.phrases[source_id]
            return False
        ts = self.p2p[source_id]['t']
        for tid in ts:
            rp2p = self.rp2p.get(tid, None)
            if rp2p:
                if source_id in rp2p['s']:
                    rp2p['s'].remove(source_id)
            if not rp2p or len(rp2p)==0:
                t = self.phrases.get(tid, None)
                if t:
                    del self.phrases[tid]

        words = p2p.get('w', None)
        if words:
            for w in words:
                word = Word(w, self)
                if word.normalize:
                    word.remove_phrase(source_id)

        del self.p2p[source_id]
        del self.phrases[source_id]
        return True


    def phrase_assign(self, cmd):
        words = cmd[4]
        original_words = words
        source = cmd[2]
        targets = cmd[3]

        if not words:
            translation = source.maketrans("\t\n\"'\\`@$><=;:|&{()}%#!?¿¡.+-[]", "                              ", "")
            new_source = source.translate(translation)
            original_words = [a.strip().lower() for a in new_source.split(' ')]
            words = [Spanish.get_singular(a) for a in original_words]
            words = [a for a in words if len(a) > 0]
        ws = []
        i = 0
        for w in words:
            if w != original_words[i]: # just to save time
                # we will try the original word first
                w = Word(original_words[i], self)
                if w.normalize:
                    ws.append(w)
                else:
                    w = Word(words[i], self)
                    if w.normalize:
                        ws.append(w)
            else:
                w = Word(w, self)
                if w.normalize:
                    ws.append(w)
            i += 1

        source_id = hashlib.md5(Spanish.normalize_phrase(source).encode()).hexdigest()
        target_ids = [hashlib.md5(Spanish.normalize_phrase(target).encode()).hexdigest() for target in targets]
        s = self.phrases.get(source_id, None)
        if not s:
            self.phrases[source_id] = {'p': source, 'pk': 's'}
        i = 0
        for tid in target_ids:
            s = self.phrases.get(tid, None)
            if not s:
                self.phrases[tid] = {'p': targets[i], 'pk': 't'}
            i += 1
        p2p = self.p2p.get(source_id, None)
        if not p2p:
            self.p2p[source_id] = {'t': [], 'w': []}

        ts = self.p2p[source_id]['t']
        for tid in target_ids:
            if tid not in ts:
                ts.append(tid)
                rp2p = self.rp2p.get(tid, None)
                if not rp2p:
                    self.rp2p[tid] = {'s': [source_id]}
                else:
                    self.rp2p[tid]['s'].append(source_id)

        words = self.p2p[source_id]['w']

        if self.pwd:
            self.pwd.add_phrase(source_id)

        for w in ws:
            w.add_phrase(source_id)
            words.append(w.simple_name)

    def phrase_remove(self, cmd):
        source = cmd[2]
        targets = cmd[3]

        r = []
        source_id = hashlib.md5(Spanish.normalize_phrase(source).encode()).hexdigest()
        target_ids = [hashlib.md5(Spanish.normalize_phrase(target).encode()).hexdigest() for target in targets]
        s = self.phrases.get(source_id, None)
        if not s:
            return [source]
        i = 0
        real_target_ids = []
        for tid in target_ids:
            s = self.phrases.get(tid, None)
            if not s:
                r.append(targets[i])
            else:
                real_target_ids.append(target_ids[i])
            i += 1
        p2p = self.p2p.get(source_id, None)
        if not p2p:
            # IMPOSSIBLE
            return [source]

        ts = p2p['t']
        for tid in real_target_ids:
            if tid in ts:
                ts.remove(tid)
            rp2p = self.rp2p.get(tid, None)
            if rp2p:
                rp2p['s'].remove(source_id)
                if len(rp2p['s']) == 0:
                    del self.rp2p[tid]
                    del self.phrases[tid]
            else:
                # IMPOSSIBLE, but still handle it
                del self.phrases[tid]

        words = self.p2p[source_id]['w']
        for w in words:
            word = Word(w, self)
            word.remove_phrase(source_id)

        if len(p2p['t']) == 0:
            del self.p2p[source_id]
            del self.phrases[source_id]

        return r

    # SUPPORT deleting a translation by index number
    def phrase_remove2(self, cmd):
        source = cmd[2]
        index = cmd[3]

        source_id = hashlib.md5(Spanish.normalize_phrase(source).encode()).hexdigest()
        p2p = self.p2p.get(source_id, None)
        if not p2p:
            return False
        if not (0 < index <= len(p2p['t'])):
            raise Exception("Invalid index: " + cmd[0])
        target_id = p2p['t'][index]
        p2p['t'].remove(target_id)

        rp2p = self.rp2p.get(target_id, None)
        rp2p['s'].remove(source_id)

        words = self.p2p[source_id]['w']
        for w in words:
            word = Word(w, self)
            word.remove_phrase(source_id)

        if len(rp2p['s']) == 0:
            del self.rp2p[target_id]
            del self.phrases[target_id]
        if len(p2p['t']) == 0:
            del self.p2p[source_id]
            del self.phrases[source_id]


    def update_reverse_word(self, rw, word, new_index):
        rwl = self.rwords.get(rw, None)
        w = word.simple_name
        word.index = new_index
        nw = word.simple_name
        if rwl:
            r = []
            i = 0
            for x in rwl:
                if x.startswith(w): # if x starts with w
                    r[i] = nw
                i+=1

    def remove_reverse_word(self, rw, word):
        # remove the reverse word from rword dict
        rwl = self.rwords.get(rw, None)
        w = word.simple_name
        if rwl:
            r = []
            for x in rwl:
                if x.startswith(w): # if x starts with w
                    r.append(x)
            for x in r:
                rwl.remove(x)
            if len(rwl) == 0:
                del self.rwords[rw]

    def __init__(self, path):
        if path:
            self.word_bank_path = path + '.json'
            self.bank = self.load_json(self.word_bank_path)
        else:
            self.word_bank_path = ':memory'
            self.bank = {'words': {}, 'tags': {}}

        self.history = []
        self.pwd = None
        self.ppwd = None
        self.letters = set()
        self.words = self.bank['words']
        for w in self.words:
            self.letters.update(w)
        self.rwords = self.bank['rwords']
        self.tags = self.bank['tags']
        self.courses = self.bank['courses']
        self.phrases = self.bank['phrases']
        self.p2p = self.bank['p2p']
        self.rp2p = self.bank['rp2p']
        self.modified = False

    def complete_tags(self, text):
        text_tag = text[1:]
        idx = text_tag.find('-')
        if idx == -1:
            full_match = None
            for tag_name in self.tags:
                if tag_name.startswith(text_tag):
                    for t in self.tags[tag_name]:
                        if t == '*':
                            if len(self.tags[tag_name]['*']) > 0:
                                self.matches.append('#' + tag_name)
                                if len(self.matches) > 10:
                                    return None
                        else:
                            if len(self.tags[tag_name][t]) > 0:
                                self.matches.append('#' + tag_name + '-' + t)
                                if len(self.matches) > 10:
                                    return None
        else:
            tag = text_tag[:idx]
            sub_tag = text_tag[idx+1:]
            if self.tags.get(tag, None):
                for t in self.tags[tag]:
                    if t != '*' and t.startswith(sub_tag):
                        self.matches.append('#' + tag + '-' + t)
            else:
                return None
        return True

    def complete_words(self, text, line):
        self.matches = []
        idx = line.rfind(' ')
        prefix = ''
        kind = ''
        if idx != -1:
            idx -= 1
            while idx >= 0 and line[idx] == ' ':
                idx-=1
            if idx != -1:
                start = line.rfind(' ', 0, idx)
                if start == -1:
                    start = 0
                else:
                    start += 1
                prefix = line[start:idx+1]

        if prefix:
            if prefix == 'el':
                kind = WordKind.Male
            elif prefix == 'la':
                kind = WordKind.Female
            elif prefix == 'los':
                kind = WordKind.PluralMale
            elif prefix == 'las':
                kind = WordKind.PluralFemale

        for s in self.words:
            if s.startswith(text) or self.words[s][0].startswith(text) or s.startswith(text):
                if kind:
                    wk = WordKind.parse(self.words[s][1][0]['wk'])
                    if wk == kind:
                        self.matches.append(self.words[s][0])
                else:
                    self.matches.append(self.words[s][0])
                if len(self.matches) > 10:
                    return None
        return True


    def complete_rwords(self, text, line):
        self.matches = []
        for s in self.rwords:
            if s.startswith(text):
                self.matches.append(s)
                if len(self.matches) > 10:
                    return None
        return True

    def complete_phrases(self, text):
        self.matches = []
        for p in self.phrases:
            if self.phrases[p]['pk'] == 's' and self.phrases[p]['p'].startswith(text):
                if self.phrases[p]['p'] != text:
                    idx = text.rfind(' ')
                    if idx == -1:
                        self.matches.append(self.phrases[p]['p'])
                    else:
                        self.matches.append(self.phrases[p]['p'][idx+1:])
                if len(self.matches) > 10:
                    return None
        return True

    def complete_reverse_phrases(self, text):
        self.matches = []
        for p in self.phrases:
            if self.phrases[p]['pk'] == 't' and self.phrases[p]['p'].startswith(text):
                if self.phrases[p]['p'] != text:
                    idx = text.rfind(' ')
                    self.matches.append(self.phrases[p]['p'][idx+1:])
                if len(self.matches) > 10:
                    return None
        return True

    def complete_courses(self, text):
        self.matches = []
        for s in self.courses:
            if s.startswith(text):
                self.matches.append(s)
                if len(self.matches) > 10:
                    return None
        return True

    def complete(self, text, state):
        if state == 0:
            self.matches = []
            if text and text.startswith('#'):
                if not self.complete_tags(text):
                    return None
            else:
                line = readline.get_line_buffer()
                sline = line.lstrip()
                if sline.startswith('pra') and text.startswith('pra'):
                    self.matches.append('practice')
                elif sline.startswith('s '):
                    if not self.complete_words(text, line):
                        return None
                elif sline.startswith('rm '):
                    if not self.complete_words(text, line):
                        return None
                elif sline.startswith('#'):
                    if not self.complete_words(text, line):
                        return None
                elif sline.startswith('e '):
                    if not self.complete_rwords(text, line):
                        return None
                elif sline.startswith('cd ') or sline.startswith('ls ') or sline.startswith('practice '):
                    if not self.complete_courses(text):
                        return None
                elif sline.startswith('p'):
                    if not self.complete_phrases(sline[1:].lstrip()):
                        return None
                elif sline.startswith('>'):
                    if sline.find('=') == -1:
                        if not self.complete_phrases(sline[1:].lstrip()):
                            return None
                    elif sline.find('-=') != -1:
                        idx = line.find('-=')
                        line = line[idx+2:]
                        if not self.complete_reverse_phrases(line.lstrip()):
                            return None
                elif sline.startswith('<'):
                    if sline.find('=') == -1:
                        if not self.complete_reverse_phrases(sline[1:].lstrip()):
                            return None

        try:
            return self.matches[state]
        except IndexError:
            return None

    @classmethod
    def load_json(cls, input_file):
        if input_file != ':memory':
            try:
                with open(input_file, 'r') as input_file:
                    return json.load(input_file)
            except:
                print("Couldn't read the file:", input_file)
        return {
            'words': {},
            'rwords': {},
            'tags': {},
            'p2p': {},
            'rp2p': {},
            'phrases': {},
            'courses': {},
        }

    def save(self):
        if self.word_bank_path != ':memory':
            with open(self.word_bank_path, 'w') as output_file:
                json.dump(self.bank, output_file, indent=2)

