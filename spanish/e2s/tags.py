from enum import Enum
from bank_utils import VocabError
import unittest
import re

class TagTextAttribute():
    def __init__(self, attrib, tag):
        self.tag = tag
        self.attrib = attrib
        self.key = attrib.key

    def assign(self, text):
        self.tag.node[self.key] = text

    @property
    def exists(self):
        return self.key in self.tag.node

    def clear(self):
        if self.tag.exists:
            if self.key in self.tag.node:
                self.tag.node[self.key] = ''

    @property
    def value(self):
        if self.tag.exists:
            if self.key in self.tag.node:
                return self.tag.node[self.key]
        return None

    def remove(self, text):
        if self.tag.node[self.key] == text:
            del self.tag.node[self.key]

    def append(self, text):
        if isinstance(text, list):
            if len(text) != 1:
                raise VocabError("Can not append more than one value: " + ','.join(text))
            text = text[0]
        if self.key in self.tag.node:
            self.tag.node[self.key] += text
        else:
            self.tag.node[self.key] = text

    def delete(self):
        del self.tag.node[self.key]

    def __str__(self):
        return str(self.tag) + ':' + str(self.attrib.value)


class TagListAttribute():
    def __init__(self, attrib, attribute_idx, tag):
        self.tag = tag
        self.attribute = attrib
        self.index = attribute_idx
        self.key = attrib.key

    @property
    def exists(self):
        return self.key in self.tag.node

    def clear(self):
        if self.tag.exists:
            if self.key in self.tag.node:
                self.tag.node[self.key] = []

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise VocabError("Must pass an integer as an index: " + str(item))
        if self.index != 0 and item != self.index:
            raise VocabError("Can not index to an already indexed attribute")
        if self.key in self.tag.node:
            if 0 < item <= len(self.tag.node[self.key]):
                return self.tag.node[self.key][item-1]

        raise VocabError("Out of bound index " + str(item))

    def assign(self, value, idx = -1):
        if idx == -1:
            if isinstance(value, list):
                if self.index == 0:
                    self.tag.node[self.key] = value
                else:
                    raise VocabError("Can not assign a list to index: " + str(self))
            elif self.index != 0:
                self.tag.node[self.key][self.index-1] = value
            else:
                self.tag.node[self.key] = [value]
            return
        elif self.index != 0:
            raise VocabError("Can not assign to an already indexed attribute")
        if 0 < idx <= len(self.tag.node[self.key]):
            if isinstance(value, list):
                if len(value) > 1:
                    raise VocabError("Can not assign more than one to an element of an attribute: " + str(self))
                self.tag.node[self.key][idx-1] = value[0]
            else:
                self.tag.node[self.key][idx-1] = value
        else:
            raise VocabError("Out of bounds index " + str(idx))

    def append(self, value):
        if self.index != 0:
            raise VocabError("Can not append to indexed attribute: " + str(self))
        if isinstance(value, list):
            if self.key in self.tag.node:
                self.tag.node[self.key].extend(value)
            else:
                self.tag.node[self.key] = value
        else:
            if self.key in self.tag.node:
                self.tag.node[self.key].append(value)
            else:
                self.tag.node[self.key] = [value]

    def remove(self, value):
        if self.index != 0:
            raise VocabError("Can not append to indexed attribute: " + str(self))
        if isinstance(value, list):
            if self.key in self.tag.node:
                for v in value:
                    self.tag.node[self.key].remove(v)
        else:
            if self.key in self.tag.node:
                self.tag.node[self.key].remove(value)

    def __str__(self):
        if self.index == 0:
            return str(self.tag) + ':' + str(self.attribute.value)
        else:
            return str(self.tag) + ':' + str(self.attribute.value) + "[" + self.index + "]"

    @property
    def value(self):
        if self.tag.exists:
            if self.key in self.tag.node:
                return ','.join(self.tag.node[self.key])
        return None

    def delete(self):
        if self.index == 0:
            del self.tag.node[self.key]
        else:
            del self.tag.node[self.key][self.index-1]

