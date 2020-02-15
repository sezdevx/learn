print("Type of a string is: ", type("string"))

s = "This is a string"
print('"', s[:], '"', " is a copy of the original string")

# individual characters of a string
print('"', s[0], '"', " is the first character")
print('"', s[-1], '"', " is the last character")

# reversing a string
print('"', s[::-1], '"', " is the reversed string")

# copy of a string
print('"', s[::2], '"', " is part of a string where we skip a character")

# substrings (slicing)
print('"', s[0:5], '"', " is substring [0, 5)")
print('"', s[1:5], '"', " is substring [1, 5)")
print('"', s[1:6], '"', " is substring [0, 6)")

# length of a string
print('"', len(s), '"', " is the length of the string")

# empty string
s = ''
if not s:
    print(f"'{s}' is an empty string")
s = ""
if not s:
    print(f"'{s}' is an empty string")

s = '"'
print(s)
s = "'"
print(s)

# escape chars
s = "\n is a new line\t is a tab\x00"
print(s)

# Triple quoted string
s = """This is a triple-quoted block string
A very long one indeed
It could be multi-line"""
print(s)

# Raw string (no escape chars)
s = r"Raw strings do not have escape chars like \n or \t"
print(s)

# Concatenating a string
s1 = "This is a"
s2 = "string"
print(s1 + " " + s2)
s = "One" "two" "three"
print(s)
s = "One" \
    "Two" \
    "Three"
print(s)
s = ("One"
     "Two"
     "Three")
print(s)
s = "One" + "Two" + "Three"
print(s)


# Repeating a string
s1 = "*" * 80
print(s1)

# formatting
s = "string"
print("This is a %s" % s)
print(f"This is a {s}")
print("This is a {0}".format(s))

# splitting
s = "A, b,C"
components = s.split(",")
print(components)
components = [x.strip().lower() for x in s.split(",")]
print(components)
print(":".join(components))
print(" | ".join(components))

if "This is a string".startswith("This is"):
    print("This is a string starts with This is, duh!")
if "This is a string".endswith("a string"):
    print("This is a string ends with a string, duh!")

s = "Unicode文字列はバイト文字列よりもクールです"
print(s)
b = s.encode('utf8')
print(type(b))
s = b.decode('utf8')
print(type(s))

if "123".isdigit():
    print("123 are all digits")
if "123".isdecimal():
    print("123 are all decimal digits")
if "ABC".isalpha():
    print("ABC are all alphabetic")
if "ABC123".isalnum():
    print("ABC123 are alphanumeric")
if '\u00BD'.isnumeric():
    print('\u00BD is numeric')
if not "123".isalpha():
    print("123 is NOT alphabetic")
if not "ABC".isdigit():
    print("ABC is NOT all digits")

s = "  There is whitespace all around   "
print("|" + s + "|")
print("lstrip")
print("|" + s.lstrip() + "|")
print("rstrip")
print("|" + s.rstrip() + "|")
print("strip")
print("|" + s.strip() + "|")

s = "This is a string"
print(s.find("is"))
print(s.find("is", s.find("is") + 1))
print(s.find("is", s.find("is", s.find("is") + 1) + 1))
print(s.replace("is", "as"))
print(s.upper())
print(s.lower())

for c in s:
    print(c, end=' ')
print()

if 'is' in s:
    print("s has is in it:", s)

# automatic implicit concatenation
s = "This "  'is '    "a string"
print(s)

print('Bell \a\a')
print('Backspace \b\b\b\b\b')
print('By Hex Characters \x63 \x64 \x65 \x66')
print('Null character \0 is here')
print('By Octal characters \143 \144 \145 \146')
print("Unicode Character \N{GREEK CAPITAL LETTER DELTA}")
print("Unicode Character \u0394")
print("Unicode Character \U00000394")
print("Unicode Character \N{SQUARED ID}")
print("Unicode Character \U0001F194")

# no escaping
print("This is \mine \other \stuff")
s = "Unicode文字列はバイト文字列よりもクールです"
if s == s.encode('utf-8').decode('utf-8'):
    print("Encoding and decoding with utf-8 does not lose any info")

if s != s.encode('ascii', "ignore").decode('ascii'):
    print("Encoding and decoding with ascii cause losing info")

# null character still counts
s = "\0\0\0"
print(r"'\0\0\0' the length is still", len(s))

# testing existince of a string within a string
s = "This is a string"
if "in" in s:
    print("in exists within", s)

if not "abc" in s:
    print("abc does not exist within", s)

s = "spam"
print(s[::-1])
print(s[slice(None, None, -1)])

print("52" + str(12))

print(str("This is a string"), repr("This is a string"))

print(ord('a'), chr(ord('a')))
print(ord('b'), chr(ord('b')))

