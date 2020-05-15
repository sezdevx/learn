import readline
import curses
import sys
from bank import WordBank
from commands import CommandParser
from commands import CommandKind
from words import WordKind
from words import Words

def tag_delete(bank, c):
    options = c[1]
    tags = c[2]
    for t in tags:
        tag = t[0]
        sub_tag = t[1]
        index = t[2]
        attrib = t[3]
        attrib_idx = t[4]
        t = bank.tags.get_tag(tag, sub_tag)
        if not t.exists:
            print("COULDN'T FIND: ", str(t))
            continue
        if not attrib:
            if index == 0:
                t.delete()
            else:
                t.delete_at(index)
        else:
            a = t.get_attribute(attrib, attrib_idx)
            if a:
                a.delete()

def tag_assign(bank, c):
    tag = c[1]
    sub_tag = c[2]
    index = c[3]
    attrib = c[4]
    attrib_idx = c[5]
    values = c[6]
    if not attrib:
        t = bank.tags.add_tag(tag, sub_tag)
        if index == 0:
            t.assign_words(values)
        else:
            t.assign_word(values, index)
    else:
        t = bank.tags.get_tag(tag, sub_tag)
        if t.exists:
            a = t.get_attribute(attrib, attrib_idx)
            if not a:
                print("COULDN'T FIND: ", str(a))
            a.assign(values)


def tag_lookup(bank, c):
    options = c[1]
    tags = c[2]
    for t in tags:
        tag = t[0]
        sub_tag = t[1]
        index = t[2]
        attrib = t[3]
        attrib_idx = t[4]
        t = bank.tags.get_tag(tag, sub_tag)
        if not t.exists:
            print("COULDN'T FIND: ", str(t))
            continue
        if not attrib:
            if index == 0:
                print(str(t))
                print(', '.join([Words.denormalize_name(w) for w in t.words]))
                # for w in t.words:
                #     print(Words.denormalize_name(w), end=', ')
                print()
            else:
                print(tag+'[' + str(index) + ']')
                print(t[index])
        else:
            a = t.get_attribute(attrib, attrib_idx)
            if a:
                print(str(a))
                if attrib_idx == 0:
                    print(a.value)
                else:
                    print(a[attrib_idx])

def tag_remove(bank, c):
    tag = c[1]
    sub_tag = c[2]
    index = c[3]
    attrib = c[4]
    attrib_idx = c[5]
    values = c[6]
    t = bank.tags.get_tag(tag, sub_tag)
    if not t.exists:
        print("COULDN'T FIND: ", str(t))
        return
    if not attrib:
        t.remove_words(values)
    else:
        if t.exists:
            a = t.get_attribute(attrib, attrib_idx)
            if not a:
                print("COULDN'T FIND: ", str(a))
            a.remove(values)

def tag_append(bank, c):
    tag = c[1]
    sub_tag = c[2]
    index = c[3]
    attrib = c[4]
    attrib_idx = c[5]
    values = c[6]
    t = bank.tags.get_tag(tag, sub_tag)
    if not t.exists:
        print("COULDN'T FIND: ", str(t))
        return
    if not attrib:
        t.append_words(values)
    else:
        if t.exists:
            a = t.get_attribute(attrib, attrib_idx)
            if not a:
                print("COULDN'T FIND: ", str(a))
            a.append(values)

def word_delete(bank, c):
    options = c[1]
    words = c[2]
    for w in words:
        name = w[0]
        kind = w[1]
        index = w[2]
        attrib = w[3]
        attrib_idx = w[4]

        w = bank.words[name]
        if index != 0 and w:
            w = w[index]
        if not w:
            print("COULDN'T FIND: ", name)
            continue
        if not kind.unknown and not w.kind.unknown and kind != w.kind:
            print("Mismatched word kinds: ", WordKind.get_prefix(kind), " vs " , WordKind.get_prefix(w.kind) + " for " + name)
            continue

        if not attrib:
            w.delete()
        else:
            a = w.get_attribute(attrib, attrib_idx)
            if not a:
                print("COULDN'T FIND: ", str(a))
            a.delete()


def word_append(bank, c):
    word, kind, index, attrib, attrib_idx, values = c[1], c[2], c[3], c[4], c[5], c[6]

    w = bank.words[word]
    if index != 0 and w:
        w = w[index]
    if not w:
        print("COULDN'T FIND: ", word)
        return
    if not kind.unknown and not w.kind.unknown and kind != w.kind:
        print("Mismatched word kinds: ", WordKind.get_prefix(kind), " vs " , WordKind.get_prefix(w.kind))
        return

    if not attrib:
        w.append_meaning(values)
    else:
        a = w.get_attribute(attrib, attrib_idx)
        if not a:
            print("COULDN'T FIND: ", str(a))
        a.append(values)

