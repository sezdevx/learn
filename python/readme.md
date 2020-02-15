## Learning Python
* Raw strings can not end in a single backslash
```python
c = r'This is not corret\' # NOT A VALID string
c = r'This is correct\\'[:-1] # we remove the last character so it ends with \
```

## Introducing Python

### Keywords
```python
help('keywords')

# or
import keyword
print(keyword.kwlist)
```

### Types
```python
type(7)
type('a')
type(0.99)
type([])
type(())
type({})

if isinstance(7, int):
    print('7 is an integer')
```

### Multiple name assignment
```python
a, b, c = 1, "A", []
a = b = c = 1
```

### Booleans
```python
# false
bool(False)
bool('')
bool(0)
bool(())
bool([])
bool(0.0)
bool(0.0000)
bool({})
bool(None)

# true
bool(True)
bool('a')
bool(1)
bool(0.0001)
bool([0])
bool(['a'])
bool((0, 1))
```

### Integers
```python
million = 1_000_000
a = 1_2_3 # stores 123
```

#### Integer division
```python
x = 7 // 2 # 3
y = 2 ** 3 # 8
```

### Operation precedence
```python
x = -5 ** 2   # -25
x = -(5 ** 2) # -25
x = (-5) ** 2 # 25
```

### Bases
```python
x = 0b10 # 2
x = 0o10 # 8
x = 0x10 # 16

v = 25
print(bin(v))
print(oct(v))
print(hex(v))
```

### Convert a number to character
```python
print(chr(65)) # A
print(ord('A')) # 65
```

### Convert to integer
```python
int(True)  # 1
int(False) # 0
int(9.8)   # 9
int('12')  # 12
int('10', 2) # base 2 conversion, 2
int('10', 8) # base 8 conversion, 8
int('10', 16) # base 16 conversion, 16
int('10', 22) # base 22 conversion, 22
int(10) # 10
```

* You can't have an integer that starts with 0
```python
# this is not legal
# x = 03
```

### Floats
```python
print(5.)
print(5.0)
print(05.0)
print(5e0)
print(5e1)
million = 1_000_000.0
```

### Convert to float
```python
float(True)
float(False)
float(98)
float('99')
float('99.9')
float('-1.5')
float('1.0e4')
```

### Continuing lines with \
```python
s = 1 + \
    2 + \
    3 + \
    4

# but with () you don't need \
s = (
    1 +
    2 +
    3 +
    4
    )
```

### If statements
```python
if 5 < x and x < 10:
  print("Between 5 and 10")
elif 1 < x and x < 5:
  print("Between 1 and 5")
elif 10 < x < 15:
  print("Between 10 and 15")
else:
  print("Not between 1 and 15")
```

### Check if a value exists in a sequence

```python
s = {'a', 'b', 'c', 'o'}
if 'o' in s:
  print("Found o")
s = ['a', 'b', 'c', 'o']
if 'o' in s:
  print("Found o")
s = ('a', 'b', 'c', 'o')
if 'o' in s:
  print("Found o")
s = {'a' : 'apple', 'b': 'banana', 'c' : 'cherry', 'o' : 'orange'}
if 'o' in s:
  print("Found o")
s = "abco"
if 'o' in s:
  print("Found o")
```

### Walrus operator
```python
name := expression
if diff := x - y >= 0:
  print("Fine")
else:
  print("Over the limit: " , diff)
```

### Multi line strings
```python
"""This is a long string
which spans multiple
lines"""
'''This is a long string
too, but uses single quotes
rather than double quotes'''
```

### Convert to string
```python
str(9.8)
str(9)
str(True)
```

### Escape characters in string
```python
print('\t')
print('\'')
print("\"")
print("\\")
```

### Raw strings
```python
info = r'\n will appear as it is in these raw strings'
```

### String concatenation
```python
x = 'a' + 'b' + 'c'
y = 'a' 'b' 'c'
z = ('a' 'b' 
  'c' 'd')
```

### Duplicating strings
```python
x = 'a' * 3 + '\n'
```

### Accessing string characters
```python
x = "abcdefghijklmn"
print(x[0]) # a
print(x[3]) # d
```

### Changing a string character
```python
x = 'Hello'
y = x.replace('H', 'M') # y points to Mello, x is still Hello
y = 'P' + x[1:]  # y points to Mello
```

### Substring with a slice
```python
a = "abcdefghijklmnopqrstuvwxyz"
b = a[:] # the entire string
b = a[5:] # string starting from index 5
b = a[1:3] # string between 1 and 3, excluding 3
b = a[-3:] # the last three characters
b = a[::3] # from start to end, skipping chars by 3 chars
b = a[-1::-1] # starts from the end, going backwads by 1 char
              # effectively reversing the characters of the string
b = a[::-1] # same as above, reversing the string
```

### Length of the string
```python
print(len("ABCD"))
```