try:
    s = "This is a string"
    s[0] = 'B'
except:
    print("You can not change a string")

s = "This is a string"
print(s.replace("is", ""))
print(s.replace("is", "'is'"))

print("I am %s, I am %d years old" % ("Joe", 29))

if not "\0".isprintable():
    print(r"\0 is NOT printable")
if "A".isprintable():
    print("A is printable")

s = "this Is A String  "
print("Orignal: ", s)
print("capitalize: ", s.capitalize())
print("casefold: ", s.casefold())
print(s.ljust(80))
print(s.center(80))
print(s.rjust(80))
print(s.rstrip()+"|")
print(s.lower().count("is"))
print(s.count("is"))

a = "sthing"
b = "123456"
# create a translation table
table = str.maketrans(a, b)
print(s.translate(table))

if "This is a string".endswith("string"):
    print("Ends with string")

s = "a\tb\tc"
print(s)
print(s.expandtabs(4))
print(s.expandtabs(3))
print(s.expandtabs(1))

s = "This is a string"
print(s.partition(' '))
print(s.partition(' is'))
print(s.partition("None"))

print(s.find("is"))
print(s.find("None"))

print(s.index('is'))
try:
    print(s.index('None'))
except:
    print("None does not exist within the string:", s)


if not "123".isidentifier():
    print("123 is not a valid identifier")

if "abc123".isidentifier():
    print("abc123 is a valid identifier")

if "abc".islower():
    print("abc is lower")
if not "ABC".islower():
    print("ABC is NOT lower")

if "ABC".isupper():
    print("ABC is upper")
if not "abc".isupper():
    print("abc is NOT upper")

if "   ".isspace():
    print("   is space")
if not "abc".isspace():
    print("abc is NOT space")

if not "TITLE".istitle():
    print("TITLE is NOT title case")
if not "title".istitle():
    print("title is NOT title case")
if "Title".istitle():
    print("Title is title case")

s = "lowerUPPER"
print(s, s.swapcase())

s = """This is a 
multi-line string
A very long one
which has at least 4
lines
"""

# keeps the eol character attached to each string
lines = s.splitlines(True)
for line in lines:
    print(line)
# by default it removes new line characters from the strings
lines = s.splitlines()
for line in lines:
    print(line)

s = "This is a string"
l = list(s)
print(l)
print(''.join(l))

print("str %s" % "String")
print("repr %r" % "String")
print("char %c" % ']')
print("char %c" % 93)
print("decimal %d" % 3.15)
print("decimal %d" % 3)
print("integer %i" % 3.15)
print("integer %i" % 3)
print("octal %o" % 255)
print("hexadecimal %x" % 255)
print("hexadecimal %X" % 255)
print("float %e" % 3.15)
print("float %e" % 3)
print("float %E" % 3.15)
print("float %E" % 3)
print("float %f" % 3.15)
print("float %f" % 3)
print("float %F" % 3.15)
print("float %F" % 3)
print("float %g" % 3.15)
print("float %g" % 3)
print("float %G" % 3.15)
print("float %G" % 3)
print("literal %%s %s" % '%' )

print("%d..%-6d..%06d" % (12, 12, 12))
print("%d..%6d..%06d" % (12, 12, 12))

print("%-6.2f..%6.2f..%06.4f %06.2f" % (3.1415, 3.1415, 3.1415, 3.1415))
print("%.*f" % (4, 3.1415))
print("%.*f" % (2, 3.1415))


print("%12s %-12s" % ("String", "String"))
print("%-12s %-12s" % ("String", "String"))
print("%-12s %12s" % ("String", "String"))

print("My name is {} and my age is {}".format("Joe", 28))
print("My name is {1} and my age is {0}".format(28, "Joe"))
print("My name is {name} and my age is {age}".format(name="Joe", age=28))
print("My name is {name} and my age is {age}".format(age=28, name="Joe"))
print("My name is {0[name]} and my age is {0[age]}".format({'name': 'Joe', 'age': 28}))
print("My name is {} and my age is betwen {ages}".format("Joe", ages = [20,30]))
print("My name is {0} and my age is betwen {ages}".format("Joe", ages = (20,30)))

print("{:<10s} {:^10s} {:>10s}".format("One", "Two", "Three"))
print("{:>10s} {:^10s} {:<10s}".format("One", "Two", "Three"))
print("{:.>10s} {:.^10s} {:.<10s}".format("One", "Two", "Three"))
print("{:_>10s} {:_^10s} {:_<10s}".format("One", "Two", "Three"))

name = "Joe"
age = 28
print(f"My name is {name} and my age is {age}")
print(f"My name is {name.capitalize()} and my birthyear is {2020 - age}")
print(f"{name:^10} {age:>10}")
print(f"{name:<10} {age:<10}")




     