def word_remove(bank, c):
    word, kind, index, attrib, attrib_idx, values = c[1], c[2], c[3], c[4], c[5], c[6]

    w = bank.words[word]
    if index != 0 and w:
        w = w[index]
    if not w:
        print("COULDN'T FIND: ", word)
        return
    if not kind.unknown and not w.kind.unknown and kind != w.kind:
        print("Mismatched word kinds: ", WordKind.get_prefix(kind), " vs " , WordKind.get_prefix(w.kind))
        return

    if not attrib:
        w.remove_meaning(values)
    else:
        a = w.get_attribute(attrib, attrib_idx)
        if not a:
            print("COULDN'T FIND: ", str(a))
        a.remove(values)

def word_assign(bank, c):
    word = c[1]
    kind = c[2]
    index = c[3]
    attrib = c[4]
    attrib_idx = c[5]
    values = c[6]
    if not attrib:
        if index != 0:
            w = bank.words[word]
            if not w:
                print("COULDN'T FIND: ", word)
                return
            w = w[index]
            if not kind.unknown and not w.kind.unknown and kind != w.kind:
                print("Mismatched word kinds: ", WordKind.get_prefix(kind), " vs " , WordKind.get_prefix(w.kind))
            else:
                w.assign_meaning(values)
        else:
            bank.words.add_word(word, kind, index, values)
    else:
        w = bank.words[word]
        if index != 0:
            w = w[index]
        a = w.get_attribute(attrib, attrib_idx)
        if not a:
            print("COULDN'T FIND: ", str(a))
        a.assign(values)

def word_lookup(bank, c):
    INDENT = 3
    options = c[1]
    words = c[2]
    for w in words:
        name = w[0]
        kind = w[1]
        index = w[2]
        attrib = w[3]
        attrib_idx = w[4]

        if not attrib:
            word = bank.words[name]
            if not word:
                print("COULDN'T FIND: ", name)
                continue
            if index != 0:
                word = word[index]
            if not kind.unknown and not word.kind.unknown and kind != word.kind:
                print("Mismatched word kinds: ", WordKind.get_prefix(kind), " vs " , WordKind.get_prefix(word.kind))
                continue

            if index == 0:
                kind = None
                meaning_count = word.meaning_count + 1
                w = word[1]
                for i in range(1, meaning_count):
                    if kind != w.kind:
                        print(w.pretty_name)
                        kind = w.kind
                    print(INDENT * ' ', i, ')', w.meaning)
                    w = word[i+1]
            else:
                print(word.pretty_name)
                print(word.meaning)
            print()
        else:
            word = bank.words[name]
            if index != 0:
                word = word[index]
            a = word[attrib]
            if attrib_idx != 0:
                print(a[attrib_idx])
            else:
                print(a.value)


bank = WordBank()
parser = CommandParser(bank)
def input_loop():
    global bank
    global parser
    while True:
        info = bank.summary()
        command = input("\n" + info + "\n% ").strip()
        c = parser.parse_command(command)
        if not c:
            print("Not a valid command, try again")
        elif c[0] == CommandKind.WORD_ASSIGN:
            word_assign(bank, c)
        elif c[0] == CommandKind.WORD_APPEND:
            word_append(bank, c)
        elif c[0] == CommandKind.WORD_REMOVE:
            word_remove(bank, c)
        elif c[0] == CommandKind.WORD_LOOKUP:
            word_lookup(bank, c)
        elif c[0] == CommandKind.WORD_DELETE:
            word_delete(bank, c)

        elif c[0] == CommandKind.TAG_ASSIGN:
            tag_assign(bank, c)
        elif c[0] == CommandKind.TAG_APPEND:
            tag_append(bank, c)
        elif c[0] == CommandKind.TAG_REMOVE:
            tag_remove(bank, c)
        elif c[0] == CommandKind.TAG_LOOKUP:
            tag_lookup(bank, c)
        elif c[0] == CommandKind.TAG_DELETE:
            tag_delete(bank, c)

        elif c[0] == CommandKind.EXIT:
            exit(1)
        elif c[0] == CommandKind.CONTINUE:
            pass
        elif c[0] == CommandKind.LOAD:
            bank.load(c[1])
        elif c[0] == CommandKind.SAVE:
            bank.save()

if len(sys.argv) > 1:
    bank.load(sys.argv[1])
else:
    bank.load('espanol.json')
readline.set_completer(parser.complete)
# ' ', '\t', '\n', '"', '\\', '\'', '`', '@', '$', '>', '<', '=', ';', '|', '&', '{', '(', '\0'
#readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.parse_and_bind('tab: complete')
input_loop()