### Splitting strings
```python
a="a,b,c,d,e,f,g"
l = a.split(',')
```

### Combining strings with join
```python
v = ['a', 'b', 'c']
x = ','.join(v) # a,b,c
```

### Replacing strings
```python
s = "This is a long long sentence"
new_str = s.replace('long', 'very long')
# This is a very long very long sentence
new_str = s.replace('long', 'very long', 1)
# This is a very long long sentence
```

### Stripping white space
```python
w = "    a   "
w.strip()     # 'a'
w.strip(' ')  # 'a'
w.lstrip()    # 'a  '
w.rstrip()    # '   a'
w = "!!!a!!"
w.strip('!')  # 'a'
w = "?$!a#$!" 
w.strip('$?!#') # 'a'
```

### Character groups
```python
import string
string.whitespace
string.punctuation
```

### Searching strings and other methods
```python
s = "abcd"
if s.startswith("ab"):
  print("Yes it does start with ab")
if s.endswith("cd"):
  print("Yes it does end with cd")
index = s.find('b')
index = s.index('b') # if index does not find it, it raises an exception
index = s.rfind('b')
index = s.rindex('b')
count = s.count('ab')
if s.isalpha():
  print("All alpahabetic characters")
s = "this is a long distance"
print(s.capitalize()) # This is a long distance
print(s.title()) # This Is A Long Distance
s.upper()
s.lower()
s.swapcase()
```

### String alignment
```python
s = "This is a string"
print(s.center(80)) # aligned to center in 80 character length
print(s.ljust(80))  # aligned to left in 80 character length
print(s.rjust(80))  # aligned to right in 80 character length
```

### Old style string formatting
```python
"%s" % 42 # '42'
"%d" % 42 # '42'
'%x' % 42 # '2a'
'%o' % 42 # '52'
'%s' % 7.03 # '7.03'
'%f' % 7.03 # '7.030000'
'%e' % 7.03 # '7.030000e+00'
'%g' % 7.03 # '7.03'
'%s%%' % 10 # '10%'
'Capital of %s is %s' % (state, capital)
'%+30s' % message # + means right align, 30 means the width of the field 
'%-30.30s' % mesg # - left align, 30 is the field width, the other 30 means the max char to print
'%.3f' % number # after decimal max 3 digits
```

### New style string formatting
```python
'Capital of {0} is {1}'.format(state, capital)
'Capital of {1} is {0}'.format(capital, state)
'Capital of {} is {}'.format(state, capital)
'Capital of {state} is {capital}'.format(state='NY', capital='Albany')
"Capital of {0[state]} is {0[capital]}".format({'state': 'NY', 'capital': 'Albany'})
```
* Initial colon
* Optional fill character (default is ' ')
* Optional alignment character < means left, > means right, ^ means center
* Optional sign for numbers
* Optional min width
* Optional . (period) to separate min width and max chars
* Optional max chars
* Conversion type

```python
'Capital of {:^8s} is {:_^20s}'.format(state, capital)
```

### Newest style f-string
```python
f"Capital of {state} is {capital}"
f"Capital of {state =} is {capital =}"
f"Capital of {state.capitalize()} is {capital.upper()}"
f"{number :^10}"
```

### While loops
```python
i = 1
while i <= 5:
  if i == 3:
    break
  elif i == 4:
    continue
  print(i)
  i += 1
```

### Break checker while else
```python
i = 0
while i < len(numbers)
  n = numbers[i]
  if n % 2 == 0:
    print("Found an even number")
    break
  i += 1
else:
  # called only when break is NOT called
  print("Couldn't find any even number")
```

### Iterate with for and in
```python
for a in 'abcdef':
  print(a)
```

### Range in for loops
```python
for n in range(0, 10):
  print(n)
list(range(0, 10))
for n in range(0, 10, 2):
  print(n)
```

### Single element tuples
```python
x = ('a', )
x = 'a',
# while passing to a function, you need to use double parentheses
function(('a', ))
```

### Multi element tuples assignment
```python
t = (0, 1, 2)
x, y, z = t

x = 1
y = 2
# exchange values
x, y = y, x
```

### Creating tuples and tuple operations
```python
l = [1, 2, 3]
t = tuple(l)

x = ('a', ) + ('b', 'c') # ('a', 'b', 'c')
x = ('a', ) * 3 # ('a', 'a', 'a')

a = (7, 2)
b = (7, 2, 9)
a == b # False
a <= b # True
a < b  # True

for w in ('a', 'b', 'c'):
  print(w)
```

### Check the id of a variable
```python
t1 = ('a', 'b')
t2 = ('c')
print(id(t1))
t1 += t2
print(id(t1)) # t1 points to a different tuple now
```

### Converting to a list
```python
x = list(range(0, 4))
x = list(('a', 'b', 'c'))
```

