import json
import os.path
from words import Words
import unittest

class WordBank():
    MEMORY_FILE = '/proc/espanol/memory'

    def __init__(self, path = MEMORY_FILE):
        if not path:
            self.word_bank_path = WordBank.MEMORY_FILE
        else:
            self.word_bank_path = path

        self.load(self.word_bank_path)

    def load(self, path):
        try:
            with open(path, 'r') as input_file:
                self.data = json.load(input_file)
                self.path = path
        except:
            if path != WordBank.MEMORY_FILE:
                print("Couldn't read the file:", path)
            else:
                self.path = WordBank.MEMORY_FILE
            self.data = {
                'words': {},
                'rwords': {},
                'tags': {},
                'p2p': {},
                'rp2p': {},
                'phrases': {},
                'courses': {},
            }

        self.words = Words(self)
        self.name = os.path.basename(path)

    def save(self):
        if self.path != WordBank.MEMORY_FILE:
            with open(self.word_bank_path, 'w') as output_file:
                json.dump(self.data, output_file, indent=2)


class Testing(unittest.TestCase):
    def test_basics(self):
        bank = WordBank()
        assert bank.name == 'memory'
        assert bank.words.count == 0


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_basics"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