class Tag():
    @property
    def exists(self):
        return self.node != None

    def __getitem__(self, item):
        if not self.node:
            return None
        if isinstance(item, int):
            if 0 < item <= len(self.node['w']):
                return self.node['w'][item-1]
            raise VocabError("Not a valid index: " + str(item))
        elif isinstance(item, str):
            attrib = TagAttribs.parse(item, item)
            return self.get_attribute(attrib, 0)
        elif isinstance(item, TagAttribs):
            return self.get_attribute(item, 0)

    def get_attribute(self, attrib, attrib_index):
        if not attrib or not self.node:
            return None
        key = attrib.key
        a = self.node.get(key, None)

        if TagAttribs.is_list(attrib):
            if attrib_index == 0:
                return TagListAttribute(attrib, attrib_index, self)
            elif a and 0 < attrib_index <= len(a):
                return TagListAttribute(attrib, attrib_index, self)
            else:
                raise InvalidTagObjName("Invalid index: " + attrib + " " + attrib_index + " for word " + str(self))
        else:
            return TagTextAttribute(attrib, self)

    def __str__(self):
        if self.sub_tag == '*':
            return '#' + self.tag
        else:
            return '#' + self.tag + '-' + self.sub_tag

    def __init__(self, tag, sub_tag, tags, bank):
        self.tag = tag
        self.sub_tag = sub_tag
        self.bank = bank
        self.tags = tags
        if sub_tag == '*':
            self.normalized = self.tag
        else:
            self.normalized = self.tag + '-' + self.sub_tag

        self.node = None
        self.parent = None
        if tag in self.tags:
            tag_node = self.tags[tag]
            self.parent = tag_node
            if sub_tag in tag_node:
                self.node = tag_node[sub_tag]

    @property
    def words(self):
        if self.node:
            return self.node['w'][:]
        return None

    @property
    def empty(self):
        if self.node:
            return len(self.node['w']) == 0
        return True

    def create(self):
        if not self.parent:
            self.parent = {}
            self.tags[self.tag] = self.parent
        if not self.node:
            self.node = {'w':[]}
            self.parent[self.sub_tag] = self.node

    def delete(self):
        if not self.exists:
            return

        # if self.sub_tag == '*':
        #     for sub_tag in self.parent:
        #         for w in self.parent[sub_tag]['w']:
        #             word = self.bank.words[w]
        #             if sub_tag == '*':
        #                 word.remove_tag(self.tag)
        #             else:
        #                 word.remove_tag(self.tag + '-' + sub_tag)
        #     del self.tags[self.tag]
        # else:
        #     self.clear()
        #     del self.parent[self.sub_tag]
        self.clear()
        del self.parent[self.sub_tag]

    def assign_from(self, target):
        if not self.exists or not target.exists:
            return

        if target.tag == self.tag and target.sub_tag == self.sub_tag:
            return

        self.clear()
        self.assign_words(target.words)

    def append_from(self, target):
        if not self.exists or not target.exists:
            return

        if target.tag == self.tag and target.sub_tag == self.sub_tag:
            return

        self.append_words(target.words)

    def remove_from(self, target):
        if not self.exists or not target.exists:
            return

        if target.tag == self.tag and target.sub_tag == self.sub_tag:
            return

        self.remove_words(target.words)

    def clear(self):
        if not self.exists:
            return

        for w in self.node['w']:
            word = self.bank.words[w]
            word.remove_tag(self.normalized)

        self.node['w'] = []

    def assign_words(self, words):
        if not self.exists:
            raise VocabError("Can not add a word to a non-existing tag")
        self.clear()
        for word in words:
            normalized = self.bank.words.normalize(word)
            if normalized and normalized not in self.node['w']:
                self.node['w'].append(normalized)
                self.bank.words[normalized].add_tag(self.normalized)
            else:
                print("No such word or already added before: " + word)
                #raise VocabError("No such word or already added before: " + word)

    def assign_word(self, word, index):
        if not self.exists:
            raise VocabError("Can not add a word to a non-existing tag")
        if isinstance(word, list):
            word = word[0]
        if 0 < index <= len(self.node['w']):
            normalized = self.bank.words.normalize(word)
            if normalized and normalized not in self.node['w']:
                self.node['w'][index-1] = normalized
                self.bank.words[normalized].add_tag(self.normalized)
            else:
                print("No such word or already added before: " + word)
                #raise VocabError("No such word or already added before: " + word)


    def append_word(self, word):
        if not self.exists:
            raise VocabError("Can not add a word to a non-existing tag")
        normalized = self.bank.words.normalize(word)
        if normalized and normalized not in self.node['w']:
            self.node['w'].append(normalized)
            self.bank.words[normalized].add_tag(self.normalized)
        else:
            print("No such word or already added before: " + word)
            #raise VocabError("No such word or already added before: " + word)

    def append_words(self, words):
        for w in words:
            self.append_word(w)

    def delete_at(self, index):
        if not self.exists:
            return False
        if 0 < index <= len(self.node['w']):
            del self.node['w'][index-1]
            return True
        return False

    def remove_word(self, word, callback = True):
        if not self.exists:
            return
        if not callback:
            normalized = word
        else:
            normalized = self.bank.words.normalize(word)
        if normalized:
            self.node['w'].remove(normalized)
            if callback:
                self.bank.words[normalized].remove_tag(self.normalized)

        if len(self.node['w']) == 0:
            self.delete()

    def remove_words(self, words, callback = True):
        if not self.exists:
            return
        for w in words:
            if not callback:
                normalized = w
            else:
                normalized = self.bank.words.normalize(w)
            if normalized and normalized in self.node['w']:
                self.node['w'].remove(normalized)
                if callback:
                    self.bank.words[normalized].remove_tag(self.normalized)

        if len(self.node['w']) == 0:
            self.delete()