### Splitting a string into a list
```python
x = "9/21/2011".split('/')
x = '9//21//2011'.split('/') # two empty entries will be in the list
x = '9//21//2011'.split('//') # ['9', '21', '2011']
```

### Index access
```python
l = [1, 2, 3]
l[0] # 1
l[-1] # 3
l[-2] # 1

## Slicing
l[0:1] # [1, 2]
l[-1:]  # [3]
l[::2] # [1, 3]
l[::-1] # [3, 2, 1]

# with invalid indices in slicing, it will not throw an exception
# instead, it will snap to the closest index
l[5:] # [] returns empty list
```

### Reversing a list in place
```python
l = [1, 2, 3]
l.reverse() # no return here
```

### Adding an item
```python
l = [1, 2, 3]
l.append(4)
l.insert(0, 0) # [0, 1, 2, 3, 4]
```

### Duplicating items in a list
```python
l = ['a'] * 3  # ['a', 'a', 'a']
```

### Extending a list
```python
x = ['a', 'b', 'c']
y = ['d', 'e']
x += y 
x.extend(y)
```

### Changing items of a list
```python
l = ['a', 'b', 'c']
l[1] = 'd'
l[1:2] = ['e', 'f', 'g', 'h']
l[1:] = [] # l becoes ['a']
l = ['a', 'b', 'c']
del l[1]
l.remove('c')
l = ['a', 'b', 'c']
x = l.pop() # x is 'c'
x = l.pop(0) # x is 'a'
l.clear() # deletes all items in the list
```

### Finding items in a list
```python
l = ['a', 'b', 'c', 'd']
l.index('a') # is 0
c = l.count('a') # c is 1, there is only one 'a'
```

### Convert a list to a string
```python
l = ['a', 'b', 'c', 'd']
x = ','.join(l)
```

### Sorting a list
```python
l = ['c', 'd', 'e', 'a', 'b']
l.sort() # sorts the list in place
x = sorted(l)
l.sort(reverse=True)
x = sorted(l, reverse=True)
```

### Length of a list
```python
l = ['c', 'd', 'e', 'a', 'b']
len(l) # is 5
```

### Copying
```python
l = ['c', 'd', 'e', 'a', 'b']
x = l.copy()
x = list(l)
x = l[:]
```

### Deep copying
```python
import copy
l = [1, 2, [3, 4]]
x = copy.deepcopy(l)
```

### Comparing lists
```python
a = [7, 2]
b = [7, 2, 9]
a == b # False
a <= b # True
a < b  # True
```

### Iterating multiple sequences with zp
```python
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']
for n, l in zip(a, b):
  print(n, ':', l)

t = list(zip(a, b))
d = dict(zip(a, b))
```

### Comprehension with lists
```python
l = [1, 2, 3, 4, 5]
l = [n for n in range(1, 6)]
l = [n-1 for n in range(1, 6)]
l = [n for n in range(1, 6) if n % 2 == 0]
rows = range(1, 10)
cols = range(1, 10)
cells = [(row, col) for row in rows for col in cols]

for row, col in cells:
  print(row, ', ' col)
```

### Tuples vs Lists
* Tuples use less space
* You can't overwrite tuples by mistake
* You can't use lists as dictionary keys
* There are no tuple comprehensions

### Dictionaries
```python
empty = {}
f = {'a' : 1, 'b': 2, 'c': 3}
f = dict(a=1, b=2, c=3)

f = dict([['a', 1], ['b', 2], ['c', 3]]) 
# f is {'a', 1, 'b', 2, 'c', 3}

f = dict([('a', 1), ('b', 2), ('c', 3)]) 

f = dict((['a', 1], ['b', 2], ['c', 3])) 
```

### Changing dictionary entries
```python
f = {'a' : 1, 'b': 2, 'c': 3}
f['a'] = 4
```

### Getting an item
```python
if 'a' in items:
  print('a is in the items\'s kys')

item = items.get('a', -1)

item = items.get('a') # if it doesn't exist None will be returned
```

### Keys in dictionary
```python
k = ditionary.keys()
x = list(k)
```


### Values of dictionary
```python
v = list(dictionary.values())
```

### Getting all items in a dictionary
```python
items = list(dictionary.items())
```

### Length of a dictionary
```python
len(dictionary)
```

### Combining dictionaries (unicorn glitter)
```python
f1 = {'a' : 1, 'b': 2}
f2 = {'b' : 3, 'c': 4}
third = {**f1, **f2}
{'a': 1, 'b': 2, 'c': 4}
```

### Combining dictionaries with update
```python
f1 = {'a' : 1, 'b': 2}
f2 = {'b' : 3, 'c': 4}
f1.update(f2)
```

### Deleting an item by del from dictionary
```python
f2 = {'b' : 3, 'c': 4}
del f2['b']
```

### Deleting an item with pop
```python
f2 = {'b' : 3, 'c': 4}
x = f2.pop('b')
y = f2.pop('g', 6)
```

