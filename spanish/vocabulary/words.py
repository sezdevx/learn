import json
import os.path

def get_singular(word):
    if word.endswith('es'):
        word = word[:-2]
        if word[-2] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['y', 'l', 'r', 'n', 'd', 'c', 'j', 's', 'x']:
            if word[-1] == 'c':
                return word[:-1] + 'z'
            else:
                return word
        return word + 'e'
    else:
        return word[:-1]

def get_plural(word):
    if word[-2] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['y', 'l', 'r', 'n', 'd', 'z', 'j', 's', 'x']:
            if word[-1] == 'z':
                return word[:-1] + 'c' + 'es'
            else:
                return word + 'es'
    return word + 's'

def load_words(path):
    try:
        with open(path, 'r') as input_file:
            return json.load(input_file)
    except:
        print("Couldn't read the file:", path)
    return {}


class WordBank():

    def __process(self):
        for item in self.words.items():
            w = item[0]
            meanings = item[1]
            for meaning in meanings:
                if meaning.get('t', None):
                    topic = meaning['t']
                    t = self.topics.get(topic, None)
                    if t:
                        t.append(meaning)
                    else:
                        self.topics[topic] = [meaning]

    def __str__(self):
        if self.modified:
            return "MODIFIED \n" + str(self.words) + "\n\n" + str(self.topics) + "\n"
        else:
            return str(self.words) + "\n\n" + str(self.topics) + "\n"
    
    def __init__(self, path):
        self.words_path = path + '.json'
        self.words = load_words(self.words_path)
        self.topics = {}
        
        self.__process()
        self.modified = False

    def is_modified(self):
        self.modified = True

    def lookup(self, word):
        return self.words.get(word, None)

    def lookup_idx(self, word, idx):
        results = self.words.get(word, None)
        if results and len(results) > idx:
            return results[idx]
        return None

    def lookup_topic(self, topic):
        return self.topics.get(topic, None)

    # saves anything that is modified to the disk
    def save(self):
        if self.modified:
            with open(self.words_path, 'w') as output_file:
                json.dump(self.words, output_file, indent=2)

    def to_simple_str(self, word, result):
        r = result['k'] + ': '
        if result['k'] == 'Noun':
            if result['s'] == 'Masculine':
                r += 'el ' + word + ' '
            elif result['s'] == 'Feminine':
                r += 'la ' + word + ' '
            elif result['s'] == 'PluralMasculine':
                r += 'los ' + get_plural(word) + ' '
            elif result['s'] == 'PluralFeminine':
                r += 'las ' + get_plural(word) + ' '
        elif result['k'] == 'Verb' and not result.get('s', None):
            r += word + ' (' + result['s'] + ')'
        else:
            r += word + ' '

        if result.get('t', None):
            r += ' [' + result['t']  + ']'
            
        r += '\n    '
        r += ','.join(result['m'])
        return r
    

    def add(self, word, kind, second_kind, meanings, topic):
        results = self.words.get(word, None)
        foundIt = False
        if results and meanings:
            for result in results:
                if kind == result['k']:
                    for meaning in meanings:
                        if meaning in result['m']:
                            foundIt = True
                            break
                    if foundIt:
                        break
            
        if foundIt:
            return None

        r = None
        r_idx = 0
        if results:
            i = 0
            for result in results:
                i += 1
                if kind == result['k']:
                    s = result.get('s', None)
                    if second_kind:
                        if s == second_kind:
                            r = result
                            r_idx = i
                    else:
                        r = result
                        r_idx = i

        if not r:
            r = {}
            r['k'] = kind
            if second_kind:
                r['s'] = second_kind
            if topic:
                r['t'] = topic
            if meanings:
                r['m'] = list(set(meanings))
            if results:
                results.append(r)
                r_idx = results.length() - 1
            else:
                self.words[word] = [r]
                r_idx = 0
        else:
            if meanings:
                r['m'] = list(set(r['m']).union(set(meanings)))
            if r.get('t', None):
                if topic and topic != r['t']:
                    print("Mismatched topics for ", word, ':', topic, 'vs', r['t'])
            elif topic:
                r['t'] = topic

        if topic:
            t = self.topics.get(topic, None)
            if t:
                t.append([word, r_idx])
            else:
                self.topics[topic] = [[word, r_idx]]
                        
        self.modified = True
        return r