class Tags():
    def __len__(self):
        return len(self.tags)

    def __init__(self, bank):
        self.bank = bank
        self.tags = bank.data['tags']

    def get_tag(self, tag, sub_tag):
        return Tag(tag, sub_tag, self.tags, self.bank)

    def complete_tags(self, text, matches):
        text_tag = text[1:]
        idx = text_tag.find('-')
        idx2 = text_tag.find(':')
        if idx2 == -1:
            if idx == -1:
                for tag_name in self.tags:
                    if tag_name.startswith(text_tag):
                        for t in self.tags[tag_name]:
                            if t == '*':
                                matches.append('#' + tag_name)
                                if len(matches) > 10:
                                    return False
                            else:
                                matches.append('#' + tag_name + '-' + t)
                                if len(matches) > 10:
                                    return False
            else:
                tag = text_tag[:idx]
                sub_tag = text_tag[idx+1:]
                if self.tags.get(tag, None):
                    for t in self.tags[tag]:
                        if t != '*' and t.startswith(sub_tag):
                            matches.append('#' + tag + '-' + t)
                else:
                    return False
        else:
            sub_a = text_tag[idx2+1:].lower()
            #tag = self[text_tag[:idx2]]
            for a in TagAttribs:
                if a.value.startswith(sub_a):
                    matches.append('#'+text_tag[:idx2]+":"+a.value)

        return len(matches) > 0

    def __getitem__(self, item):
        if not item.startswith('#'):
            item = '#' + item
        tag, sub_tag, word_idx, attrib, attrib_idx = TagObjName.parse_object_name(item)
        t = Tag(tag, sub_tag, self.tags, self.bank)
        if not attrib:
            if word_idx == 0:
                return t
            words = t.words
            if words and 0 < word_idx <= len(words):
                return words[word_idx-1]
            raise VocabError("Invalid word index: " + item)
        else:
            w = Tag(tag, sub_tag, self.tags, self.bank)
            if w.exists:
                return w.get_attribute(attrib, attrib_idx)
        return None

    def add_tag(self, tag, sub_tag):
        t = Tag(tag, sub_tag, self.tags, self.bank)
        t.create()
        return t

    def del_tag(self, tag, sub_tag):
        t = Tag(tag, sub_tag, self.tags, self.bank)
        t.delete()