### Deleting all items with clear
```python
f2 = {'b' : 3, 'c': 4}
f2.clear()
```

### Testing the existenc of a key in a dictionary
```python
if 'b' in f2:
  print("b exists in f2")
```

### Copying a dictionary
```python
c = f2.copy() # shallow copy
```

### Deep copying a dictionary
```python
import copy
c = copy.deepcopy(f2)
```

### Comparison of dictionaries
```python
a == b
a != b
# a <= b not supported
# a < b not supported
```

### Iterating over dictionaries
```python
for k in d:
  print("Key is ", k)

for v in d.values():
  print("Value is ", v)

for key, value in d.items():
  print(key, ': ', value)
```

### Dictionary comprehensions
```python
vowels = "aeiou"
w = 'this is a long sentence'
c = {letter: w.count(letter) for letter in w}
c = {letter: w.count(letter) for letter in set(w)}
c = {letter: w.count(letter) for letter in set(w) if letter in vowels}
```

### Sets
```python
even_numbers = {2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7}
empty = set()
```

### Sets from other structures
```python
e = set('letters')
e = set(['a', 'b', 'a', 'c', 'd'])
e = set(('a', 'b', 'c', 'd'))
e = set({'a': 1, 'b': 2, 'c': 3})
```

### Length of sets
```python
e = set('letters')
len(e)
```

### Adding an item to a set
```python
s.add('b')
```

### Removing an item from the set
```python
s.remove('b')
```

### Iterating items in a set
```python
for v in s:
  print(v)
```

### Testing a value's existence in a set
```python
if v in items:
  print(v, ' exists in items')
```

### Intersection operator with sets
```python
a = {'a', 'b', 'c'}
b = {'a', 'd', 'e'}
if a & b:
  print('a and b has a common element')
if a.intersection(b):
  print('a and be has a common element')
```

### Union with sets
```python
c = a | b
c = a.union(b)
```

### Difference with sets
```python
c = a - b
c = a.difference(b)
```

### Symmetric difference with sets
```python
c = a ^ b
c = a.symmetric_difference(b)
```

### Subset with sets
```python
a <= b
a.issubset(b)
```

### Proper subset with sets
```python
a < b
```

### Superset with sets
```python
a >= b
a.issuperset(b)
```

### Proper superset with sets
```python
a > b
```

### Set comprehensions
```python
c = {n for n in range(1, 6) if n % 2 == 0}
```

### Immutable set
```python
a = frozenset([1, 2, 3])
a = frozenset({1, 2, 3})
```

### Functions
```python
def sample():
  pass

sample()

def is_cool():
  return True

if is_cool():
  print("Yes it is cool")

def add(n1, n2):
  return n1 + n2
```

### None
```python
if x is None:
  print('x is None')

x = None
if not x:
  print('x is False')
```

### Keyword arguments to functions
```python
def full_name(first, last, middle = ""):
  if middle:
    return first + " " + middle + " " + last
  else:
    return first + " " + last


full_name('John', 'Doe')
full_name(last='Doe', first='John')
full_name('John', middle="J", last="Doe")
```

* Do NOT use a mutable type as a default value

### Variable number of arguments
```python
def print_args(*args):
  print('Args: ', args)
print_args()
print_args('a', 1, 2)
```

```python
def print_args(**kwargs):
  print('Args: ', kwargs)
print_args(a='1', b=2, c=12.5)
```

### Keyword only arguments
```python
def process(data, *, start = 0, end = -1):
  pass
process(data, start=4, end=10)
```

### Docstring
```python
def complex(data):
  '''This a very complex method.
  You need to pass data that is big.
  This function will do a lot on the data
  '''
  pass
help(complex)
print(complex.__doc__)
```

### Functions are objects too
```python
def say_hello():
  print("Hello")

def run_func(func):
  func()

run_func(say_hello)

def add_values(a1, a2):
  print(a1+a2)

def run_func2(func, a1, a2):
  func(a1, a2)

run_func2(add_values, 1, 2)

def run_func3(func, *args):
  return func(*args)

run_func3(sum(1, 2, 3))
```

### Inner functions
```python
def outer(a, b):
  def inner(c, d):
    return c + d
  print(inner(a,b))
```

### Closures
```python
def outer2(a, b):
  def inner():
    return a + b
  return inner

a = outer2(5, 10)
b = outer2(2, 4)

print(a()) # 15
print(b()) # 6
```

### Lambda functions
```python
def process_words(words, func):
  for w in words:
    print(func(w))

process_words(['one', 'two', 'three'], lambda w: w.capitalize() + '!')
```

### Generator functions
```python
def my_range_func(first=0, last=100, step=1):
  n = first
  while n < last:
    yield n
    n += step

for i in my_range_func():
  print(i)
```
* Generators can be run only once

### Generator function comprehensions
```python
genobj = (pair for pair in zip(['a', 'b'], [1, 2]))
for p in genobj:
  print(p)
```

