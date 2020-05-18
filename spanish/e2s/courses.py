from enum import Enum
from bank_utils import VocabError
import unittest
import datetime


class Course():

    def __init__(self, bank, name):
        self.bank = bank
        self.name = name
        self.courses = bank.data['courses']
        self.node = self.courses.get(self.name, None)

    def create(self):
        if not self.node:
            self.node = {'w': [], 't': [], 'p': []}
            self.courses[self.name] = self.node

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


class Courses():

    def __init__(self, bank):
        self.bank = bank

    def add_course(self, name):
        c = Course(name, self.bank)
        c.create()
        return c

    def get_course(self, name):
        return Course(name, self.bank)

    def delete_course(self, name):
        c = Course(name, self.bank)
        return c.delete()






