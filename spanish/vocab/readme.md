# Data Structures

```
#family-beginner = el padre, la madre, 

# WORDS
# el padre
# padre
# padre[1]
# el padre[1]
# padre(male)
# padre(male)[1]
# el padre(male)[1]
```

```
words[padre] = [
    padre,
    [
        {
            wk: male,             # word_category
            k: relative          # keywords
            m: [father, dad]     # meanings
            t: [family-beginner] # tag
            p: [1231231]         # phrases
            f: [/path/to/file]   # files
            x: [/path/to/t.txt]  # text files which include padre
            s: [el papa]         # synonyms
            a: [la madre]        # antonyms
            u: time              # last use
        },
        {
            c: adjective
            k: religous
            m: [father]
            t: [religion-beginner]
            p: [123123, 1231231]
        }
    ]
]
tags[family] = [
       
]

el padre = family
el padre:keyword = 

    # el padre:keyword = relative
    # el padre:keyword =
    MEANING_KEYWORD_ASSIGN = 'meaning-keyword-assign'
    MEANING_KEYWORD_REMOVE = 'meaning-keyword-remove'


    # el padre ~ el papa
    SYNONYM_ADD = 'synonym-add'
    # padre ~ - papa
    SYNONYM_REMOVE = 'synonym-remove'

    # inteligente ! burro
    ANTONYM_ADD = 'antonym-add'
    # inteligente ! - burro
    ANTONYM_REMOVE = 'antonym-remove'

    # mi madre > my mother
    # mi madre > 'my mother', 'my mom'
    TRASNLATION_ASSIGN = 'translation-assign'
    # mi madre -> my mother
    TRASNLATION_REMOVE = 'translation-remove'
    # mi madre +> my mom
    TRASNLATION_APPEND = 'translation-append'

    # el padre:file = /path/to/image.file
    # padre[2]:file = /path/to/audio.file
    MEANING_FILE = 'meaning-file'

    # attach el padre /path/to/image.file
    # a padre /path/to/audio.file
    # a -d padre audio.file   # delete a file from meaning
    # a -f padre audio.file   # move to the front in the list
    # a padre                 # list all attached files (same as s -f padre)
    ATTACH_FILE_TO_MEANING = 'attach-file-to-meaning'

    # s padre
    # s padre, madre
    # s -k padre        # show keywords
    # s -x padre, madre # list examples
    # s -t padre, madre # list tags
    # s -s padre, madre # list synonyms
    # s -a padre, madre # list antonyms
    # s -e padre, madre # list everything
    # s -f padre        # list attached files
    # s -m padre        # list full meanings
    # s -n padre        # list full first meaning (default)
    SPANISH_WORD_LOOKUP = 'spanish-word-lookup'

    # e -x father         # list examples
    # e -t father         # list tags
    # e -s father, mother # list synonyms
    # e -a father, mother # list antonyms
    # s -e father         # list everything
    # s -f father         # list attached files
    ENGLISH_WORD_LOOKUP = 'english-word-lookup'


    # course family-beginner
    # c family-beginner
    # c -d family-beginner          # delete a course
    BEGIN_COURSE = 'begin-course'
    # c -a el padre
    ADD_MEANING_TO_COURSE = 'add-meaning-to-course'
    # c -d el padre
    REMOVE_MEANING_FROM_COURSE = 'remove-meaning-from-course'
    # c -x      # end the current course
    END_COURSE = 'end-course'

    ERROR = 'error-command'


```