### Decorators
* To change functions which can not be modified
* A decorator is a function that takes one function and returns another function

```python
def document_func_call(func):
  def new_func(**args, **kwargs):
    print("Running function: ", func.__name__)
    print("Positional args: ", args)
    print("Keyword args: ", kwargs)
    result = func(*args, **kwargs)
    print("Result: ", result)
    return result
  return new_func
```

```python
def add_nums(a, b):
  return a + b

documented_add_nums = document_func_call(add_nums)
documented_add_nums(1, 2)
```

```python
@document_func_call
def add_nums(a, b):
  return a + b

add_nums(5, 10) # this function call is documented
```

### Namespaces and scopes
* In order to access a global variable, use `global` keyword within a function
```python
a = 1
def f():
  global a
  a = 2
```

* `locals()` returns a dictionary of the local namespace
* `globals()` returns a dictionary of the global namespace

### Handling exceptions
```python
try:
  x = 5 / 0
except:
  print("An error occurred")


try:
  p = int(answer)
  print(my_list[p])
except IndexError as err:
  print("Incorrect index position")
except ValueError as err:
  print("Not a valid integer")
```

### Making your own exceptions
```python
class MyOwnException(Exception):
  pass

if somethingIsWrong:
  raise MyOwnException('There is something wrong here')
```

### Object initialization
```python
class Person:
  def __init__(self, name):
    self.name = name

p = Person('John')
```

* Unlike other languages, __init__ is not a constructor, but
an initialization function. It can be overriden.

### Inheritance
```python
class Base:
  pass

class Derived(Base):
  pass

issubclass(Derived, Base)  # True
```

### Calling super's method
```python
class Derived(Base):
  def __init__(self):
    super().__init__()
```

### Multiple inheritance
```python
class Mule(Donkey, Horse):
  pass
```
* The methods are looked up first from Donkey, then Horse

### Mixins
* A super class that is used only as a helper method is called mixin
```python
class Helper():
  def printThis():
    import pprint
    pprint.print(vars(self))

class MyClass(Helper):
  pass

mine = MyCLass()
mine.printThis()
```

### Properties
```python
class Person():
  def __init__(self, name):
    self.my_hidden_name = name

  def get_name(self):
    return self.my_hidden_name

  def set_name(self, name):
    self.my_hidden_name = name

  name = property(get_name, set_name)

p = Person('John')
print(p.name)
p.name = 'Jane'
```

* Python mangles that start with `__` attributes

```python
class Person():
  def __init__(self, name):
    self.__name = name

  @property
  def name(self):
    return self.__name

  @property
  def name(self, name):
    self.__name = name

p = Person('John')
print(p.name)
p.name = 'Jane'
```

### Class attributes
* Class attributes are inherited by their child objects
```python
class Person:
  people_limit = 100

print(Person.people_limit)
p = Person()
print(p.people_limit)
Person.people_limit = 200
print(p.people_limit) # still 100
```

### Method types
* If there is no preceding decorator, it is an instance method. Its first argument should be `self`.
* If there is `@classmethod` decorator, it is a class method, its first argument should be `cls`
* If there is `@staticmethod` decorator, it is a static method, no specific first argument is required

### Class methods
```python
class Person():
  people_count = 0
  def __init__(self):
    Person.count += 1

  @classmethod
  def people_count(cls):
    return cls.people_count

p = Person()
p2 = Person()
print(Person.people_count())
```

### Static methods
```python
class Person():
  @staticmethod
  def info():
    print("Hello People")

Person.info()
```

### Magic methods
* `__eq__` for `==`
* `__ne__` for `!=`
* `__lt__` for `<`
* `__gt__` for `>`
* `__le__` for `<=`
* `__ge__` for `>=`

* `__add__` for `+`
* `__sub__` for `-`
* `__mul__` for `*`
* `__floordiv__` for `//`
* `__truediv__` for `/`
* `__mod__` for `%`
* `__pow__` for `**`

* `__str__` for `str(self)`
* `__repr__` for `repr(self)`
* `__len__` for `len(self)`

### Named tuples
```python
from collections import namedtuple
Person = namedtuple('Person', 'first last')
joe = Person('John', 'Doe')

d = {'first': 'John', 'last': 'Doe'}
joe2 = Person(**d)

joe3 = Person(first='John', last = 'Doe')
```

### Dataclasses
```python
from dataclasses import dataclass

@dataclass
class Person:
  first: str
  last: str
  age: int = -1

p = Person('John', 'Doe', 29)
```

### Modules
```python
import module_name
from random import choice
return choice(['a', 'b', 'c'])

import random
return random.choice(['a', 'b', 'c'])

import random as r
return r.choice([1, 2, 3])

from random import choice as c
return c([1, 2, 3, 4])
```

```python
from dir_name import module1, module2
```

