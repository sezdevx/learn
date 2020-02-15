import enum

class WordKind(str, enum.Enum):
    Noun = "Noun"
    PluralNound = "PluralNoun"
    Adjective = "Adjective"
    Adverb = "Adverb"
    Verb = "Verb"
    Preposition = "Preposition"
    Pronoun = "Pronoun"
    Conjuction = "Conjuction"

    def __str__(self):
        return self.value

class NounKind(str, enum.Enum):
    Feminine = 'Feminine'
    Masculine = 'Masculine'
    PluralFeminine = 'PluralFeminine'
    PluralMasculine = 'PluralMasculine'

    def __str__(self):
        return self.value

class VerbKind(str, enum.Enum):
    Transitive = 'Transitive'
    Intransitive = 'Intransitive'
    Reflexive = 'Reflexive'
    Reciprocal = 'Reciprocal'

    def __str__(self):
        return self.value
    

