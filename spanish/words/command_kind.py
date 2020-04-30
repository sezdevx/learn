from enum import Enum
from base_utils import LangUtils
from base_utils import InvalidCommandError
from base_utils import NotValidTagName
from base_utils import NotValidWordName
from tags import TagName
from tags import TagAttributes
from words import WordName
from words import WordAttributes

import unittest

class CommandKind(Enum):
    # rm > mi madre
    DELETE_PHRASE = 'delete-phrase'
    DELETE_TAG = 'delete-tag'
    DELETE_WORD = 'delete-word'

    # el padre = father, dad, daddy
    # el padre = priest
    MEANING_ASSIGN = 'meaning-assign'
    # padre -= father
    MEANING_REMOVE = 'meaning-remove'
    # el padre += father
    MEANING_APPEND = 'meaning-append'

    TAG_ASSIGN = 'tag-assign'
    TAG_REMOVE = 'tag-remove'
    TAG_APPEND = 'tag-append'

    PHRASE_ASSIGN = 'phrase-assign'
    PHRASE_REMOVE = 'phrase-remove'
    PHRASE_APPEND = 'phrase-append'

    S_COMMAND = 's-command'
    E_COMMAND = 'e-command'
    T_COMMAND = 't-command'
    P_COMMAND = 'p-command'
    R_COMMAND = 'r-command'
    PRACTICE_COMMAND = 'practice-command'

    CD_COMMAND = 'cd-command'
    LS_COMMAND = 'ls-command'

    CREATE_COURSE = 'create-course'
    PUT_IN_COURSE = 'put-in-course'

    #ERROR = 'error'
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
            raise InvalidCommandError("No value is provided: ")

        if not WordName.is_valid(word):
            raise NotValidWordName("Not a valid word name: " + word + " in '" + original + "'")

        name, meaning_idx, attribute, attribute_idx = tuple(WordName.parse_object_name(word))

        if attribute:
            if WordAttributes.is_list(attribute):
                values = LangUtils.dequote_and_split(value)
            else:
                values = [value]
        else:
            values = [a.strip() for a in value.split(',')]

        return [None, cmd_kind, name, meaning_idx, attribute, attribute_idx, values]


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
            raise InvalidCommandError("No value is provided: ")

        if not TagName.is_valid(tag):
            raise NotValidTagName("Not a valid tag name: " + tag + " in '" + original + "'")

        base_name, sub_name, word_idx, attrib, attrib_idx = tuple(TagName.parse_object_name(tag))

        if attrib:
            if TagAttributes.is_list(attrib):
                values = LangUtils.dequote_and_split(value)
            else:
                values = [value]
        else:
            values = [a.strip() for a in value.split(',')]

        return [None, cmd_kind, base_name, sub_name, word_idx, attrib, attrib_idx, values]

    @classmethod
    def remove_command(self, cmd):
        if cmd.startswith('>'): # rm > mi madre
            phrase = LangUtils.dequote(cmd[1:].strip())
            return [None, CommandKind.DELETE_PHRASE, phrase]
        elif cmd.startswith('#'): # rm #family, #another_one
            tags = [a.strip() for a in cmd.split(',')]
            tag_names = []
            for tag_name in tags:
                if not TagName.is_valid(tag_name):
                    raise NotValidTagName("Not a valid tag name: " + tag_name)
                tag_names.append(TagName.parse_object_name(tag_name))
            return [None, CommandKind.DELETE_TAG, tag_names]
        else: # rm el padre, la madre
            words = [a.strip() for a in cmd.split(',')]
            word_names = []
            for word_name in words:
                if not WordName.is_valid(word_name):
                    raise NotValidWordName("Not a valid word name: " + word_name)
                word_names.append(WordName.parse_object_name(word_name))

            return [None, CommandKind.DELETE_WORD, word_names]

    def do_parse_command(self, cmd, original):
        if cmd.startswith("rm "):
            return self.remove_command(cmd[2:].strip())
        elif cmd == "rm":
            raise InvalidCommandError("rm expects a parameter")
        elif cmd.startswith('#'):
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
                return self.meaning_assignment(original, cmd, '-=', CommandKind.MEANING_REMOVE)
            elif cmd.find('+=') != -1:
                return self.meaning_assignment(original, cmd, '+=', CommandKind.MEANING_APPEND)
            else:
                return self.meaning_assignment(original, cmd, '=', CommandKind.MEANING_ASSIGN)


    def parse_command(self, original):
        # remove any double space
        r = self.do_parse_command(' '.join(original.strip().split()), original)
        r[0] = original
        return r