### Module search path
```python
import sys
for place in sys.path:
  print(place)

# you can modify the search path
sys.path.insert(0, '/path/to/my/modules')
```

### Relative Imports
```python
from .. import my_module # parent directory
from . import my_module  # current directory
from ..sibling_dir import my_module # ../sibling_dir
```

### Handling missing keys with setdefault
* `setdefault` sets a default value for a given key if it doesn't exist already
```python
d = {'a': 1, 'b': 2}
d.setdefault('c', 3) # now c has a value of 3 since it doesn't exist
d.setdefault('a', 12) # a's value will not change, since a already exists
```

### Handling missing keys with defaultdict
```python
from collections import defaultdict
d = defaultdict(int) # now any missing key will return 0
def my_own_default():
  return -1
d2 = defaultdict(my_own_default)
d3 = defaultdict(lambda: -1)
```

### Counting items
```python
from collections import Counter
l = ['a', 'b', 'a', 'c', 'a', 'b']
c = Counter(l) # {'a': 3, 'b': 2, 'c': 1}
print(c.most_common()) # ordered in descending order
print(c.most_common(1)) # [('a': 3)]
```

* You can combine and subtract counters
```python
c1 & c2
c1 + c2
c1 - c2
c1 | c2
```

### Deque
```python
from collections import deque
dq = deque('ala')
dq.popleft() == dq.pop()
```

### Iterating over multiple sources
```python
import itertools
for i in itertools.chain(['a', 'b'], [1, 2, 3]):
  print(i)
```

### Cycling infinitely over a source
```python
import itertools
for i in itertools.cycle([1, 2]):
  print(i)
```

### Accumulating numbers
```python
import itertools
for i in itertools.accumulate([1, 2, 3, 4, 5]):
  print(i) # i is the accumulated sum of all the numbers so far

def multiple(a, b):
  return a * b
for i in itertools.accumulate([1, 2, 3, 4, 5], multiple):
  print(i) # i is the multiplied accumulation of all the numbers so far
```

### Printing nicely
```python
from pprint import pprint
pprint({'a': 1, 'b': 2})
```

### Sampling from a list
```python
from random import sample
sample([1, 2, 3, 4, 5, 6, 7], 3)
```

### Getting a random numbers 
```python
from random import randint
x = randint(1, 10)

from random import randrange
x = randrange(1, 10, 2)

from random import random
x = random()
```

### Unicode characters
```python
print('\U0001F600')
# http://www.unicode.org/charts/charindex.html
print("\N{grinning face}")

import unicodedata
name = unicodedata.name('\U0001F600')
print(name) # GRINNING FACE
value = unicodedata.lookup(name)
```

### Encode
```python
smiley = '\U0001F600'
x = smiley.encode('utf-8')
print(len(x))
# ignore characters that can't be encoded
smiley.encode('ascii', 'ignore')
# replace unknown characters with ?
smiley.encode('ascii', 'replace')
# produce a python unicode string, like unicode escape
smiley.encode('ascii', 'backslashreplace')
# for html-safe strings
smiley.encode('ascii', 'xmlcharrefreplace') 
```

### Decode
```python
smiley = '\U0001F600'
x = smiley.encode('utf-8')
y = x.decode('utf-8')
y == smiley
y2 = x.decode('latin-1') # weird characters
y3 = x.decode('windows-1252') # weird chars
```

### HTML Entities
```python
import html
html.unescape('&egrave;')
html.unescape('&#233;')
html.unescape('&#xe9;')

from html.entities import html5
html5["egrave"]
html5["egrave;"]

import html
char = '\u00e9'
dec_value = ord(char)
html.entities.codepoint2name[dec_value]
```

### Unicode normalization
```python
import unicodedata
normalized = unicodedata.normalize('NFC', text)
```

### Regular expressions
```python
import re
result = re.match('pattern', text)

pattern = re.compile('pattern')
result = pattern.match(text)
```

* `search()` returns the first match
* `findall()` returns the list of all non-overlapping matches
* `split()` splits at matches with pattern and returns a list
* `sub()` takes another replacement argument, and changes all parts of source that are matched by pattern to replacement

```python
import re
m = re.match('pattern', text)
if m:
  print(m.group())

if m:= re.match('pattern', text):
  print(m.group())
```

### Finding first match with search()
```python
import re
m = re.search('pattern', text)
if m:
  print(m.group())
```

### Finding all matches with findall()
```python
import re
m = re.findall('pattern', text) # list
```

### Split at matches with split()
```python
import re
m = re.split('pattern', text)
```


### Replace at matches with sub()
```python
import re
m = re.sub('pattern1', 'pattern2', text)
```

### Special regular expression characters
* `\d` digit
* `\D` non-digit
* `\w` alphanumeric character
* `\W` non-alphanumeric character
* `\s` whitespace character
* `\S` non-whitespace character
* `\b` a word boundary
* `\B` a non-word boundary

