from enum import Enum
import unittest
from tags import *
from words import *
from bank_utils import VocabError
from bank_utils import BankUtils

class InvalidCommandError(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message

class CommandKind(Enum):
    WORD_DELETE = 'word-obj-delete'
    WORD_LOOKUP = 'word-obj-lookup'
    WORD_ASSIGN = 'word-obj-assign'
    WORD_REMOVE = 'word-obj-remove'
    WORD_APPEND = 'word-obj-append'

    TAG_DELETE = 'tag-obj-delete'
    TAG_LOOKUP = 'tag-obj-lookup'
    TAG_ASSIGN = 'tag-obj-assign'
    TAG_REMOVE = 'tag-obj-remove'
    TAG_APPEND = 'tag-obj-append'

    SAVE = 'save'
    EXIT = 'exit'

class CommandParser():
    def __init__(self, bank):
        self.bank = bank

    def word_lookup(self, original, cmd):
        pass

    def tag_lookup(self, original, cmd):
        pass

    def tag_delete(self, original, cmd):
        pass

    def word_delete(self, original, cmd):
        pass

    def meaning_assignment(self, original, cmd, symbol, cmd_kind):
        idx = cmd.find(symbol)
        symbol_len = len(symbol)

        if idx == 0 or idx == (len(cmd) - symbol_len):
            raise InvalidCommandError("Invalid command: " + original)

        value = cmd[idx+symbol_len:].strip()
        word = cmd[:idx].strip()

        if not value:
            raise InvalidCommandError("No value is provided: " + original)

        if not WordObjName.is_valid(word):
            raise InvalidWordObjName("Not a valid word name: " + word + " in '" + original + "'")

        name, meaning_idx, attribute, attribute_idx = tuple(WordObjName.parse_object_name(word))

        if attribute:
            if WordAttribs.is_list(attribute):
                values = BankUtils.dequote_and_split(value)
            else:
                values = [value]
            if attribute_idx != 0 and cmd_kind != CommandKind.WORD_ASSIGN:
                raise InvalidCommandError("Can not remove or append to an attribute value: " + original)
        else:
            values = [a.strip() for a in value.split(',')]


        return [cmd_kind, name, meaning_idx, attribute, attribute_idx, values]


    def tag_assignment(self, original, cmd, symbol, cmd_kind):
        idx = cmd.find(symbol)
        if idx == -1:
            raise InvalidCommandError("Invalid tag command " + original)

        symbol_len = len(symbol)

        if idx == 0 or idx == (len(cmd) - symbol_len):
            raise InvalidCommandError("Invalid command: " + original)

        value = cmd[idx+symbol_len:].strip()
        tag = cmd[:idx].strip()

        if not value:
            raise InvalidCommandError("No value is provided: " + original)

        if not TagObjName.is_valid(tag):
            raise InvalidTagObjName("Not a valid tag name: " + tag + " in '" + original + "'")

        base_name, sub_name, word_idx, attrib, attrib_idx = tuple(TagObjName.parse_object_name(tag))

        if attrib:
            if TagAttribs.is_list(attrib):
                values = BankUtils.dequote_and_split(value)
            else:
                values = [value]
        else:
            values = [a.strip() for a in value.split(',')]

        return [cmd_kind, base_name, sub_name, word_idx, attrib, attrib_idx, values]

    def parse_command(self, original):
        # remove any double space
        cmd = ' '.join(original.strip().split())
        if cmd.startswith('#'):
            # tag
            if cmd.find('-=') != -1:
                return self.tag_assignment(original, cmd, '-=', CommandKind.TAG_REMOVE)
            elif cmd.find('+=') != -1:
                return self.tag_assignment(original, cmd, '+=', CommandKind.TAG_APPEND)
            elif cmd.find('=') != -1:
                return self.tag_assignment(original, cmd, '=', CommandKind.TAG_ASSIGN)
            else:
                idx = cmd.find(' ')
                if idx == -1:
                    return self.tag_lookup(original, cmd)
                else:
                    cmd = cmd[:idx] + ' = ' + cmd[idx+1:]
                    return self.tag_assignment(original, cmd, '=', CommandKind.TAG_ASSIGN)
        elif cmd.find("=") != -1:
            if cmd.find('-=') != -1:
                return self.meaning_assignment(original, cmd, '-=', CommandKind.WORD_REMOVE)
            elif cmd.find('+=') != -1:
                return self.meaning_assignment(original, cmd, '+=', CommandKind.WORD_APPEND)
            else:
                return self.meaning_assignment(original, cmd, '=', CommandKind.WORD_ASSIGN)

        elif cmd.startswith('rm '):
            cmd = cmd[3:]
            if cmd.startswith('#'):
                return self.tag_delete(original, cmd)
            # elif cmd.startswith('>'):
            #     return self.delete_phrase(original, cmd[1:].strip())
            else:
                return self.word_delete(original, cmd)

        elif cmd.startswith('more '):
            cmd = cmd[5:]
            if cmd.startswith('#'):
                return self.tag_lookup(original, cmd)
            # elif cmd.startswith('>'):
            #     return self.phrase_lookup(original, cmd[1:].strip())
            else:
                return self.word_lookup(original, cmd)

        # elif cmd.count(' ') > 3:
        #     return self.phrase_lookup(original, cmd)
        else:
            return self.word_lookup(original, cmd)

class Testing(unittest.TestCase):
    def check(self, commands):
        parser = CommandParser(None)
        for key in commands:
            r = parser.parse_command(key)
            assert r == commands[key]

    def test_meaning_assignment(self):
        commands = {
            "el padre = father": [CommandKind.WORD_ASSIGN, "el padre", 0, None, 0, ["father"]],
            "el padre=father": [CommandKind.WORD_ASSIGN, "el padre", 0, None, 0, ["father"]],
            "el padre[1]=father": [CommandKind.WORD_ASSIGN, "el padre", 1, None, 0, ["father"]],
            "el padre +=father": [CommandKind.WORD_APPEND, "el padre", 0, None, 0, ["father"]],
            "el padre -=father": [CommandKind.WORD_REMOVE, "el padre", 0, None, 0, ["father"]],
            "el padre-=father": [CommandKind.WORD_REMOVE, "el padre", 0, None, 0, ["father"]],
            "el padre[1]:IMAGES = '/path/to/image.file'": [CommandKind.WORD_ASSIGN, "el padre", 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
            "el padre[1]:IMAGES -= '/path/to/image.file'": [CommandKind.WORD_REMOVE, "el padre", 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
            "el padre[1]:IMAGES += '/path/to/image.file'": [CommandKind.WORD_APPEND, "el padre", 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
        }
        parser = CommandParser(None)

        try:
            r = parser.parse_command("el padre[1]:IMAGES[1] -= '/path/to/image.file'")
            assert r == [CommandKind.WORD_REMOVE, "el padre", 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']]
        except InvalidCommandError as e:
            assert e.message == "Can not remove or append to an attribute value: el padre[1]:IMAGES[1] -= '/path/to/image.file'"
        self.check(commands)

    def test_tag_assignment(self):
        commands = {
            "#family el padre": [CommandKind.TAG_ASSIGN, "family", '*', 0, None, 0, ["el padre"]],
            "#family-beginner el padre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 0, None, 0, ["el padre"]],
            "#family-beginner[1] el padre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 1, None, 0, ["el padre"]],
            "#family-beginner = el padre, la madre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 0, None, 0, ["el padre", "la madre"]],
        }
        parser = CommandParser(None)

        try:
            r = parser.parse_command("#family-beginner[1]:IMAGES el padre")
            assert r == [CommandKind.TAG_ASSIGN, "family", 'beginner', 1, TagAttribs.IMAGES, 0, ["el padre"]]
        except InvalidTagObjName as e:
            assert e.message == "Not a valid tag name: #family-beginner[1]:IMAGES in '#family-beginner[1]:IMAGES el padre'"
            self.check(commands)



if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_meaning_assignment"))
    test_suite.addTest(Testing("test_tag_assignment"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
