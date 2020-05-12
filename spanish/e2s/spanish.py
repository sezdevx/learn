import re
import unicodedata

# partially based on https://github.com/bermi/Python-Inflector/blob/master/rules/spanish.py
# other useful projects: https://github.com/jaumeortola/spanish-dict-tools

class Spanish():
    @classmethod
    def normalize(cls, text):
        """Normalizes a word, removing accents etc.."""
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        return str(text.decode('utf-8'))

    @classmethod
    def normalize_phrase(cls, text):
        translation = text.maketrans("\t\n\"'\\`@$><=;:|&{()}%#!?¿¡.+-[]", "                              ", "")
        new_text = text.translate(translation)
        if new_text.find('  ') != -1:
            new_text = ' '.join(text.strip().split())
        return cls.normalize(new_text.lower())

    @classmethod
    def str_replace(cls, word, find, replace):
        for i in range(0, len(find)):
            word = re.sub(find[i], replace[i], word)
        return word

    irregulars = {
        'base': 'bases',
        'carácter': 'caracteres',
        'champú': 'champús',
        'curriculum': 'currículos',
        'espécimen': 'especímenes',
        'jersey': 'jerséis',
        'memorándum': 'memorandos',
        'menú': 'menús',
        'no': 'noes',
        'país': 'países',
        'referéndum': 'referendos',
        'régimen': 'regímenes',
        'sándwich': 'sándwiches',
        'si': 'sis',
        'taxi': 'taxis',
        'ultimátum': 'ultimatos',
    }

    non_changing = {
        'lunes', 'martes', 'miércoles', 'jueves', 'viernes',
        'paraguas', 'tijeras', 'gafas', 'vacaciones', 'víveres',
        'cumpleaños', 'virus', 'atlas', 'sms', 'hummus',
    }

    @classmethod
    def get_plural(cls, word):
        rules = [
            ['(?i)([aeiou])x$', '\\1x'],
            # This could fail if the word is oxytone.
            ['(?i)([áéíóú])([ns])$', '|1\\2es'],
            ['(?i)(^[bcdfghjklmnñpqrstvwxyz]*)an$', '\\1anes'],  # clan->clanes
            ['(?i)([áéíóú])s$', '|1ses'],
            ['(?i)(^[bcdfghjklmnñpqrstvwxyz]*)([aeiou])([ns])$', '\\1\\2\\3es'],  # tren->trenes
            ['(?i)([aeiouáéó])$', '\\1s'],  # casa->casas, padre->padres, papá->papás
            ['(?i)([aeiou])s$', '\\1s'],  # atlas->atlas, virus->virus, etc.
            ['(?i)([éí])(s)$', '|1\\2es'],  # inglés->ingleses
            ['(?i)z$', 'ces'],  # luz->luces
            ['(?i)([íú])$', '\\1es'],  # ceutí->ceutíes, tabú->tabúes
            ['(?i)(ng|[wckgtp])$', '\\1s'],
            # Anglicismos como puenting, frac, crack, show (En que casos podría fallar esto?)
            ['(?i)$', 'es']  # ELSE +es (v.g. árbol->árboles)
        ]

        lower = word.lower()

        for w in cls.non_changing:
            if lower[-1 * len(w):] == w:
                return word

        for singular, plural in cls.irregulars.items():
            match = re.search('(?i)(^' + singular + ')$', word, re.IGNORECASE)
            if match:
                result = re.sub('(?i)' + singular + '$', match.expand('\\1')[0] + plural[1:], word)
                return result

        for rule in rules:
            match = re.search(rule[0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                replacement = rule[1]
                if re.match(r'|', replacement):
                    for k in range(1, len(groups)):
                        replacement = replacement.replace('|' + str(k),
                                                          cls.str_replace(groups[k - 1], 'ÁÉÍÓÚáéíóú', 'AEIOUaeiou'))

                result = re.sub(rule[0], replacement, word)
                match = re.search('(?i)([aeiou]).{1,3}([aeiou])nes$', result)

                if match and len(match.groups()) > 1 and not re.search('(?i)[áéíóú]', word):
                    result = result.replace(match.group(0), cls.str_replace(
                        match.group(1), 'AEIOUaeiou', 'ÁÉÍÓÚáéíóú') + match.group(0)[1:])

                return result

        return word

    @classmethod
    def get_singular(cls, word):
        rules = [
            [r'(?i)^([bcdfghjklmnñpqrstvwxyz]*)([aeiou])([ns])es$', '\\1\\2\\3'],
            [r'(?i)([aeiou])([ns])es$', '~1\\2'],
            [r'(?i)shes$', 'sh'],  # flashes->flash
            [r'(?i)oides$', 'oide'],  # androides->androide
            [r'(?i)(sis|tis|xis)$', '\\1'],  # crisis, apendicitis, praxis
            [r'(?i)(é)s$', '\\1'],  # bebés->bebé
            [r'(?i)(ces)$', 'z'],  # luces->luz
            [r'(?i)([^e])s$', '\\1'],  # casas->casa
            [r'(?i)([bcdfghjklmnñprstvwxyz]{2,}e)s$', '\\1'],  # cofres->cofre
            [r'(?i)([ghñptv]e)s$', '\\1'],  # llaves->llave, radiocasetes->radiocasete
            [r'(?i)jes$', 'je'],  # ejes->eje
            [r'(?i)ques$', 'que'],  # tanques->tanque
            [r'(?i)es$', '']  # ELSE remove _es_  monitores->monitor
        ]

        lower = word.lower()

        for w in cls.non_changing:
            if lower[-1 * len(w):] == w:
                return word

        for singular, plural in cls.irregulars.items():
            match = re.search('(^' + plural + ')$', word, re.IGNORECASE)
            if match:
                result = re.sub('(?i)' + plural + '$', match.expand('\\1')[0] + singular[1:], word)
                return result

        for rule in rules:
            match = re.search(rule[0], word, re.IGNORECASE)
            if match:
                groups = match.groups()
                replacement = rule[1]
                if re.match('~', replacement):
                    for k in range(1, len(groups)):
                        replacement = replacement.replace('~' + str(k),
                                                          cls.str_replace(groups[k - 1], 'AEIOUaeiou', 'ÁÉÍÓÚáéíóú'))

                result = re.sub(rule[0], replacement, word)
                match = re.search('(?i)([áéíóú]).*([áéíóú])', result)

                if match and len(match.groups()) > 1 and not re.search('(?i)[áéíóú]', word):
                    result = cls.str_replace(result, 'ÁÉÍÓÚáéíóú', 'AEIOUaeiou')

                return result

        return word

    @classmethod
    def tokenize(cls, text):
        result = []
        i = 0
        start = -1
        while i < len(text):
            if text[i] in [' ', '\t', '\r', '\n', '?', '.', ',', '¿', '"', "'", '-']:
                if start != -1 and start != i:
                    result.append(text[start:i])
                    start = -1
            elif start == -1:
                start = i
            i += 1

        if start != -1 and start != i:
            result.append(text[start:i])

        return result