### Printable strings
```python
import string
print(string.printable)
```

### bytes and bytearray
* `bytes` is immutable
* `bytearray` is mutable
```python
blist = [1, 5, 230, 255]
b = bytes(blist)
b2 = bytearray(blist)
b2[1] = 19 
```

### Converting binary data with struct
* `>` means big-endian
* `<` means little-endian

* `x` skip a byte
* `b` signed byte
* `B` unsigned byte
* `h` signed short integer
* `H` unsigned short integer
* `i` signed integer
* `I` unsigned integer
* `l` signed long
* `L` unsigned long
* `Q` unsigned long long
* `f` float
* `d` double
* `p` count and characters
* `s` characters

```python
struct.unpack('>2L', data)
struct.unpack('>16x2L', data)
```

### Convert bytes/strings with binascii
```python
import binascii
valid_header = b'\x89PNG\r\n\x1a\n'
print(binascii.hexlify(valid_header))
```

### Bit operators
* `&`, `|`, `^`, `~`, `<<`, `>>`

### Leap year
```python
import calendar
calendar.isleap(1900)
calendar.isleap(2000)
```

### Dates and times
```python
from datetime import date

today = date.today()
print(today.isoformat())

halloween = date(2018, 10, 31)

from datetime import time
noon = time(12, 0, 0)

from datetime import datetime
birthday = datetime(2005, 1, 1, 18, 34, 20, 0)
print(birthday.isoformat())

now = datetime.now()

today = date.today()
noon_today = datetime.combine(today, time(12, 0, 0))
```

### Using time module
```python
import time
now = time.time() # number of seconds since epoch, Jan 1 1970

time.ctime(now) # date time string

time.localtime(now) # time.struct_time

time.gmtime(now) # time.struct_time

now2 = time.mktime(time.localtime(now)) # back to number of seconds since epoch
```

### strftime
```python
import time
fmt = "%A, %B %d, %Y : T %I:%M:%S%p"
t = time.localtime()
time.strftime(fmt, t)

from datetime import date
today = date.today()
today.strftime(fmt) # only the date parts are filled

from datetime import time
now = time(10, 40, 32)
now.strftime(fmt) # only time part is filled
```

### strptime
```python
import time

fmt='%Y-%m-%d'
time.strptime(text, fmt)
```

* To change month names etc.. change the locale

```python
import locale
from datetime import date
h = date(2018, 10, 18)
local.setlocale(locale.LC_TIME, "fr_FR")
h.strftime("%A %B %d")
```

* To get the locale names
```python
import locale
names = locale.locale_alias_keys()
```

### Create or open a file
```python
file_obj = open(path, mode)
```
* `w` for writing
* `r` for reading
* `x` for writing only if it doesn't exist
* `a` for appending if the file exists

* `t` for text (or nothing, the default is text)
* `b` means for binary

```python
f = open('/tmp/file.txt', 'w')
print("Hello World!", file=fout)
f.close()
```

### Writing text to a file
```python
f = open(path, 'w')
f.write("Text")
# print("Text", file=f, sep='', end='')
f.close()
```

### Reading from a file
```python
f = open('input.txt', 'rt' )
buffer_size = 32
all_buffer = ''
while True:
  buff = f.read(buffer_size)
  if not buff:
    break
  all_buffer += buff

f.close()
```

* You can read a line with `readline`
* You can read the whole file with `read`

```python
all_buffer = ''
f = open('input.txt', 'r')
for line in f:
  all_buffer += line
f.close()
```

```python
f = open('input.txt', 'r')
lines = f.readlines()
f.close()
```

### Writing a binary file with write
```python
data = bytes(range(0, 256))
f = open('output.bin', 'wb')
f.write(data)
f.close()
```

### Reading a binary file with read
```python
f = open('input.bin', 'rb')
```

### Close files automatically with with
```python
with open('file.txt', 'r') as f:
  lines = f.readlines()
```

### Change position in the file with seek()
```python
f = open('file.txt', 'r')
f.tell() # where we are in the file
f.seek(200) # go to 200th byte in the file
```

* `seek(offset, origin)` where
  * if `origin` is 0, start from the beginning of the file
  * if `origin` is 1, start from the current position of the file
  * if `origin` is 2, start from the end of the file

```
import os
os.SEEK_SET
os.SEEK_CUR
os.SEEK_END
```

### File and path operations
```python
import os
os.path.exists('path/to/file')
os.path.isfile('path/to/file')
os.path.isdir('path/to/dir')
os.path.isabs('/path/to/file')
```

### Copying a file
```python
import shutil
shutil.copy(source, target)
shutil.move(source, target)
```

### Renaming a file
```python
import os
os.rename(source, target)
```

### Creating hard and soft links
```python
os.link(source, target)
os.path.islink(target) # True

os.symlink(source, target)
os.path.islink(target) # True
```

