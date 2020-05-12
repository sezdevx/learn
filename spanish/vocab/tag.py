from word import Word

class Tag():

    def __init__(self, tag, bank):
        self.bank = bank
        self.tags = bank.tags
        self.full_name = tag
        idx = tag.find('-')
        if idx != -1:
            self.sub_tag = tag[idx+1:]
            self.name = tag[:idx]
        else:
            self.sub_tag = '*'
            self.name = tag

        self.find()

    @property
    def exists(self):
        return self.node != None

    @property
    def words(self):
        if self.exists:
            return self.node['w']
        else:
            return []

    # def delete_if_empty(self):
    #     if self.exists:
    #         if len(self.tags[self.name][self.sub_tag]['w']) == 0:
    #             del self.tags[self.name][self.sub_tag]
    #         if len(self.tags[self.name]) == 0:
    #             del self.tags[self.name]
    #         self.node = None

    def delete(self):
        if self.exists:
            if self.name == self.full_name:
                for sub_tag in self.tags[self.name]:
                    for w in self.tags[self.name][sub_tag]:
                        word = Word(w, self.bank)
                        if word.normalize:
                            if sub_tag == '*':
                                word.remove_tag(self.name)
                            else:
                                word.remove_tag(self.name+"-"+sub_tag)

                del self.tags[self.name]
            else:
                for w in self.node['w']:
                    word = Word(w, self.bank)
                    if word.normalize:
                        if self.sub_tag == '*':
                            word.remove_tag(self.name)
                        else:
                            word.remove_tag(self.full_name)
                del self.tags[self.name][self.sub_tag]
                if len(self.tags[self.name]) == 0:
                    del self.tags[self.name]
            self.node = None

    def create(self):
        if self.tags.get(self.name, None):
            list = self.tags[self.name]
            if list.get(self.sub_tag, None):
                self.node = list[self.sub_tag]
            else:
                self.node = {'w': []}
                list[self.sub_tag] = self.node
        else:
            self.node = {}
            self.tags[self.name] = self.node
            self.node[self.sub_tag] = {'w': []}
            self.node = self.node[self.sub_tag]

        return self.node

    def find(self):
        if self.tags.get(self.name, None):
            list = self.tags[self.name]
            if list.get(self.sub_tag, None):
                self.node = list[self.sub_tag]
            else:
                self.node = None
        else:
            self.node = None

        return self.node

    def add_word(self, word):
        if self.exists:
            if word not in self.node['w']:
                self.node['w'].append(word)

    def remove_word(self, word):
        if self.exists:
            if word == '*':
                self.delete()
            elif word in self.node['w']:
                self.node['w'].remove(word)
                if not self.node['w']:
                    self.delete()



