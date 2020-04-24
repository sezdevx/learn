
from tag import Tag
from word import Word

import random

class Question():
    def __init__(self, word, words, course):
        self.word = Word(word, course.bank)
        self.answer = self.word.get_meanings()[0]
        self.course = course
        self.words = random.sample(words, len(words))
        self.choices = []
        for w in self.words:
            if w not in self.word.get_list_attrib('s'):
                word = Word(w, course.bank)
                if word.questionable:
                    self.choices.append(word.get_meanings()[0])
                    if len(self.choices) == 3:
                        break
        self.choices.append(self.answer)
        random.shuffle(self.choices)


class Practice():

    def __init__(self, course, limit = -1):
        words = course.words
        self.course = course
        self.words = random.sample(words, len(words))
        self.phrase_ids = course.phrase_ids
        self.current = 0
        if limit == -1:
            self.limit = len(self.words)
        else:
            self.limit = limit
        self.iter = iter(self.words)

    def __iter__(self):
        self.current = 0
        self.iter = iter(self.words)
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            try:
                key = next(self.iter)
            except StopIteration:
                self.iter = iter(self.words)
                key = next(self.iter)
            question_type = random.randint(1, 3)
            if question_type == 1:
                return Question(key, self.words, self.course)
            elif question_type == 2:
                return Question(key, self.words, self.course)
            else:
                return Question(key, self.words, self.course)
        raise StopIteration




class Course():

    def practice(self, limit = -1):
        return Practice(self, limit)

    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.courses = bank.courses
        self.node = self.courses.get(name, None)
        self.history = []

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()

    def add_to_history(self, word):
        if len(self.history) > 100:
            self.history.pop(0)
        self.history.append(word)

    @property
    def tag_count(self):
        if not self.exists:
            return 0
        return len(self.node['t'])

    @property
    def phrase_count(self):
        if not self.exists:
            return 0
        return len(self.node['p'])

    @property
    def word_count(self):
        if not self.exists:
            return 0
        return len(self.node['w'])

    @property
    def total_word_count(self):
        if not self.exists:
            return 0
        r = set()
        for t in self.node['t']:
            tag = Tag(t, self.bank)
            for w in tag.words:
                r.add(w)
        for w in self.node['w']:
            r.add(w)
        return len(r)

    @property
    def words(self):
        if self.exists:
            return self.node['w']
        else:
            return []

    @property
    def tags(self):
        if self.exists:
            return self.node['t']
        else:
            return []

    @property
    def phrase_ids(self):
        if self.exists:
            return self.node['p']
        else:
            return []

    @property
    def exists(self):
        return self.node != None

    def create(self):
        if not self.exists:
            self.courses[self.name] = {'w': [], 'p': [], 't': []}
            self.node = self.courses[self.name]

    def add_word(self, word):
        if not self.exists:
            self.create()
        if word not in self.node['w']:
            self.node['w'].append(word)

    def remove_word(self, word):
        if self.exists:
            if word in self.node['w']:
                self.node['w'].remove(word)

    def add_tag(self, tag):
        if not self.exists:
            self.create()
        if tag not in self.node['t']:
            self.node['t'].append(tag)

    def remove_tag(self, tag):
        if self.exists:
            if tag in self.node['t']:
                self.node['t'].remove(tag)

    def add_phrase(self, pid):
        if not self.exists:
            self.create()
        if pid not in self.node['p']:
            self.node['p'].append(pid)

    def remove_phrase(self, pid):
        if self.exists:
            if pid in self.node['p']:
                self.node['p'].remove(pid)