class TestingSuite(unittest.TestCase):

    def check(self, commands):
        parser = CommandParser(None)
        for key in commands:
            r = parser.parse_command(key)
            commands[key][0] = key
            print(r)
            assert r == commands[key]

    def test_remove_command(self):
        commands = {
            "rm el padre": [None, CommandKind.DELETE_WORD, [['el padre', 0, None, 0]]],
            "rm el padre, la madre": [None, CommandKind.DELETE_WORD, [['el padre', 0, None, 0], ['la madre', 0, None, 0]]],
            "rm el padre:synonyms": [None, CommandKind.DELETE_WORD, [['el padre', 0, WordAttributes.SYNONYMS, 0]]],
            "rm padre:synonyms": [None, CommandKind.DELETE_WORD, [['padre', 0, WordAttributes.SYNONYMS, 0]]],
            "rm #family": [None, CommandKind.DELETE_TAG, [['family', '*', 0, None, 0]]],
            "rm #family[1]": [None, CommandKind.DELETE_TAG, [['family', '*', 1, None, 0]]],
            "rm #family:images": [None, CommandKind.DELETE_TAG, [['family', '*', 0, TagAttributes.IMAGES, 0]]],
            "rm #family-beginner:images": [None, CommandKind.DELETE_TAG, [['family', 'beginner', 0, TagAttributes.IMAGES, 0]]],
            "rm #family-beginner:IMAGES, #family-advanced": [None, CommandKind.DELETE_TAG, [['family', 'beginner', 0, TagAttributes.IMAGES, 0], ['family', 'advanced', 0, None, 0]]],
            "rm > mi padre": [None, CommandKind.DELETE_PHRASE, 'mi padre'],
        }
        self.check(commands)


    def test_meaning_assign_command(self):
        commands = {
            "el padre = father": [None, CommandKind.MEANING_ASSIGN, 'el padre', 0, None, 0, ['father']],
            "el padre -= father": [None, CommandKind.MEANING_REMOVE, 'el padre', 0, None, 0, ['father']],
            "el padre[1] += father": [None, CommandKind.MEANING_APPEND, 'el padre', 1, None, 0, ['father']],
            "el padre = father, dad": [None, CommandKind.MEANING_ASSIGN, 'el padre', 0, None, 0, ['father', 'dad']],
            "el padre:images = '/path/to/file.jpg'": [None, CommandKind.MEANING_ASSIGN, 'el padre', 0, WordAttributes.IMAGES, 0, ['/path/to/file.jpg']],
            "el padre:images = '/path/to/file.jpg', '/path/to/file2.jpg'": [None, CommandKind.MEANING_ASSIGN, 'el padre', 0, WordAttributes.IMAGES, 0, ['/path/to/file.jpg', '/path/to/file2.jpg']],
        }
        self.check(commands)

    def test_tag_assign_command(self):
        commands = {
            "#family el padre, la madre": [None, CommandKind.TAG_ASSIGN, 'family', '*', 0, None, 0, ['el padre', 'la madre']],
            "#family = el padre, la madre": [None, CommandKind.TAG_ASSIGN, 'family', '*', 0, None, 0, ['el padre', 'la madre']],
        }
        self.check(commands)


if __name__ == 'main':
    parser = CommandParser(None)
    while True:
        cmd = input("% ")
        if cmd == 'exit' or cmd == 'x':
            break
        r = parser.parse_command(cmd)
        print(r)

    test_suite = unittest.TestSuite()
    test_suite.addTest(TestingSuite("test_remove_command"))
    test_suite.addTest(TestingSuite("test_meaning_assign_command"))
    test_suite.addTest(TestingSuite("test_tag_assign_command"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)




    # def generic_assignment(self, cmd, symbol, cmd_kind, strip_quotes = False):
    #     idx = cmd.find(symbol)
    #     symbol_len = len(symbol)
    #
    #     if idx == 0 or idx == (len(cmd) - symbol_len):
    #         return [None, CommandKind.ERROR, "Invalid command"]
    #
    #     second = cmd[idx+symbol_len:].strip()
    #     first = cmd[:idx].strip()
    #
    #     if not first or not second:
    #         return [None, CommandKind.ERROR, "Invalid command"]
    #
    #     if strip_quotes:
    #         first = LangUtils.dequote(first)
    #         i = 0
    #         r = []
    #         in_phrase = False
    #         start = 0
    #         symbol = ""
    #         while i < len(second):
    #             if in_phrase:
    #                 if second[i] == symbol:
    #                     in_phrase = False
    #                     r.append(second[start:i].strip())
    #                     start = i + 1
    #             elif second[i] == '"' or second[i] == "'":
    #                 in_phrase = True
    #                 symbol = second[i]
    #                 start = i+1
    #             elif second[i] == ',' and start != i:
    #                 r.append(second[start:i].strip())
    #                 start = i+1
    #             i+=1
    #         if start < i:
    #             r.append(second[start:i].strip())
    #         return [None, cmd_kind, first, r]
    #     else:
    #         values = [a.strip() for a in second.split(',')]
    #         if first.find(':') != -1:
    #             i = 0
    #             while i < len(values):
    #                 values[i] = LangUtils.dequote(values[i])
    #                 i += 1
    #         return [None, cmd_kind, first, values]


    # elif cmd.startswith('['):
    #     # [el padre] mi padre = my father
    #     idx = cmd.find(']')
    #     if idx == -1:
    #         return [None, CommandKind.ERROR, 'Assissted words for a phrase is not closed by ]']
    #     words = [a.strip() for a in cmd[1:idx].split(',')]
    #     r = self.generic_assignment(cmd, '=', CommandKind.PHRASE_ASSIGN, True)
    #     r.append(words)
    #     return r
