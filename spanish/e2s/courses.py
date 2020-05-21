from enum import Enum
from bank_utils import VocabError
import unittest
import datetime


class Course():

    def __init__(self, name, bank):
        self.bank = bank
        self.name = name
        self.courses = bank.data['courses']
        self.node = self.courses.get(self.name, None)

    def clear(self):
        self.node = {'w': [], 't': [], 'p': []}
        self.courses[self.name] = self.node

    @property
    def word_count(self):
        w = len(self.node['w'])
        for t in self.node['t']:
            w += self.bank.tags[t].word_count
        return w

    @property
    def tag_count(self):
        return len(self.node['t'])

    @property
    def words(self):
        r = set()
        for w in self.node['w']:
            r.add(w)
        for t in self.node['t']:
            t = self.bank.tags[t]
            if t.exists:
                for w in t.words:
                    r.add(w)
        return r

    @property
    def tags(self):
        return self.node['t']

    def create(self):
        if not self.node:
            self.clear()

    def delete(self):
        if self.node:
            del self.courses[self.name]
            return True
        return False

    @property
    def exists(self):
        return self.node != None

    def put_words(self, words):
        if not self.exists:
            return
        for w in words:
            normalized = self.bank.words.normalize(w)
            if normalized and not normalized in self.node['w']:
                self.node['w'].append(normalized)

    def remove_words(self, words):
        if not self.exists:
            return
        for w in words:
            normalized = self.bank.words.normalize(w)
            if normalized and normalized in self.node['w']:
                self.node['w'].remove(normalized)

    def put_tags(self, tags):
        if not self.exists:
            return
        for t in tags:
            if self.bank.tags[t].exists and not t in self.node['t']:
                self.node['t'].append(t)

    def remove_tags(self, tags):
        if not self.exists:
            return
        for t in tags:
            if t in self.node['t']:
                self.node['t'].remove(t)


class CourseIterator():
    def __init__(self, bank):
        self.courses = bank.courses
        self.bank = bank
        self.current = 0
        self.it = iter(self.courses.courses)
        self.limit = len(self.courses.courses)

    def __iter__(self):
        self.current = 0
        self.limit = len(self.courses.courses)
        self.it = iter(self.courses.courses)
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current+=1
            return Course(next(self.it), self.bank)
        raise StopIteration


class Courses():

    def __len__(self):
        return len(self.courses)

    def __iter__(self):
        return CourseIterator(self.bank)

    def __init__(self, bank):
        self.bank = bank
        self.courses = bank.data['courses']

    def complete(self, name, matches):
        prefix = None
        if name.startswith('../') and self.bank.course:
            prefix = name[:3]
            name = name[3:]
        for w in self.courses:
            if w.startswith(name):
                if self.bank.course and w == self.bank.course.name:
                    continue
                if prefix:
                    w = prefix + w
                matches.append(w)
                if len(matches) > 10:
                    return None

        return matches

    def add_course(self, name):
        c = Course(name, self.bank)
        c.create()
        return c

    def get_course(self, name):
        if name in self.courses:
            return Course(name, self.bank)
        else:
            return None

    def delete_course(self, name):
        c = Course(name, self.bank)
        return c.delete()

