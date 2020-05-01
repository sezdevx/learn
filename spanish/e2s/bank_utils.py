
class VocabError(Exception):
    pass

class QuoteError(VocabError):
    def __init__(self, message = ""):
        self.message = message

    def __str__(self):
        return self.message

class BankUtils():
    @classmethod
    def dequote_and_split(cls, value):
        r = []
        in_phrase = False
        start = 0
        symbol = ""
        i = 0
        while i < len(value):
            if in_phrase:
                if value[i] == symbol:
                    in_phrase = False
                    r.append(value[start:i].strip())
                    start = i + 1
            elif value[i] == '"' or value[i] == "'":
                in_phrase = True
                symbol = value[i]
                start = i+1
            elif value[i] == ',' and start != i:
                r.append(value[start:i].strip())
                start = i+1
            i+=1
        if start < i:
            r.append(value[start:i].strip())
        return r

    @classmethod
    def dequote(cls, text):
        if len(text) <= 1:
            return text
        if text.startswith('"') or text.startswith("'"):
            symbol = text[0]
            if not text.endswith(symbol):
                raise QuoteError("Not properly quoted: " + text)
            return text[1:-1].strip()
        else:
            return text
