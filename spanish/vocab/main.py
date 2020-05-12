import readline
import curses

from command_kind import CommandKind
from word_bank import WordBank
from course import Course
from word import Word

INDENT = 5
def find_max_width(words):
    x = 8
    for w in words:
        s = str(w)
        if len(s) > x:
            x = len(s)
    x += 2
    return x

def practice(bank, pit):
    a = ['a', 's', 'd', 'f']
    for p in pit:
        print(p.word)
        i = 0
        for c in p.choices:
            print(i, ')', c)
            i+=1

def ls_command(bank, options, name):
    if 'c' in options:
        courses  = bank.get_courses()
        if not courses:
            print("No courses")
        else:
            i = 1
            for t in courses:
                c = Course(t, bank)
                print(i,')', t, ':', c.word_count, 'words', c.tag_count, 'tags', c.phrase_count, 'phrases')
                i+=1
                if i % 10 == 0:
                    x = input("Press enter to continue, [eXit/Quit]: ").strip().lower()
                    if x == 'exit' or x == 'quit' or x == 'q' or x == 'x':
                        break
        return

    if name or bank.pwd:
        course = bank.pwd
        if name:
            course = bank.get_course(name)
        if course:
            if 'w' in options:
                words = course.words
                if not words:
                    print("No words in", course.name)
                else:
                    print(course.name, 'words')
                    i = 0
                    for w in words:
                        word = Word(w, bank)
                        if not word.normalize:
                            course.remove_word(w.simple_name)
                        else:
                            print(w)
                            i+=1
                            if i % 10 == 0:
                                x = input("Press enter to continue, [eXit/Quit]: ").strip().lower()
                                if x == 'exit' or x == 'quit' or x == 'q' or x == 'x':
                                    break

            elif 't' in options:
                tags  = course.tags
                if not tags:
                    print("No tags in", course.name)
                else:
                    print(course.name, 'tags')
                    i = 0
                    for t in tags:
                        print(i,')', t)
                        i+=1
                        if i % 10 == 0:
                            x = input("Press enter to continue, [eXit/Quit]: ").strip().lower()
                            if x == 'exit' or x == 'quit' or x == 'q' or x == 'x':
                                break
            elif 'p' in options:
                pids = course.phrase_ids
                if not pids:
                    print("No phrases in", course.name)
                else:
                    print(course.name, 'phrases')
                    i = 0
                    for pid in pids:
                        s = bank.phrases.get(pid, None)
                        print(i,')', s['p'])
                        i+=1
                        if i % 10 == 0:
                            x = input("Press enter to continue, [eXit/Quit]: ").strip().lower()
                            if x == 'exit' or x == 'quit' or x == 'q' or x == 'x':
                                break
            else:
                print(course.name)
                print(course.word_count, "words")
                print(course.total_word_count, "total words")
                print(course.tag_count, "tags")
                print(course.phrase_count, "phrases")
        elif name:
            print("No such course: ", name)
    else:
        if 'w' in options:
            it = bank.word_iterator()
            for w in it:
                print(w)
        else:
            print(bank.name)
            print(bank.word_count, "words")
            print(bank.total_word_count, "total words")
            print(bank.tag_count, "tags")
            print(bank.phrase_count, "phrases")


def print_phrases(phrases, options):
    print(phrases[0])
    i = 1
    for p in phrases[1:]:
        print(i, ')', p)
        i+=1

def print_words(words, options):
    x = find_max_width(words)
    for w in words:
        if w.normalize:
            m = ", ".join(w.get_meanings())
            print(f"{str(w):>{x}}: {m}")
            if 's' in options:
                print('Synonyms:', ', '.join(w.get_list_attrib('s')))
            if 'a' in options:
                print('Antonyms:', ', '.join(w.get_list_attrib('a')))
            if 'f' in options:
                print('File Names:')
                for f in w.get_list_attrib('f'):
                    print(f)
            if 'x' in options:
                examples = w.get_list_attrib('x')
                i = 1
                for sid in examples:
                    print(i, ')', bank.phrases[sid]['p'])
                    i+=1
        else:
            print(f"{str(w):>{x}}: NOT FOUND")

def print_reverse_words(rwords, options):
    x = find_max_width(rwords)
    for w in rwords:
        if w.normalize:
            print(f"{str(w):>{x}}: {w.get_meanings()[0]}")
        else:
            print(f"{str(w):>{x}}: NOT FOUND")

def print_tag_words(words, options, tag):
    print(tag,":", ', '.join([str(w) for w in words]))


