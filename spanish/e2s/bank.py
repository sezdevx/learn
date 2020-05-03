import json

class WordBank():

    def __init__(self, path):
        if path:
            self.word_bank_path = path + '.json'
            self.bank = self.load_json(self.word_bank_path)
        else:
            self.word_bank_path = ':memory'
            self.bank = {'words': {}, 'tags': {}}

    @classmethod
    def load_json(cls, input_file):
        if input_file != ':memory':
            try:
                with open(input_file, 'r') as input_file:
                    return json.load(input_file)
            except:
                print("Couldn't read the file:", input_file)
        return {
            'words': {},
            'rwords': {},
            'tags': {},
            'p2p': {},
            'rp2p': {},
            'phrases': {},
            'courses': {},
        }


    def save(self):
        if self.word_bank_path != ':memory':
            with open(self.word_bank_path, 'w') as output_file:
                json.dump(self.bank, output_file, indent=2)


