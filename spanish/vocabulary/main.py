import sys
from kinds import *
from words import WordBank
from words import get_singular, get_plural

words = WordBank('word_bank')
WORD_KINDS = []
for kind in WordKind:
    WORD_KINDS.append(str(kind).lower())

# returns the word kind if there is any
def get_word_kind_aux(arg):
    for kind in WORD_KINDS:
        i = 0
        k = 0
        while i < len(kind) and k < len(arg):
            if kind[i] != arg[k]:
                break
            i += 1
            k += 1

        if len(arg) > 0 and k == len(arg):
            return kind.capitalize()
    return None


def get_noun_kind_aux(first):
    if first == 'el':
        return 'Masculine'
    elif first == 'la':
        return 'Feminine'
    elif first == 'los':
        return 'PluralMasculine'
    elif first == 'las':
        return 'PluralFeminine'
        
    return None

def process_for_word_kind(args, index):
    first = args[index].lower()
    kind = None
    second_kind = get_noun_kind_aux(first)
    if second_kind:
        kind = 'Noun'
        if second_kind.startswith('Plural'):
            word = get_singular(args[index+1])
            return (kind, second_kind, word, index+2)
    else:
        kind = get_word_kind_aux(first)
        if kind == 'Noun':
            second_kind = get_noun_kind_aux(args[index+1].lower())
            if not second_kind:
                print("You have to provide el/la/los/las for the noun")
                return None
            if second_kind.startswith('Plural'):
                word = get_singular(args[index+2])
                return (kind, second_kind, word, index+3)
            else:
                return (kind, second_kind, args[index+2], index+3)
        elif kind == 'Verb':
            vk = args[index+1].lower()
            if vk != 'to':
                if vk in ['trans', 'tra', 'tran', 'tr', 'transitive']:
                    second_kind = 'Transitive'
                elif vk in ['intrans', 'intra', 'in', 'intrans', 'intransitive']:
                    second_kind = 'Intransitive'
                elif vk in ['ref', 'reflex', 'rex', 'reflexive']:
                    second_kind = 'Reflexive'
                elif vk in ['rec', 'recip', 'reciprocal']:
                    second_kind = 'Reciprocal'
                
    return (kind, second_kind, args[index+1], index+2)

def list_words(arguments):
    global words
    print(str(words))

def define_word(arguments):
    global words
    word = get_noun_kind_aux(arguments[0])
    if word:
        if len(arguments) == 2:
            word = arguments[1]
        else:
            word = ' '.join(arguments[1:])
    else:
        word = ' '.join(arguments)

    results = words.lookup(word)
    if results:
        i = 0
        for r in results:
            i += 1
            print(i, words.to_simple_str(word, r))
    else:
        print("No such word in the vocabulary: ", word)


def topic_assignment(topic, args):
    global words
    global word_kinds

    if len(arguments) == 0:
        results = words.lookup_topic(topic)
        pass
    else:
        pass

# adds a word
def add_word(arguments):
    global words
    global word_kinds
    if len(arguments) <= 0:
        print("Usage: a[dd] noun el madre mother")
        return

    i = 0
    kind, second_kind, word, i = process_for_word_kind(arguments, i)

    meaning = " ".join(arguments[i:])

    topic = None
    start = meaning.find('[')
    if start != -1:
        end = meaning.find(']', start + 1)
        topic = meaning[start+1:end].strip().lower()
        meaning = meaning[:start] + meaning[end+1:]
        meaning = meaning.strip()

    if topic and not words.lookup_topic(topic):
        answer = input("Adding topic '" + topic + "'? Type yes to add [y/N] ").strip().lower()
        if answer not in ['y', 'yes', 'ye']:
            return

    if meaning:
        meanings = [x.strip().lower() for x in meaning.split(',')]
    else:
        meanings = []
        
    r = words.add(word, kind, second_kind, meanings, topic)
    if not r:
        print("This word already exists with the given meaning")

def exit_program(arguments):
    print("Bye")
    sys.exit(0)

def try_again(arguments):
    print("Invalid command, try again")

def get_word_and_index(word):
    if word.startswith('el ') or word.startswith('la '):
        word = word[3:]
    idx = word.find(':')
    if idx != -1:
        num = int(word[idx+1:])
        word = word[:idx]
    else:
        num = 0
    return (word, num)

def synonym(arguments):
    global words
    if len(arguments) < 2:
        print("Incorrect usage of ==")
        return

    wis = []
    meanings = []
    for arg in arguments:
        wis.append(get_word_and_index(arg.strip()))
        meanings.append(words.lookup_idx(wis[-1][0], wis[-1][1]))
        if meanings[-1] == None:
            print("Missing meanings for ", wis[-1][0])
            return

    i = 0
    while i < len(meanings):
        if not meanings[i].get('same', None):
            meanings[i]['same'] = []
        j = 0
        while j < len(meanings):
            if i != j:
                meaning['same'].append([wis[j][0], wis[j][1]])
            j += 1

        i += 1
        
    words.is_modified()
        
    
def antonym(arguments):
    global words
    if len(arguments) != 2:
        print("Incorrect usage of ==")
        return
    first, first_idx = get_word_and_index(arguments[0].strip())
    second, second_idx = get_word_and_index(arguments[1].strip())

    first_meaning = words.lookup_idx(first, first_idx)
    second_meaning = words.lookup_idx(second, second_idx)
    if not first_meaning or not second_meaning:
        print("Missing first or second meanings")
    else:
        if not first_meaning.get('oppo', None):
            first_meaning['oppo'] = []
        if not second_meaning.get('oppo', None):
            second_meaning['oppo'] = []
        first_meaning['oppo'].append([second, second_idx])
        second_meaning['oppo'].append([first, first_idx])
        words.is_modified()    


COMMANDS = {
    'add': add_word,
    'exit': exit_program,
    'quit': exit_program,
    'define': define_word,
    'list': list_words
    }

# find the best possible command
def find_command(command):
    for cmd in COMMANDS.keys():
        i = 0
        k = 0
        while i < len(cmd) and k < len(command):
            if cmd[i] != command[k]:
                break
            i += 1
            k += 1

        if len(command) > 0 and k == len(command):
            return COMMANDS[cmd]

    return try_again
    

while True:
    command = input("Español: ").strip()
    command = ' '.join(command.split())
    if command.startswith('['):
        end = command.find(']', 2)
        if end == -1:
            try_again(command)
        else:
            topic = command[1:end].strip()
            command = command[end+1:].strip()
            commands = [x.strip().lower() for x in command.split(',')]
            topic_assignment(topic, commands)
    elif command.endswith('?'):
        commands = command[:-1].strip().split(' ')
        define_word(commands)
    elif command.find('==') != -1:
        commands = command.split('==')
        synonym(commands)
    elif command.find('=!') != -1:
        commands = command.split('=!')
        antonym(commands)
    elif command.find('=') != -1:
        x = command.find('=')
        command = command[:x] + ' ' + command[x+1:]
        commands = command.split(' ')
        add_word(commands)
    else:
        commands = command.split(' ')
        cmd = find_command(commands[0])
        cmd(commands[1:])
        
        
