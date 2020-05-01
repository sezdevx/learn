from enum import Enum
from bank_utils import VocabError
import unittest
import re

class InvalidTagObjName(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message

class TagAttribs(Enum):
    IMAGES = 'images'

    @classmethod
    def is_list(cls, attrib):
        return (attrib == TagAttribs.IMAGES
                )

class TagObjName():
    # #family-beginner[1]
    # #family-beginner:images[1]
    name_regex = re.compile(r'^#\w[\d\w_]*(-[\w\d_]+)?((\[\d+\])?|(:\w+)?(\[\d+\])?)$')

    @classmethod
    def is_valid(cls, name):
        return TagObjName.name_regex.match(name)

    @classmethod
    def parse_object_name(cls, tag_expr):
        name = tag_expr[1:].lower()
        word_idx = 0
        attrib = None
        attrib_idx = 0
        idx = name.find(':')
        if idx == -1:
            if name.endswith(']'):
                idx = name.find('[')
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid word index: " + str + " in " + tag_expr)
                word_idx = int(name[idx+1:-1])
                name = name[:idx]
        else:
            attrib = name[idx+1:]
            name = name[:idx]
            if name.endswith(']'):
                idx = name.find('[')
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid word index: " + str + " in " + tag_expr)
                word_idx = int(str)
                name = name[:idx]
            if attrib.endswith(']'):
                idx = attrib.find('[')
                str = attrib[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid attribute index: " + str + " in " + tag_expr)
                attrib_idx = int(str)
                attrib = attrib[:idx]

        if attrib:
            for a in TagAttribs:
                if a.value.startswith(attrib):
                    attrib = a
                    break
            else:
                raise InvalidTagObjName("Not a valid tag attribute name: " + attrib + " in " + tag_expr)

        idx = name.find('-')
        if idx != -1:
            sub_name = name[idx+1:]
            base_name = name[:idx]
        else:
            sub_name = '*'
            base_name = name

        if attrib and not TagAttribs.is_list(attrib) and attrib_idx != 0:
            raise InvalidTagObjName("Not a list attribute: " + attrib + " in " + tag_expr)

        if word_idx != 0 and attrib:
            raise InvalidTagObjName("Can not provide word index and an attribute in this expression: " + tag_expr)

        return [base_name, sub_name, word_idx, attrib, attrib_idx]


class Testing(unittest.TestCase):
    def test_tag_obj_name_parse(self):
        assert TagObjName.parse_object_name("#family") == ["family", '*', 0, None, 0]
        assert TagObjName.parse_object_name("#family-beginner") == ["family", 'beginner', 0, None, 0]
        assert TagObjName.parse_object_name("#family-beginner[1]") == ["family", 'beginner', 1, None, 0]
        assert TagObjName.parse_object_name("#family-beginner:images") == ["family", 'beginner', 0, TagAttribs.IMAGES, 0]
        assert TagObjName.parse_object_name("#family-beginner:images[1]") == ["family", 'beginner', 0, TagAttribs.IMAGES, 1]
        try:
            assert TagObjName.parse_object_name("#family-beginner[1]:images") == ["family", 'beginner', 0, TagAttribs.IMAGES, 1]
        except InvalidTagObjName as e:
            assert e.message == "Can not provide word index and an attribute in this expression: #family-beginner[1]:images"



if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_tag_obj_name_parse"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

