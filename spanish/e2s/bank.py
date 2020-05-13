import json
import os.path
from words import Words
import unittest

class WordBank():
    MEMORY_FILE = '/proc/espanol/memory'

    def __init__(self, path = MEMORY_FILE):
        self.load(path)

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
                'tags': {},
                'phrases': {
                    'p2r': {},
                    'r2p' : {},
                    'ids' : {},
                    'last_id': 0
                },
                'courses': {},
            }

        self.words = Words(self)
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

