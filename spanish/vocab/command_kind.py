from enum import Enum
import unittest

class CommandKind(Enum):
    # el padre = father, dad, daddy
    MEANING_ASSIGN = 'meaning-assign'
    MEANING_REMOVE = 'meaning-remove'
    MEANING_APPEND = 'meaning-append'

    MEANING_ATTR_ASSIGN = 'meaning-attrib-assign'
    MEANING_ATTR_REMOVE = 'meaning-attrib-remove'
    MEANING_ATTR_APPEND = 'meaning-attrib-append'

    TAG_ASSIGN = 'tag-assign'
    TAG_REMOVE = 'tag-remove'
    TAG_APPEND = 'tag-append'

    TAG_ATTR_ASSIGN = 'tag-attr-assign'
    TAG_ATTR_REMOVE = 'tag-attr-remove'
    TAG_ATTR_APPEND = 'tag-attr-append'

    PHRASE_ASSIGN = 'phrase-assign'
    PHRASE_REMOVE = 'phrase-remove'
    PHRASE_APPEND = 'phrase-append'

    PHRASE_ATTR_ASSIGN = 'phrase-attr-assign'
    PHRASE_ATTR_REMOVE = 'phrase-attr-remove'
    PHRASE_ATTR_APPEND = 'phrase-attr-append'

    S_COMMAND = 's-command'
    E_COMMAND = 'e-command'
    T_COMMAND = 't-command'
    P_COMMAND = 'p-command'
    R_COMMAND = 'r-command'
    PRACTICE_COMMAND = 'practice-command'

    CD_COMMAND = 'cd-command'
    LS_COMMAND = 'ls-command'

    DELETE_PHRASE = 'remove-phrase'
    DELETE_TAG = 'remove-tag'
    DELETE_WORD = 'remove-word'

    CREATE_COURSE = 'create-course'
    PUT_IN_COURSE = 'put-in-course'

    ERROR = 'error'
    SAVE = 'save'
    EXIT = 'exit'

    @classmethod
    def is_invalid_word(cls, name):
        return (name.find('+') != -1 or # name.find('-') != -1 or
                name.find('&') != -1 or name.find('%') != -1 or
                name.find('$') != -1 or name.find('{') != -1 or
                name.find('}') != -1 or name.find('^') != -1 or
                name.find('@') != -1 or name.find('!') != -1 or
                name.find('¡') != -1 or name.find('¿') != -1 or
                name.find('?') != -1 or name.find(':') != -1
                )

    @classmethod
    def generic_assignment(cls, cmd, original, symbol, kind1, kind2, strip_quotes = False):
        idx = cmd.find(symbol)
        symbol_len = len(symbol)

        if idx == 0 or idx == (len(cmd) - symbol_len):
            return [original, CommandKind.ERROR, "Invalid command"]

        second = cmd[idx+symbol_len:].strip()
        first = cmd[:idx].strip()

        if not isinstance(kind2, str):
            idx = first.rfind(':')
            if idx != -1:
                if idx == (len(first) - 1):
                    return [original, CommandKind.ERROR, "Invalid command"]
                attribute = first[idx+1:]
                object = first[:idx]
            else:
                object = first
                attribute = ''
        else:
            object = first
            attribute = kind2
            idx = first.rfind(':')
            if idx != -1:
                if idx == (len(first) - 1):
                    return [original, CommandKind.ERROR, "Invalid command"]
                attribute = first[idx+1:]
                if not kind2.startswith(attribute):
                    return [original, CommandKind.ERROR, "Invalid command"]
                else:
                    attribute = kind2
                object = first[:idx]
            kind2 = kind1

        if not first or not second:
            return [original, CommandKind.ERROR, "Invalid command"]

        if cls.is_invalid_word(object):
            return [original, CommandKind.ERROR, "Invalid word: " + object]
        if attribute and not attribute.isidentifier():
            return [original, CommandKind.ERROR, "Invalid attribute name: " + attribute]

        if strip_quotes:
            if object.startswith('"') or object.startswith("'"):
                symbol = object[0]
                if not object.endswith(symbol):
                    return [original, CommandKind.ERROR, "Invalid phrase quotation: " + object]
                object = object[1:-1]
            i = 0
            r = []
            in_phrase = False
            start = 0
            symbol = ""
            while i < len(second):
                if in_phrase:
                    if second[i] == symbol:
                        in_phrase = False
                        r.append(second[start:i].strip())
                        start = i + 1
                elif second[i] == '"' or second[i] == "'":
                    in_phrase = True
                    symbol = second[i]
                    start = i+1
                elif second[i] == ',' and start != i:
                    r.append(second[start:i].strip())
                    start = i+1
                i+=1
            if start < i:
                r.append(second[start:i].strip())
            if not attribute:
                return [original, kind1, object, r]
            else:
                return [original, kind2, object, attribute, r]
        else:
            if not attribute:
                return [original, kind1, object, [a.strip() for a in second.split(',')]]
            else:
                return [original, kind2, object, attribute, [a.strip() for a in second.split(',')]]

    @classmethod
    def s_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                return [original, CommandKind.ERROR, 'Invalid s command']
            options = cmd[1:idx]
            cmd = cmd[idx+1:]
        words = [a.strip() for a in cmd.split(',')]
        return [original, CommandKind.S_COMMAND, options, words]

    @classmethod
    def ls_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                options = cmd[1:]
                cmd = ""
            else:
                options = cmd[1:idx]
                cmd = cmd[idx+1:]
        return [original, CommandKind.LS_COMMAND, options, cmd]

    @classmethod
    def e_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                return [original, CommandKind.ERROR, 'Invalid e command']
            options = cmd[1:idx]
            cmd = cmd[idx+1:]
        words = [a.strip() for a in cmd.split(',')]
        return [original, CommandKind.E_COMMAND, options, words]

    @classmethod
    def t_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                return [original, CommandKind.ERROR, 'Invalid t command']
            options = cmd[1:idx]
            cmd = cmd[idx+1:].strip()
        if cmd.startswith("#"):
            cmd = cmd[1:]
        return [original, CommandKind.T_COMMAND, options, cmd]

    @classmethod
    def p_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                return [original, CommandKind.ERROR, 'Invalid p command']
            options = cmd[1:idx]
            cmd = cmd[idx+1:].strip()
        if cmd.startswith("'"):
            if not cmd.endswith("'"):
                return [original, CommandKind.ERROR, "Not closed phrase"]
            cmd = cmd[1:-1]
        elif cmd.startswith('"'):
            if not cmd.endswith('"'):
                return [original, CommandKind.ERROR, "Not closed phrase"]
            cmd = cmd[1:-1]
        return [original, CommandKind.P_COMMAND, options, cmd]

    @classmethod
    def r_command(cls, cmd, original):
        options = ""
        if cmd.startswith('-'):
            idx = cmd.find(' ')
            if idx == -1:
                return [original, CommandKind.ERROR, 'Invalid r command']
            options = cmd[1:idx]
            cmd = cmd[idx+1:].strip()
        if cmd.startswith("'"):
            if not cmd.endswith("'"):
                return [original, CommandKind.ERROR, "Not closed phrase"]
            cmd = cmd[1:-1]
        elif cmd.startswith('"'):
            if not cmd.endswith('"'):
                return [original, CommandKind.ERROR, "Not closed phrase"]
            cmd = cmd[1:-1]
        return [original, CommandKind.R_COMMAND, options, cmd]

    @classmethod
    def rm_command(cls, cmd, original):
        if cmd.startswith('>'):
            # rm > mi madre
            phrase = cmd[1:].strip()
            if phrase.startswith('"') or phrase.startswith("'"):
                symbol = phrase[0]
                if not phrase.endswith(symbol):
                    return [original, CommandKind.ERROR, "Invalid phrase removal"]
                phrase = phrase[1:-1].strip()
            return [original, CommandKind.DELETE_PHRASE, phrase]
        elif cmd.startswith('#'):
            # rm #family
            tag = cmd[1:].strip()
            if cmd.find(' ') != -1:
                return [original, CommandKind.ERROR, "You can only remove one tag at a time"]
            return [original, CommandKind.DELETE_TAG, tag]
        else:
            # rm el padre, la madre
            return [original, CommandKind.DELETE_WORD, [a.strip() for a in cmd.split(', ')]]

    @classmethod
    def parse_command(cls, original):
        # remove any double space
        cmd = ' '.join(original.strip().split())
        if cmd.startswith("rm "):
            return cls.rm_command(cmd[2:].strip(), original)
        if cmd.startswith("practice"):
            cmd = cmd[8:].strip()
            limit = -1
            if cmd.isnumeric():
                limit = int(limit)
            else:
                limit = -1
            return [original, CommandKind.PRACTICE_COMMAND, limit, cmd]
        elif cmd == 'exit' or cmd == 'quit':
            return [original, CommandKind.EXIT]
        elif cmd == 'save':
            return [original, CommandKind.SAVE]
        elif cmd == 'cd':
            return [original, CommandKind.CD_COMMAND, '']
        elif cmd.startswith('create '):
            return [original, CommandKind.CREATE_COURSE, cmd[7:].strip()]
        elif cmd.startswith('mkdir '):
            return [original, CommandKind.CREATE_COURSE, cmd[6:].strip()]
        elif cmd.startswith('put '):
            return [original, CommandKind.PUT_IN_COURSE, cmd[4:].strip()]
        elif cmd == 'ls':
            return [original, CommandKind.LS_COMMAND, '', '']
        elif cmd.startswith('ls '):
            return cls.ls_command(cmd[2:].strip(), original)
        elif cmd.startswith("cd "):
            return [original, CommandKind.CD_COMMAND, cmd[2:].strip()]
        elif cmd == 'e':
            return [original, CommandKind.ERROR, "e command requires at least one word"]
        elif cmd == 's':
            return [original, CommandKind.ERROR, "s command requires at least one word"]
        elif cmd.startswith("s "):
            return cls.s_command(cmd[2:].strip(), original)
        elif cmd.startswith("e "):
            return cls.e_command(cmd[2:].strip(), original)
        elif cmd.startswith("t "):
            return cls.t_command(cmd[2:].strip(), original)
        elif cmd.startswith("p "):
            return cls.p_command(cmd[2:].strip(), original)
        elif cmd.startswith("r "):
            return cls.r_command(cmd[2:].strip(), original)
        elif cmd.startswith('<'):
            return cls.r_command(cmd[1:].strip(), original)
        elif cmd.startswith('>'):
            cmd = cmd[1:].strip()
            if cmd.find("-~") != -1:
                return cls.generic_assignment(cmd, original, '-~', CommandKind.PHRASE_ATTR_REMOVE, 'related', True)
            elif cmd.find("+~") != -1:
                return cls.generic_assignment(cmd, original, '+~', CommandKind.PHRASE_ATTR_APPEND, 'related', True)
            elif cmd.find("~") != -1:
                return cls.generic_assignment(cmd, original, '~', CommandKind.PHRASE_ATTR_ASSIGN, 'related', True)
            elif cmd.find("+=") != -1:
                return cls.generic_assignment(cmd, original, '+=', CommandKind.PHRASE_APPEND, CommandKind.PHRASE_ATTR_APPEND, True)
            elif cmd.find("-=") != -1:
                return cls.generic_assignment(cmd, original, '-=', CommandKind.PHRASE_REMOVE, CommandKind.PHRASE_ATTR_REMOVE, True)
            elif cmd.find("=") != -1:
                words = []
                if cmd.startswith('['):
                    idx = cmd.find(']')
                    if idx == -1:
                        return [original, CommandKind.ERROR, 'Invalid assisted words']
                    words = [a.strip() for a in cmd[1:idx].split(',')]
                    cmd = cmd[idx+1:]
                r = cls.generic_assignment(cmd, original, '=', CommandKind.PHRASE_ASSIGN, CommandKind.PHRASE_ATTR_ASSIGN, True)
                if r[1] == CommandKind.PHRASE_ASSIGN:
                    r.append(words)
                return r
            else:
                return cls.p_command(cmd, original)
        elif cmd.find('>') != -1:
            idx = cmd.find('>')
            cmd = cmd[:idx] + " = " + cmd[idx+1:]
            words = []
            if cmd.startswith('['):
                idx = cmd.find(']')
                if idx == -1:
                    return [original, CommandKind.ERROR, 'Invalid assisted words']
                words = [a.strip() for a in cmd[1:idx].split(',')]
                cmd = cmd[idx+1:]
            r = cls.generic_assignment(cmd, original, '=', CommandKind.PHRASE_ASSIGN, CommandKind.PHRASE_ATTR_ASSIGN, True)
            if r[1] == CommandKind.PHRASE_ASSIGN:
                r.append(words)
            return r
        elif cmd.startswith("#"):
            cmd = cmd[1:]
            if cmd.find("-~") != -1:
                return cls.generic_assignment(cmd, original, '-~', CommandKind.TAG_ATTR_REMOVE, 'related')
            elif cmd.find("+~") != -1:
                return cls.generic_assignment(cmd, original, '+~', CommandKind.TAG_ATTR_APPEND, 'related')
            elif cmd.find("~") != -1:
                return cls.generic_assignment(cmd, original, '~', CommandKind.TAG_ATTR_ASSIGN, 'related')
            elif cmd.find("+=") != -1:
                return cls.generic_assignment(cmd, original, '+=', CommandKind.TAG_APPEND, CommandKind.TAG_ATTR_APPEND)
            elif cmd.find("-=") != -1:
                return cls.generic_assignment(cmd, original, '-=', CommandKind.TAG_REMOVE, CommandKind.TAG_ATTR_REMOVE)
            elif cmd.find("=") != -1:
                return cls.generic_assignment(cmd, original, '=', CommandKind.TAG_ASSIGN, CommandKind.TAG_ATTR_ASSIGN)
            else:
                idx = cmd.find(' ')
                if idx != -1:
                    cmd = cmd[:idx] + '=' + cmd[idx+1:]
                    return cls.generic_assignment(cmd, original, '=', CommandKind.TAG_ASSIGN, CommandKind.TAG_ATTR_ASSIGN)
                else:
                    return [original, CommandKind.T_COMMAND, "", cmd]
        elif cmd.find("-~") != -1:
            return cls.generic_assignment(cmd, original, '-~', CommandKind.MEANING_ATTR_REMOVE, 'synonyms')
        elif cmd.find("+~") != -1:
            return cls.generic_assignment(cmd, original, '+~', CommandKind.MEANING_ATTR_APPEND, 'synonyms')
        elif cmd.find("~") != -1:
            return cls.generic_assignment(cmd, original, '~', CommandKind.MEANING_ATTR_ASSIGN, 'synonyms')
        elif cmd.find("-!") != -1:
            return cls.generic_assignment(cmd, original, '-!', CommandKind.MEANING_ATTR_REMOVE, 'antonyms')
        elif cmd.find("+!") != -1:
            return cls.generic_assignment(cmd, original, '+!', CommandKind.MEANING_ATTR_APPEND, 'antonyms')
        elif cmd.find("!") != -1:
            return cls.generic_assignment(cmd, original, '!', CommandKind.MEANING_ATTR_ASSIGN, 'antonyms')
        elif cmd.find("+=") != -1:
            return cls.generic_assignment(cmd, original, '+=', CommandKind.MEANING_APPEND, CommandKind.MEANING_ATTR_APPEND)
        elif cmd.find("-=") != -1:
            return cls.generic_assignment(cmd, original, '-=', CommandKind.MEANING_REMOVE, CommandKind.MEANING_ATTR_REMOVE)
        elif cmd.find("=") != -1:
            idx = cmd.index('=')
            first = cmd[:idx]
            if cmd.startswith('[') or first.count(' ') > 3:
                words = []
                if cmd.startswith('['):
                    idx = cmd.find(']')
                    if idx == -1:
                        return [original, CommandKind.ERROR, 'Invalid assisted words']
                    words = [a.strip() for a in cmd[1:idx].split(',')]
                    cmd = cmd[idx+1:]
                r = cls.generic_assignment(cmd, original, '=', CommandKind.PHRASE_ASSIGN, CommandKind.PHRASE_ATTR_ASSIGN, True)
                if r[1] == CommandKind.PHRASE_ASSIGN:
                    r.append(words)
                return r
            else:
                return cls.generic_assignment(cmd, original, '=', CommandKind.MEANING_ASSIGN, CommandKind.MEANING_ATTR_ASSIGN)
        elif len(cmd) > 3:
            if cmd.count(' ') > 3:
                return cls.p_command(cmd, original)
            else:
                return cls.s_command(cmd, original)