bank = WordBank('espanol')
def input_loop():
    global bank
    while True:
        info = bank.name + ": " + str(bank.word_count) + " words, " + str(bank.tag_count) +  " tags, " + str(bank.phrase_count) + " phrases"
        command = input("\n" + info + "\n% ").strip()
        cmd = CommandKind.parse_command(command)
        if not cmd:

            print("Not a valid command, try again")

        elif cmd[1] == CommandKind.ERROR:

            print(cmd[2])

        elif cmd[1] == CommandKind.EXIT:

            bank.save()
            break

        elif cmd[1] == CommandKind.SAVE:

            bank.save()

        elif cmd[1] == CommandKind.DELETE_WORD:

            cmd = bank.delete_words(cmd[2])
            if cmd:
                print("Couldn't find:", ','.join(cmd))

        elif cmd[1] == CommandKind.DELETE_TAG:

            if not bank.delete_tag(cmd[2]):
                print("Couldn't find:" , cmd[2])

        elif cmd[1] == CommandKind.DELETE_PHRASE:

            if not bank.delete_phrase(cmd[2]):
                print("Couldn't find:", cmd[2])

        elif cmd[1] == CommandKind.CREATE_COURSE:

            bank.create_course(cmd[2])

        elif cmd[1] == CommandKind.PUT_IN_COURSE:

            if not bank.pwd:
                print("Not in a course yet")
            else:
                bank.put_in_course(cmd[2])

        elif cmd[1] == CommandKind.CD_COMMAND:

            bank.change_course(cmd[2])

        elif cmd[1] == CommandKind.LS_COMMAND:

            ls_command(bank, cmd[2], cmd[3])

        elif cmd[1] == CommandKind.PRACTICE_COMMAND:

            if cmd[3]:
                bank.change_course(cmd[3])

            if not bank.pwd:
                print("Select a course first")
            else:
                pit = bank.pwd.practice(cmd[2])
                practice(bank, pit)

        elif cmd[1] == CommandKind.S_COMMAND:

            options = cmd[2]
            words = bank.words_list(cmd[3])
            print_words(words, options)

        elif cmd[1] == CommandKind.P_COMMAND:

            options = cmd[2]
            phrases = bank.phrase_list(cmd[3])
            print_phrases(phrases, options)

        elif cmd[1] == CommandKind.R_COMMAND:

            options = cmd[2]
            phrases = bank.reverse_phrase_list(cmd[3])
            print_phrases(phrases, options)

        elif cmd[1] == CommandKind.E_COMMAND:

            options = cmd[2]
            rwords = bank.reverse_words_list(cmd[3])
            print_reverse_words(rwords, options)


        elif cmd[1] == CommandKind.MEANING_ASSIGN:

            bank.meaning_assign(cmd)

        elif cmd[1] == CommandKind.MEANING_APPEND:

            if not bank.meaning_append(cmd):
                print("Couldn't find", cmd[2])

        elif cmd[1] == CommandKind.MEANING_REMOVE:

            r = bank.meaning_remove(cmd)
            if r:
                print("COuldn't find", ', '.join(r))

        elif cmd[1] == CommandKind.MEANING_ATTR_ASSIGN:

            if not bank.meaning_attr_assign(cmd):
                print("Couldn't find", cmd[2])

        elif cmd[1] == CommandKind.MEANING_ATTR_REMOVE:

            r = bank.meaning_attr_remove(cmd)
            if r:
                if not r[0]:
                    print("Couldn't find:", cmd[2])
                else:
                    print("Not found values: ", ','.join(r))

        elif cmd[1] == CommandKind.MEANING_ATTR_APPEND:

            if not bank.meaning_attr_append(cmd):
                print("Couldn't find", cmd[2])

        elif cmd[1] == CommandKind.T_COMMAND:

            options = cmd[2]
            words = bank.tag_list(cmd[3])
            if not words:
                print("No such tag:", cmd[3])
            else:
                print_tag_words(words, options, cmd[3])

        elif cmd[1] == CommandKind.TAG_ASSIGN:

            r = bank.tag_assign(cmd)
            if r:
                print("Couldn't find: ", ', '.join(r))

        elif cmd[1] == CommandKind.TAG_APPEND:

            r = bank.tag_append(cmd)
            if r:
                print("Couldn't find: ", ', '.join(r))

        elif cmd[1] == CommandKind.TAG_REMOVE:

            r = bank.tag_remove(cmd)
            if r:
                print("Couldn't find: ", ', '.join(r))

        elif cmd[1] == CommandKind.TAG_ATTR_ASSIGN:

            pass

        elif cmd[1] == CommandKind.TAG_ATTR_REMOVE:

            pass

        elif cmd[1] == CommandKind.TAG_ATTR_APPEND:

            pass

        elif cmd[1] == CommandKind.PHRASE_ASSIGN:

            bank.phrase_assign(cmd)

        elif cmd[1] == CommandKind.PHRASE_APPEND:

            pass

        elif cmd[1] == CommandKind.PHRASE_REMOVE:

            r = bank.phrase_remove(cmd)
            if r:
                if r[0] == cmd[2]:
                    print("Couldn't find phrase: ", cmd[2])
                else:
                    for p in r:
                        print("Couldn't find ", r)

        elif cmd[1] == CommandKind.PHRASE_ATTR_ASSIGN:

            pass

        elif cmd[1] == CommandKind.PHRASE_ATTR_REMOVE:

            pass

        elif cmd[1] == CommandKind.PHRASE_ATTR_APPEND:

            pass

        else:
            r = []
            print(r)


readline.set_completer(bank.complete)
# ' ', '\t', '\n', '"', '\\', '\'', '`', '@', '$', '>', '<', '=', ';', '|', '&', '{', '(', '\0'
#readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.set_completer_delims(' \t\n"\'\\`@$><=;|&{(')
readline.parse_and_bind('tab: complete')
input_loop()
