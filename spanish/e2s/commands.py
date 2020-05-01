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
    WORD_LOOKUP = 'word-obj-lookup'
    WORD_ASSIGN = 'word-obj-assign'
    WORD_REMOVE = 'word-obj-remove'
    WORD_APPEND = 'word-obj-append'

    TAG_LOOKUP = 'tag-obj-lookup'
    TAG_ASSIGN = 'tag-obj-assign'
    TAG_REMOVE = 'tag-obj-remove'
    TAG_APPEND = 'tag-obj-append'

    SAVE = 'save'
    EXIT = 'exit'

class CommandParser():
    def __init__(self, bank):
        self.bank = bank

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
            if cmd.find('-=') != -1:
                return self.tag_assignment(original, cmd, '-=', CommandKind.TAG_REMOVE)
            elif cmd.find('+=') != -1:
                return self.tag_assignment(original, cmd, '+=', CommandKind.TAG_APPEND)
            elif cmd.find('=') != -1:
                return self.tag_assignment(original, cmd, '=', CommandKind.TAG_ASSIGN)
            else:
                idx = cmd.find(' ')
                if idx == -1:
                    raise InvalidCommandError("Not a valid tag operation: " + original)
                cmd = cmd[:idx] + ' = ' + cmd[idx+1:]
                return self.tag_assignment(original, cmd, '=', CommandKind.TAG_ASSIGN)
        elif cmd.find("=") != -1:
            if cmd.find('-=') != -1:
                return self.meaning_assignment(original, cmd, '-=', CommandKind.WORD_REMOVE)
            elif cmd.find('+=') != -1:
                return self.meaning_assignment(original, cmd, '+=', CommandKind.WORD_APPEND)
            else:
                return self.meaning_assignment(original, cmd, '=', CommandKind.WORD_ASSIGN)

class Testing(unittest.TestCase):
    def test_meaning_assignment(self):

        pass


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_meaning_assignment"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
