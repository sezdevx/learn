import json
import os.path
from words import Words
from tags import Tags
from courses import Courses
import unittest

class WordBank():
    MEMORY_FILE = '/proc/espanol/memory'

    def change_course(self, course):
        if course:
            self.course = course
        else:
            self.course = None

    def __init__(self, path = MEMORY_FILE):
        self.load(path)
        self.course = None

    def load(self, path):
        try:
            self.path = path
            with open(path, 'r') as input_file:
                self.data = json.load(input_file)
        except:
            if path != WordBank.MEMORY_FILE:
                print("Couldn't read the file:", path)
            else:
                self.path = WordBank.MEMORY_FILE
            self.data = {
                'words': {},
                'rwords': {},
                'letters': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                            'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                            't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú'],
                'tags': {},
                'phrases': {
                    'p2r': {},
                    'r2p' : {},
                    'ids' : {},
                    'last_id': 0
                },
                'courses': {},
            }

        if not 'letters' in self.data:
            self.data['letters'] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                                  'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
                                  't', 'u', 'v', 'w', 'x', 'y', 'z', 'á', 'é', 'í', 'ó', 'ú']


        self.words = Words(self)
        self.tags = Tags(self)
        self.courses = Courses(self)
        self.name = os.path.basename(path)

    def summary(self):
        return str(len(self.words)) + " w"

    def save(self):
        if self.path != WordBank.MEMORY_FILE:
            with open(self.path, 'w') as output_file:
                json.dump(self.data, output_file, indent=2)

class Testing(unittest.TestCase):
    def test_basics(self):
        bank = WordBank()
        assert bank.name == 'memory'
        assert len(bank.words) == 0


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_basics"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