### Changing permissions with chmod
```python
import os
os.chmod(path, 0o400)

import stat
os.chmod(path, stat.S_IRUSR)
```

### Changing ownership with chown
```python
os.chown(path, new_uid, new_gid)
```

### Deleting a file with remove
```python
os.remove(path)
```

### Creating a directory
```python
os.mkdir('/path/to/dir')
```

### Deleting a directory
```python
os.rmdir(dir_path)
```

#### Listing directory contents
```python
os.listdir(dir_path)
```

### Changing current directory
```python
os.chdir(new_path)
```

### Listing matching files with glob
```python
import glob
l = glob.glob('m*')
```

### Getting absolute path
```python
os.path.abspath(path)
```

### Get a symbolic link's real path name
```python
os.path.realpath(symbolic_link_path)
```

### Building a path with os.path.join
```python
import os
f = os.path.join('part1', 'part2')
```

### Use pathlib (portable way of handling paths)
```python
from pathlib import Path
f = Path('part1') / 'part2' / 'final.txt'
f.name   # final.txt
f.suffix # .txt
f.stem   # final
```

### BytesIO and StringIO
* When you have in-memory data and have a function that expects a file
```python
from io import BytesIO
fp = BytesIO(data)
```

### Getting pid of a process
```python
import os
os.getpid()
```

### Getting the current directory
```python
os.getcwd()
```

### Getting the user id and group id
```python
os.getuid()
os.getgid()
```

### Create a process with subprocess
```python
import subprocess
# runs the commands in shell and returns string
r = subprocess.getoutput('date')
r = subprocess.getoutput('date -u | wc')
```

```python
# does not run the command in shell and returns bytes
r = subprocess.check_output(['date', '-u'])
```

```python
# gets both status and output
r = subprocess.getstatusoutput('date -u | wc')
```

```python
# only if you are interested in the status
r = subprocess.call('date')
```

```python
# shell=True is needed to parse date -u properly
r = subprocess.call('date -u', shell=True)
# alternative
r = subprocess.call(['date', '-u'])
```

### Create a process with multiprocessing
```python
import multiprocessing
import os

def another_process(mesg):
  print("Process id %s: %s" % (os.getpid(), mesg))

for n in range(4):
  p = multiprocessing.Process(target=another_process,
    args = f"{n}")
  p.start()
  # to kill the process prematurely
  # p.terminate()
```

### Get system info
```python
import os
os.uname()
os.getloadavg()
os.cpu_count()

os.system('date -u')
```

### Queues with multiprocessing
```python
import multiprocessing as m
import random

def consumer(input_queue):
  while True:
    item = input_queue.get()
    # process the item
    input_queue.task_done()

queue = m.JoinableQueue()
proc = m.Process(target=consumer, args=(queue,))
proc.daemon = True
proc.start()

def producer(output_queue):
  for i in range(1, 4):
    item = str(random.randint(100))
    output_queue.put(item)

producer(queue)
queue.join()
```

### Threads
```python
import threading
import queue
import random

def producer(queue):
  def i in range(1,5):
    queue.put(str(random.randint(100)))

def consumer(queue):
  while True:
    item = queue.get()
    # process item
    queue.task_done()

queue = queue.Queue()
for n in range(5):
  t = threading.Thread(target=producer, args=(queue,))
  t.start()

consumer(queue)
queue.join()
```

### Processes vs Threads
* Use threads for I/O bound tasks (threading does not scale in python)
* Use processes for CPU bound tasks

### concurrent.futures
```python
from concurrent import futures

def process_func(arg):
  # process arg and return a value

with futures.ThreadPoolExecutor(10) as tex:
  results = tex.map(process_func, args)

with futures.ProcessPoolExecutor(10) as pex:
  results = pex.map(process_func, args)

with futures.ThreadPoolExecutor(10) as tex:
  tasks = [tex.submit(process_func, value) for value in args]
  for f in futures.as_completed(tasks):
    yield f.result()
```

### CSV
```python
import csv

with open('data.csv', 'rt') as data_file:
  cin = csv.reader(data_file)
  data = [row for row in cin]

with open('data.csv', 'rt') as data_file:
  cin = csv.reader(data_files, fieldnames=['name', 'age'])
  data = [row for row in cin]

with open('data.csv', 'wt') as data_file:
  cout = csv.DictWriter(data_file, ['name', 'age'])
  cout.writeheader()
  cout.writerows(data)
```

### JSON
```python
data = {
  "john": {
    "age": "20",
    "name": "john doe",
    "from": "usa"
  }
}

with open('data.txt', 'wt') as fout:
  json.dump(data, fout)

with open('data.txt', 'rt') as fin:
  data = json.load(fin)

import datetime
now = datetime.datetime.utcnow()
json.dumps(now, default=str)
```

### Config files (ini files)
```python
import configparser
cfg = configparser.ConfigParser()
cfg.read('my_config.ini')
print(cfg['section']['option'])
```

