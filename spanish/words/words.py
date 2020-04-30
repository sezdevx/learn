import re
import unittest
from enum import Enum
from base_utils import NotValidWordName
from word_kind import WordKind

class WordAttributes(Enum):
    SYNONYMS = 'synonyms'
    ANONYMS = 'anonyms'
    IMAGES = 'images'

    @classmethod
    def is_list(cls, attrib):
        return (attrib == WordAttributes.SYNONYMS or
                attrib == WordAttributes.ANONYMS or
                attrib == WordAttributes.IMAGES
                )

class WordName():
    name_regex = re.compile(r'^\w+(\s\w+)?(\s\w+)?(\s\w+)?(\[\d+\])?(:\w+)?(\[\d+\])?$')

    @classmethod
    def is_valid(cls, name):
        return WordName.name_regex.match(name)

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
                meaning_idx = int(name[idx+1:-1])
                name = name[:idx]
        else:
            attrib = name[idx+1:].lower()
            name = name[:idx]
            if name.endswith(']'):
                idx = name.find('[')
                meaning_idx = int(name[idx+1:-1])
                name = name[:idx]
            if attrib.endswith(']'):
                idx = attrib.find('[')
                attrib_idx = int(name[:idx])
                attrib = attrib[:idx]

        if attrib:
            for a in WordAttributes:
                if a.value.startswith(attrib):
                    attrib = a
                    break
            else:
                raise NotValidWordName("Not a valid word attribute: " + str(attrib) + " in "+ word)

        if attrib and not WordAttributes.is_list(attrib) and attrib_idx != 0:
            raise NotValidWordName("Not a list attribute: " + attrib + " in " + word)

        return [name, meaning_idx, attrib, attrib_idx]


class Word():
    pass


class TestingSuite(unittest.TestCase):
    def test_is_valid_word_name(self):
        assert WordName.is_valid("padre")
        assert WordName.is_valid("padre[1]")
        assert WordName.is_valid("el padre")
        assert WordName.is_valid("el fin de semana")
        assert WordName.is_valid("padre:files")
        assert WordName.is_valid("padre:files[1]")
        assert WordName.is_valid("padre:files[1]")
        assert WordName.is_valid("padre[1]:files[1]")


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestingSuite("test_is_valid_word_name"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