class CommandKindTesting(unittest.TestCase):
    def test_s_command(self):
        commands = {
            "e": [None, CommandKind.ERROR, "e command requires at least one word"],
            "s": [None, CommandKind.ERROR, "s command requires at least one word"]

    }
        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

    def test_cd_pwd(self):
        commands = {
            "ls": [None, CommandKind.LS_COMMAND, '', ''],
            "cd people-1": [None, CommandKind.CD_COMMAND, 'people-1'],
            "cd": [None, CommandKind.CD_COMMAND, '']
        }
        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

    def test_remove(self):
        commands = {
            "rm > mi madre": [None, CommandKind.DELETE_PHRASE, 'mi madre'],
            "rm > 'mi madre'": [None, CommandKind.DELETE_PHRASE, 'mi madre'],
            "rm #family": [None, CommandKind.DELETE_TAG, 'family'],
            "rm #family-beginner": [None, CommandKind.DELETE_TAG, 'family-beginner'],
            "rm el padre": [None, CommandKind.DELETE_WORD, ['el padre']],
            "rm el padre, la mujer": [None, CommandKind.DELETE_WORD, ['el padre', 'la mujer']],
        }

        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

    def test_phrases(self):
        commands = {
            "> [ madre ] mi madre = my mother": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother'], ['madre']],
            "> [ mi, madre ] mi madre = my mother": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother'], ['mi', 'madre']],
            "> mi madre = my mother": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother'], []],
            "> mi madre = 'my mother'": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother'], []],
            "> mi madre = 'my mother', 'my mom'": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother', 'my mom'], []],
            "> mi madre = my mother, my mom": [None, CommandKind.PHRASE_ASSIGN, 'mi madre', ['my mother', 'my mom'], []],
            "> mi madre -= 'my mother'": [None, CommandKind.PHRASE_REMOVE, 'mi madre', ['my mother']],
            "> mi madre += 'my mother'": [None, CommandKind.PHRASE_APPEND, 'mi madre', ['my mother']],
            "> mi madre ~ 'mi padre'": [None, CommandKind.PHRASE_ATTR_ASSIGN, 'mi madre', 'related', ['mi padre']],
            "> mi madre -~ 'mi padre'": [None, CommandKind.PHRASE_ATTR_REMOVE, 'mi madre', 'related', ['mi padre']],
            "> mi madre +~ 'mi padre'": [None, CommandKind.PHRASE_ATTR_APPEND, 'mi madre', 'related', ['mi padre']],
            "> mi madre:files = /path/to/audio.file": [None, CommandKind.PHRASE_ATTR_ASSIGN, 'mi madre', 'files', ['/path/to/audio.file']],
            "> mi madre:files = '/path/to/audio.file'": [None, CommandKind.PHRASE_ATTR_ASSIGN, 'mi madre', 'files', ['/path/to/audio.file']],
            '> mi madre:files = "/path/to/audio.file"': [None, CommandKind.PHRASE_ATTR_ASSIGN, 'mi madre', 'files', ['/path/to/audio.file']],
            '> mi madre:files -= "/path/to/audio.file"': [None, CommandKind.PHRASE_ATTR_REMOVE, 'mi madre', 'files', ['/path/to/audio.file']],
        }
        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

    def test_meanings(self):
        commands = {
            "el padre = father": [None, CommandKind.MEANING_ASSIGN, 'el padre', ['father']],
            "padre = father": [None, CommandKind.MEANING_ASSIGN, 'padre', ['father']],
            "padre = dad, father": [None, CommandKind.MEANING_ASSIGN, 'padre', ['dad', 'father']],
            "padre=dad,father": [None, CommandKind.MEANING_ASSIGN, 'padre', ['dad', 'father']],
            "padre += dad": [None, CommandKind.MEANING_APPEND, 'padre', ['dad']],
            "padre+=dad": [None, CommandKind.MEANING_APPEND, 'padre', ['dad']],
            "padre-=dad": [None, CommandKind.MEANING_REMOVE, 'padre', ['dad']],
            "padre -= dad": [None, CommandKind.MEANING_REMOVE, 'padre', ['dad']],
            "inteligente(adj) = intelligent": [None, CommandKind.MEANING_ASSIGN, 'inteligente(adj)', ['intelligent']],
            "padre[1]:keyword = religous": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre[1]', 'keyword', ['religous']],
            "padre[1]:keyword -= religous": [None, CommandKind.MEANING_ATTR_REMOVE, 'padre[1]', 'keyword', ['religous']],
            "padre[1]:keyword += religous": [None, CommandKind.MEANING_ATTR_APPEND, 'padre[1]', 'keyword', ['religous']],
            "padre:files += /path/to/image/file,/path/to/image/file2": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'files', ['/path/to/image/file', '/path/to/image/file2']],
            "padre:files -= /path/to/image/file": [None, CommandKind.MEANING_ATTR_REMOVE, 'padre', 'files', ['/path/to/image/file']],
            "padre:synonyms = el papa, el dada": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre', 'synonyms', ['el papa', 'el dada']],
            "padre ~ el papa, el dada": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre', 'synonyms', ['el papa', 'el dada']],
            "padre -~ el papa, el dada": [None, CommandKind.MEANING_ATTR_REMOVE, 'padre', 'synonyms', ['el papa', 'el dada']],
            "padre +~ el papa, el dada": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'synonyms', ['el papa', 'el dada']],
            "padre+~el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'synonyms', ['el papa']],
            "padre~el papa": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre', 'synonyms', ['el papa']],
            "padre:sdsad~el papa": [None, CommandKind.ERROR, "Invalid command"],
            "padre:synonyms~el papa": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre', 'synonyms', ['el papa']],
            "padre:synonyms-~el papa": [None, CommandKind.MEANING_ATTR_REMOVE, 'padre', 'synonyms', ['el papa']],
            "padre:synonyms+~el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'synonyms', ['el papa']],
            "padre:synonyms +~ el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'synonyms', ['el papa']],
            "padre:s +~ el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'synonyms', ['el papa']],
            "padre:s += el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 's', ['el papa']],
            "padre ! el papa": [None, CommandKind.MEANING_ATTR_ASSIGN, 'padre', 'antonyms', ['el papa']],
            "padre -! el papa": [None, CommandKind.MEANING_ATTR_REMOVE, 'padre', 'antonyms', ['el papa']],
            "padre:a +! el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'antonyms', ['el papa']],
            "padre:a += el papa": [None, CommandKind.MEANING_ATTR_APPEND, 'padre', 'a', ['el papa']],
            "padre:a + = el papa": [None, CommandKind.ERROR, 'Invalid attribute name: a +'],
            "padre:a - = el papa": [None, CommandKind.ERROR, 'Invalid attribute name: a -'],
            "padre: = el papa": [None, CommandKind.ERROR, 'Invalid command'],
            "padre- = el papa": [None, CommandKind.ERROR, 'Invalid word: padre-'],
        }
        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

    def test_tags(self):
        commands = {
            "#family el padre, la madre": [None, CommandKind.TAG_ASSIGN, 'family', ['el padre', 'la madre']],
            "#family = el padre, la madre": [None, CommandKind.TAG_ASSIGN, 'family', ['el padre', 'la madre']],
            "#family -= el padre": [None, CommandKind.TAG_REMOVE, 'family', ['el padre']],
            "#family += el padre": [None, CommandKind.TAG_APPEND, 'family', ['el padre']],
            "#family:files += /path/to/image.file": [None, CommandKind.TAG_ATTR_APPEND, 'family', 'files', ['/path/to/image.file']],
            "#family:files -= /path/to/image.file": [None, CommandKind.TAG_ATTR_REMOVE, 'family', 'files', ['/path/to/image.file']],
            "#family:files = /path/to/image.file": [None, CommandKind.TAG_ATTR_ASSIGN, 'family', 'files', ['/path/to/image.file']],
            "#family ~ #people": [None, CommandKind.TAG_ATTR_ASSIGN, 'family', 'related', ['#people']],
            "#family -~ #people": [None, CommandKind.TAG_ATTR_REMOVE, 'family', 'related', ['#people']],
            "#family +~ #people": [None, CommandKind.TAG_ATTR_APPEND, 'family', 'related', ['#people']],
            "#family+~#people": [None, CommandKind.TAG_ATTR_APPEND, 'family', 'related', ['#people']],
            "#family~#people": [None, CommandKind.TAG_ATTR_ASSIGN, 'family', 'related', ['#people']],
        }
        for key in commands:
            r = CommandKind.parse_command(key)
            commands[key][0] = key
            assert r == commands[key]

if __name__ == 'main':
    command_kind_suite = unittest.TestSuite()
    command_kind_suite.addTest(CommandKindTesting("test_meanings"))
    command_kind_suite.addTest(CommandKindTesting("test_tags"))
    command_kind_suite.addTest(CommandKindTesting("test_phrases"))
    command_kind_suite.addTest(CommandKindTesting("test_remove"))
    command_kind_suite.addTest(CommandKindTesting("test_cd_pwd"))
    command_kind_suite.addTest(CommandKindTesting("test_s_command"))
    runner = unittest.TextTestRunner()
    runner.run(command_kind_suite)

