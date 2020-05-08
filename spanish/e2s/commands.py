from enum import Enum
import unittest
from tags import TagAttribs
from tags import TagObjName
from tags import InvalidTagObjName
from words import WordAttribs
from words import WordObjName
from words import WordKind
from words import InvalidWordObjName
from bank_utils import VocabError
from bank_utils import BankUtils

class InvalidCommandError(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message

class CommandKind(Enum):
    REVERSE_WORD_LOOKUP = 'reverse-word-lookup'

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

    PHRASE_LOOKUP = 'phrase-lookup'
    REVERSE_PHRASE_LOOKUP = 'reverse-phrase-lookup'

    COURSE_LOOKUP = 'course-lookup'
    COURSE_DELETE = 'course-delete'
    COURSE_CREATE = 'course-create'
    COURSE_CHANGE = 'course-change'

    SAVE = 'save'
    EXIT = 'exit'

class CommandParser():
    def __init__(self, bank):
        self.bank = bank

    def reverse_word_lookup(self, original, cmd, options):
        words = [a.strip() for a in cmd.split(',')]
        return [CommandKind.REVERSE_WORD_LOOKUP, options, words]

    def word_lookup(self, original, cmd, options):
        words = [a.strip() for a in cmd.split(',')]
        r = []
        for word in words:
            if not WordObjName.is_valid(word):
                raise InvalidWordObjName("Not a valid word name: " + word + " in '" + original + "'")
            r.append(WordObjName.parse_object_name(word))

        return [CommandKind.WORD_LOOKUP, options,  r]

    def word_delete(self, original, cmd, options):
        words = [a.strip() for a in cmd.split(',')]
        r = []
        for word in words:
            if not WordObjName.is_valid(word):
                raise InvalidWordObjName("Not a valid word name: " + word + " in '" + original + "'")
            r.append(WordObjName.parse_object_name(word))

        return [CommandKind.WORD_DELETE, options, r]

    def tag_lookup(self, original, cmd, options):
        tags = [a.strip() for a in cmd.split(',')]
        r = []
        for tag in tags:
            if not TagObjName.is_valid(tag):
                raise InvalidTagObjName("Not a valid tag name: " + tag + " in '" + original + "'")
            r.append(TagObjName.parse_object_name(tag))

        return [CommandKind.TAG_LOOKUP, options, r]

    def tag_delete(self, original, cmd, options):
        if cmd.find(',') != -1:
            tags = [a.strip() for a in cmd.split(',')]
        else:
            tags = [a.strip() for a in cmd.split(' ')]
        r = []
        for tag in tags:
            if not TagObjName.is_valid(tag):
                raise InvalidTagObjName("Not a valid tag name: " + tag + " in '" + original + "'")
            r.append(TagObjName.parse_object_name(tag))

        return [CommandKind.TAG_DELETE, options, r]

    def reverse_phrase_lookup(self, original, cmd, options):
        return [CommandKind.REVERSE_PHRASE_LOOKUP, options, cmd]

    def phrase_lookup(self, original, cmd, options):
        return [CommandKind.PHRASE_LOOKUP, options, cmd]

    def phrase_delete(self, original, cmd, options):
        return [CommandKind.PHRASE_DELETE, options, cmd]

    def course_lookup(self, original, cmd, options):
        return [CommandKind.COURSE_LOOKUP, options, cmd]

    def course_delete(self, original, cmd, options):
        return [CommandKind.COURSE_DELETE, options, cmd]

    def course_create(self, original, cmd, options):
        return [CommandKind.COURSE_CREATE, options, cmd]

    def course_change(self, original, cmd, options):
        return [CommandKind.COURSE_CHANGE, options, cmd]

    def word_assignment(self, original, cmd, symbol, cmd_kind, kind = WordKind.Unknown):
        idx = cmd.find(symbol)
        symbol_len = len(symbol)

        if idx == 0 or idx == (len(cmd) - symbol_len):
            raise InvalidCommandError("Invalid command: " + original)

        value = cmd[idx+symbol_len:].strip()
        word = cmd[:idx].strip()

        if not WordObjName.is_valid(word):
            raise InvalidWordObjName("Not a valid word name: " + word + " in '" + original + "'")

        name, mkind, meaning_idx, attribute, attribute_idx = tuple(WordObjName.parse_object_name(word))

        if mkind != WordKind.Unknown:
            if kind == WordKind.Unknown:
                kind = mkind
            elif kind != mkind:
                raise VocabError("Mismatched kind for : " + word + " in " + original)

        if attribute:
            if WordAttribs.is_list(attribute):
                values = BankUtils.dequote_and_split(value)
            else:
                values = [value]
            if attribute_idx != 0 and cmd_kind != CommandKind.WORD_ASSIGN:
                raise InvalidCommandError("Can not remove or append to an attribute value: " + original)
        else:
            values = [a.strip() for a in value.split(',')]


        return [cmd_kind, name, kind, meaning_idx, attribute, attribute_idx, values]


    def tag_assignment(self, original, cmd, symbol, cmd_kind):
        idx = cmd.find(symbol)
        if idx == -1:
            raise InvalidCommandError("Invalid tag command " + original)

        symbol_len = len(symbol)

        if idx == 0 or idx == (len(cmd) - symbol_len):
            raise InvalidCommandError("Invalid command: " + original)

        value = cmd[idx+symbol_len:].strip()
        tag = cmd[:idx].strip()

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
                    return self.tag_lookup(original, cmd, "")
                else:
                    cmd = cmd[:idx] + ' = ' + cmd[idx+1:]
                    return self.tag_assignment(original, cmd, '=', CommandKind.TAG_ASSIGN)

        elif cmd.startswith('('):
            idx = cmd.find(')')
            if idx == -1:
                raise InvalidCommandError("Not closed parentheses: " + original)
            kind = WordKind.parse(cmd[1:idx].strip())
            cmd = cmd[idx+1:]
            if cmd.find('-=') != -1:
                return self.word_assignment(original, cmd, '-=', CommandKind.WORD_REMOVE, kind)
            elif cmd.find('+=') != -1:
                return self.word_assignment(original, cmd, '+=', CommandKind.WORD_APPEND, kind)
            else:
                return self.word_assignment(original, cmd, '=', CommandKind.WORD_ASSIGN, kind)

        elif cmd.find("=") != -1:
            if cmd.find('-=') != -1:
                return self.word_assignment(original, cmd, '-=', CommandKind.WORD_REMOVE)
            elif cmd.find('+=') != -1:
                return self.word_assignment(original, cmd, '+=', CommandKind.WORD_APPEND)
            else:
                return self.word_assignment(original, cmd, '=', CommandKind.WORD_ASSIGN)

        elif cmd.startswith('mkdir '):

            return self.course_create(original, cmd[6:], "")

        elif cmd.startswith('cd '):

            return self.course_change(original, cmd[3:], "")

        elif cmd.startswith('rm '):
            cmd = cmd[3:]
            options = ""
            if cmd.startswith('-'):
                idx = cmd.find(' ')
                if idx == -1:
                    raise InvalidCommandError("More requires an argument: " + original)
                options = cmd[1:idx]
                cmd = cmd[idx+1]

            if cmd.startswith('#'):
                return self.tag_delete(original, cmd, options)
            elif cmd.startswith('$'):
                return self.course_delete(original, cmd[1:].strip(), options)
            elif cmd.startswith('>'):
                return self.phrase_delete(original, cmd[1:].strip(), options)
            else:
                return self.word_delete(original, cmd, options)

        elif cmd.startswith('more '):
            cmd = cmd[5:]
            options = ""
            if cmd.startswith('-'):
                idx = cmd.find(' ')
                if idx == -1:
                    raise InvalidCommandError("More requires an argument: " + original)
                options = cmd[1:idx]
                cmd = cmd[idx+1]

            if cmd.startswith('#'):
                return self.tag_lookup(original, cmd, options)
            elif cmd.startswith('$'):
                return self.course_lookup(original, cmd[1:].strip(), options)
            elif cmd.startswith('>'):
                return self.phrase_lookup(original, cmd[1:].strip(), options)
            elif cmd.startswith('<'):
                return self.reverse_phrase_lookup(original, cmd[1:].strip(), options)
            elif cmd.startswith('?'):
                return self.reverse_word_lookup(original, cmd[1:].strip(), options)
            else:
                return self.word_lookup(original, cmd, options)

        elif cmd.startswith('?'):

            return self.reverse_word_lookup(original, cmd[1:].strip(), "")

        elif cmd.startswith('<'):

            return self.reverse_phrase_lookup(original, cmd[1:].strip(), "")

        elif cmd.startswith('>'):

            return self.phrase_lookup(original, cmd[1:].strip(), "")

        else:

            space_count = cmd.count(' ')

            if space_count > 3:
                return self.phrase_lookup(original, cmd, "")
            elif space_count == 3:
                if cmd.startswith('el ') or cmd.startswith('los ') or cmd.startswith('la ') or cmd.startswith('las '):
                    return self.word_lookup(original, cmd, "")
                else:
                    return self.phrase_lookup(original, cmd, "")
            else:
                return self.word_lookup(original, cmd, "")

class Testing(unittest.TestCase):
    def check(self, commands):
        parser = CommandParser(None)
        for key in commands:
            r = parser.parse_command(key)
            try:
                assert r == commands[key]
            except:
                print(r)
                print(commands[key])
                assert False


    def test_lookups(self):
        commands = {
            "el padre": [CommandKind.WORD_LOOKUP, "", [["padre", WordKind.Male, 0, None, 0]]],
            "mi madre es inteligente": [CommandKind.PHRASE_LOOKUP, "", 'mi madre es inteligente'],
        }
        self.check(commands)

    def test_word_assignment(self):
        commands = {
            "el padre = father": [CommandKind.WORD_ASSIGN, "padre", WordKind.Male, 0, None, 0, ["father"]],
            "el padre=father": [CommandKind.WORD_ASSIGN, "padre", WordKind.Male, 0, None, 0, ["father"]],
            "(adj) inteligente = intelligent": [CommandKind.WORD_ASSIGN, "inteligente", WordKind.Adjective, 0, None, 0, ["intelligent"]],
            "el padre[1]=father": [CommandKind.WORD_ASSIGN, "padre", WordKind.Male, 1, None, 0, ["father"]],
            "el padre +=father": [CommandKind.WORD_APPEND, "padre", WordKind.Male, 0, None, 0, ["father"]],
            "el padre -=father": [CommandKind.WORD_REMOVE, "padre", WordKind.Male, 0, None, 0, ["father"]],
            "el padre-=father": [CommandKind.WORD_REMOVE, "padre", WordKind.Male, 0, None, 0, ["father"]],
            "el padre[1]:IMAGES = '/path/to/image.file'": [CommandKind.WORD_ASSIGN, "padre", WordKind.Male, 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
            "el padre[1]:IMAGES -= '/path/to/image.file'": [CommandKind.WORD_REMOVE, "padre", WordKind.Male, 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
            "el padre[1]:IMAGES += '/path/to/image.file'": [CommandKind.WORD_APPEND, "padre", WordKind.Male, 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']],
        }
        self.check(commands)

        parser = CommandParser(None)
        try:
            r = parser.parse_command("el padre[1]:IMAGES[1] -= '/path/to/image.file'")
            assert r == [CommandKind.WORD_REMOVE, "padre", WordKind.Male, 1, WordAttribs.IMAGES, 0, ['/path/to/image.file']]
        except InvalidCommandError as e:
            assert e.message == "Can not remove or append to an attribute value: el padre[1]:IMAGES[1] -= '/path/to/image.file'"

        try:
            r = parser.parse_command("el padre&[1]:IMAGES[1] -= '/path/to/image.file'")
            assert r == [CommandKind.WORD_REMOVE, "padre&", 1, WordKind.Male, WordAttribs.IMAGES, 0, ['/path/to/image.file']]
        except InvalidWordObjName as e:
            assert e.message == "Not a valid word name: el padre&[1]:IMAGES[1] in 'el padre&[1]:IMAGES[1] -= '/path/to/image.file''"

        try:
            r = parser.parse_command("= '/path/to/image.file'")
            assert r == [CommandKind.WORD_REMOVE, "", WordKind.Unknown, 0, None, 0, ['/path/to/image.file']]
        except InvalidCommandError as e:
            assert e.message == "Invalid command: = '/path/to/image.file'"

        try:
            r = parser.parse_command("el padre =")
            assert r == [CommandKind.WORD_REMOVE, "padre", WordKind.Male, 0, None, 0, ['']]
        except InvalidCommandError as e:
            assert e.message == "Invalid command: el padre ="


    def test_tag_assignment(self):
        commands = {
            "#family el padre": [CommandKind.TAG_ASSIGN, "family", '*', 0, None, 0, ["el padre"]],
            "#family-beginner el padre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 0, None, 0, ["el padre"]],
            "#family-beginner[1] el padre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 1, None, 0, ["el padre"]],
            "#family-beginner = el padre, la madre": [CommandKind.TAG_ASSIGN, "family", 'beginner', 0, None, 0, ["el padre", "la madre"]],
        }
        self.check(commands)

        parser = CommandParser(None)
        try:
            r = parser.parse_command("#family-beginner[1]:IMAGES el padre")
            assert r == [CommandKind.TAG_ASSIGN, "family", 'beginner', 1, TagAttribs.IMAGES, 0, ["el padre"]]
        except InvalidTagObjName as e:
            assert e.message == "Not a valid tag name: #family-beginner[1]:IMAGES in '#family-beginner[1]:IMAGES el padre'"

        try:
            r = parser.parse_command("#family-beginner[1]:IMAGES el padre")
            assert r == [CommandKind.TAG_ASSIGN, "family", 'beginner', 1, TagAttribs.IMAGES, 0, ["el padre"]]
        except InvalidTagObjName as e:
            assert e.message == "Not a valid tag name: #family-beginner[1]:IMAGES in '#family-beginner[1]:IMAGES el padre'"

    def test_tag_delete(self):
        commands = {
            "rm #family": [CommandKind.TAG_DELETE, '', [["family", '*', 0, None, 0]]],
            "rm #family-beginner": [CommandKind.TAG_DELETE, '', [["family", 'beginner', 0, None, 0]]],
            "rm #family-beginner:IMAGES": [CommandKind.TAG_DELETE, '', [["family", 'beginner', 0, TagAttribs.IMAGES, 0]]],
            "rm #family-beginner[2]": [CommandKind.TAG_DELETE, '', [["family", 'beginner', 2, None, 0]]],
            "rm #family-beginner[2], #family-advanced:IMAGES": [CommandKind.TAG_DELETE, '', [["family", 'beginner', 2, None, 0], ["family", 'advanced', 0, TagAttribs.IMAGES, 0]]],
            "rm #family-beginner[2] #family-advanced:IMAGES": [CommandKind.TAG_DELETE, '', [["family", 'beginner', 2, None, 0], ["family", 'advanced', 0, TagAttribs.IMAGES, 0]]],
        }
        self.check(commands)

    def test_word_delete(self):
        commands = {
            "rm el padre": [CommandKind.WORD_DELETE, '', [["padre", WordKind.Male, 0, None, 0]]],
            "rm el padre[1]": [CommandKind.WORD_DELETE, '', [["padre", WordKind.Male, 1, None, 0]]],
            "rm el padre[1]:IMAGES": [CommandKind.WORD_DELETE, '', [["padre", WordKind.Male, 1, WordAttribs.IMAGES, 0]]],
            "rm el padre[1]:IMAGES, la madre": [CommandKind.WORD_DELETE, '', [["padre", WordKind.Male, 1, WordAttribs.IMAGES, 0], ["madre", WordKind.Female, 0, None, 0]]],
        }
        self.check(commands)


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_word_assignment"))
    test_suite.addTest(Testing("test_tag_assignment"))
    test_suite.addTest(Testing("test_lookups"))
    test_suite.addTest(Testing("test_tag_delete"))
    test_suite.addTest(Testing("test_word_delete"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)