class InvalidTagObjName(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message

class TagAttribs(Enum):
    IMAGES = 'images'
    KEYWORD = 'keyword'

    @classmethod
    def parse(cls, attrib, message):
        attrib = attrib.lower()
        for a in TagAttribs:
            if a.value.startswith(attrib):
                return a
        else:
            raise InvalidTagObjName("Not a valid word attribute: " + attrib + " in "+ message)

    @property
    def key(self):
        return TagAttribs.get_json_key(self)

    @classmethod
    def get_json_key(cls, attrib):
        if attrib == TagAttribs.IMAGES:
            return 'i'
        elif attrib == TagAttribs.KEYWORD:
            return 'k'
        else:
            return None

    @classmethod
    def is_list(cls, attrib):
        return (attrib == TagAttribs.IMAGES
                )

class TagObjName():
    # #family-beginner[1]
    # #family-beginner:images[1]
    name_regex = re.compile(r'^#\w[\d\w_]*(-[\w\d_]+)?((\[\d+\])?|(:\w+)?(\[\d+\])?)$')

    @classmethod
    def is_valid(cls, name):
        return TagObjName.name_regex.match(name)

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
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid word index: " + str + " in " + tag_expr)
                word_idx = int(name[idx+1:-1])
                name = name[:idx]
        else:
            attrib = name[idx+1:]
            name = name[:idx]
            if name.endswith(']'):
                idx = name.find('[')
                str = name[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid word index: " + str + " in " + tag_expr)
                word_idx = int(str)
                name = name[:idx]
            if attrib.endswith(']'):
                idx = attrib.find('[')
                str = attrib[idx+1:-1]
                if not str.isnumeric():
                    raise InvalidTagObjName("Not a valid attribute index: " + str + " in " + tag_expr)
                attrib_idx = int(str)
                attrib = attrib[:idx]

        if attrib:
            for a in TagAttribs:
                if a.value.startswith(attrib):
                    attrib = a
                    break
            else:
                raise InvalidTagObjName("Not a valid tag attribute name: " + attrib + " in " + tag_expr)

        idx = name.find('-')
        if idx != -1:
            sub_name = name[idx+1:]
            base_name = name[:idx]
        else:
            sub_name = '*'
            base_name = name

        if attrib and not TagAttribs.is_list(attrib) and attrib_idx != 0:
            raise InvalidTagObjName("Not a list attribute: " + attrib + " in " + tag_expr)

        if word_idx != 0 and attrib:
            raise InvalidTagObjName("Can not provide word index and an attribute in this expression: " + tag_expr)

        return [base_name, sub_name, word_idx, attrib, attrib_idx]

class DummyBank():

    def __init__(self):
        self.data = {
            'tags': {},
            'words': {}
        }


class Testing(unittest.TestCase):
    def test_tags(self):
        bank = DummyBank()
        from commands import CommandParser
        from words import Words
        parser = CommandParser(bank)
        tags = Tags(bank)
        words = Words(bank)
        bank.words = words
        bank.tags = tags
        r = parser.parse_command("el padre = father")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("la madre = mother")
        w = words.add_word(r[1], r[2], r[3], r[6])
        r = parser.parse_command("#family padre, madre")
        t = tags.add_tag(r[1], r[2])
        assert len(tags) == 1
        t.append_words(r[6])
        assert t.words == ['padre[1]', 'madre[1]']
        t.remove_words(['la madre'])
        assert t.words == ['padre[1]']
        t.remove_words(['padre'])
        assert t.words == []

        t.append_word("el padre")
        t.append_word("la madre")
        assert tags["family[1]"] == 'padre[1]'
        assert tags["family[2]"] == 'madre[1]'
        assert tags["family"][1] == 'padre[1]'
        assert tags["family"][2] == 'madre[1]'

        r = parser.parse_command("#family:IMAGES = '/path/to/image.jpg'")
        t = tags[r[1]+'-'+r[2]]
        t[r[4]].assign(r[6])
        assert t["IMAGES"].value == '/path/to/image.jpg'
        assert t["IMAGES"][1] == '/path/to/image.jpg'

        r = parser.parse_command("#family:IMAGES[1] = '/path/to/image2.jpg'")
        t = tags[r[1]+'-'+r[2]]
        t[r[4]].assign(r[6], r[5])
        assert t["IMAGES"].value == '/path/to/image2.jpg'
        assert t["IMAGES"][1] == '/path/to/image2.jpg'


    def test_tag_obj_name_parse(self):
        assert TagObjName.parse_object_name("#family") == ["family", '*', 0, None, 0]
        assert TagObjName.parse_object_name("#family-beginner") == ["family", 'beginner', 0, None, 0]
        assert TagObjName.parse_object_name("#family-beginner[1]") == ["family", 'beginner', 1, None, 0]
        assert TagObjName.parse_object_name("#family-beginner:images") == ["family", 'beginner', 0, TagAttribs.IMAGES, 0]
        assert TagObjName.parse_object_name("#family-beginner:images[1]") == ["family", 'beginner', 0, TagAttribs.IMAGES, 1]
        try:
            assert TagObjName.parse_object_name("#family-beginner[1]:images") == ["family", 'beginner', 0, TagAttribs.IMAGES, 1]
        except InvalidTagObjName as e:
            assert e.message == "Can not provide word index and an attribute in this expression: #family-beginner[1]:images"


if __name__ == 'main':
    test_suite = unittest.TestSuite()
    test_suite.addTest(Testing("test_tag_obj_name_parse"))
    test_suite.addTest(Testing("test_tags"))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)

