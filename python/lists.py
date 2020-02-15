empty = []
print(empty)
empty = list()
print(empty)

a = (1, 2, 3)
b = list(a)
print(b)

b = list(range(1, 11))
print(b)
print(b[2:6])
print(b[0])
print(b[-1])
print(b[0::2])
print(b[1::2])

c = b[:]
d = b
print("Copy of the original list: ", c)
print(id(c))
print(id(b))
print(id(d))

r = b[::-1]
print(r)
print(b)
print(id(b), " vs ", id(r))

# in-place reverse
b.reverse()
print(b)

# lists are mutable
b.reverse()
print(b)
b[0] = 11
print(b)
b.append('string')
print(b)
b.insert(0, 'One')
print(b)
c = b * 3
print(c)

a = list(range(0, 5))
b = list(range(5, 11))
print(a)
a.extend(b)
print(a)

a = list(range(0, 5))
b = list(range(5, 11))
print(a)
a += b
print(a)
a[5:11] = []
print(a)
a[5:11] = range(5, 11)
print(a)

print(a)
a.remove(1)
print(a)
a.remove(5)
print(a)

b = a.pop()
print(b)
print(a)

b = a.pop()
print(b)
print(a)

b = a.pop(0)
print(b)
print(a)

b = a.pop(0)
print(b)
print(a)

b = a.pop(0)
print(b)
print(a)

a = list(range(0, 11))
print(a)
a.clear()
print(a)

a = list(range(0, 11))
print(a.index(1))
try:
    print(a.index(-1))
except:
    print("No -1 is found in the list")

a = ["one", "two", "three"]
if "two" in a:
    print("two exists in the list")
if not "four" in a:
    print("four does not exist in the list")

a = ["one", "two", "three", "one", "two", "one"]
print("one in the list: ", a.count('one'))
print("three in the list: ", a.count('three'))
print("two in the list: ", a.count('two'))

a = list(range(0, 11))
import random
random.shuffle(a)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)


# copying a list
b = a.copy()
b = a[::]
b = list(a)

a = [0, 1, [2, 3], [4, [5, 6]]]
print(a)
b = a.copy()
b[2][0] = "Did I modify a too? Yes I did"
b[0] = "Only B"
print(a)
print(b)

print()

a = [0, 1, [2, 3], [4, [5, 6]]]
print(a)
import copy
b = copy.deepcopy(a)
b[2][0] = "Did I modify a too? Yes I did"
b[0] = "Only B"
print(a)
print(b)


a = [1]
b = [1, 2]
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)

a = [3]
b = [1, 2]
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)

a = [1, 3]
b = [1, 2]
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)


a = list(range(1, 11))
for x in a:
    print(x, end = "")
print()
