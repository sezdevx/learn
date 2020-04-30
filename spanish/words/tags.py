import re
import unittest
from enum import Enum
from base_utils import NotValidTagName

class TagAttributes(Enum):
    IMAGES = 'images'

    @classmethod
    def is_list(cls, attrib):
        return (attrib == TagAttributes.IMAGES
                )


class TagName():
    name_regex = re.compile(r'^#\w[\d\w_]*(-[\w\d_]+)?((\[\d+\])?|(:\w+)?(\[\d+\])?)$')

    @classmethod
    def is_valid(cls, name):
        return TagName.name_regex.match(name)

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
                word_idx = int(name[idx+1:-1])
                name = name[:idx]
        else:
            attrib = name[idx+1:]
            name = name[:idx]
            if name.endswith(']'):
                idx = name.find('[')
                word_idx = int(name[idx+1:-1])
                name = name[:idx]
            if attrib.endswith(']'):
                idx = attrib.find('[')
                attrib_idx = int(name[:idx])
                attrib = attrib[:idx]

        if attrib:
            for a in TagAttributes:
                if a.value.startswith(attrib):
                    attrib = a
                    break
            else:
                raise NotValidTagName("Not a valid tag attribute name: " + str(attrib) + " in " + tag_expr)

        idx = name.find('-')
        if idx != -1:
            sub_name = name[idx+1:]
            base_name = name[:idx]
        else:
            sub_name = '*'
            base_name = name

        if attrib and not TagAttributes.is_list(attrib) and attrib_idx != 0:
            raise NotValidTagName("Not a list attribute: " + attrib + " in " + tag_expr)

        if word_idx != 0 and attrib:
            raise NotValidTagName("Can not provide word index and an attribute in this expression: " + tag_expr)

        return [base_name, sub_name, word_idx, attrib, attrib_idx]

class Tag():
    pass


class TestingSuite(unittest.TestCase):
    def test_is_valid(self):
        assert TagName.is_valid("#family")
        assert TagName.is_valid("#family:files")
        assert TagName.is_valid("#family-beginner")
        assert TagName.is_valid("#family-beginner:files")
        assert TagName.is_valid("#family-beginner[1]")
        assert TagName.is_valid("#family[1]")
        assert TagName.is_valid("#family-beginner:files[1]")
        assert TagName.is_valid("#family:files")
        assert TagName.is_valid("#family-1")

        assert not TagName.is_valid("fam#ily")
        assert not TagName.is_valid("[1]#family")
        assert not TagName.is_valid("#family  [1]")
        assert not TagName.is_valid("#family-")
        assert not TagName.is_valid("#family -files")
        assert not TagName.is_valid("#family-files ")
        assert not TagName.is_valid(" #family-files ")
        assert not TagName.is_valid("#family-beginner[1]:files")

if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestingSuite("test_is_valid"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
