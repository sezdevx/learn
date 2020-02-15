empty = ()
print(empty)

empty = tuple()
print(empty)

one = "One",
print(one)

one = ("One",)
print(one)
print(type(one))

not_a_tuple = ("Not a tuple")
print(not_a_tuple)
print(type(not_a_tuple))

a, b, c = "One", "Two", "Three"
print(a, b, c)

a, b, c = ("Uno", "Dos" , "Tres")
print(a, b, c)

print(a, b)
a, b = b, a
print(a, b)

a = ['one', 'two', 'three']
b = tuple(a)
print(b)

b += 'four',
print(b)

a = ('one',) * 5
print(a)

a = (1,)
b = (1, 2)
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)

a = (3,)
b = (1, 2)
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)

a = (1, 3)
b = (1, 2)
print(a, " vs ", b)
print(a == b)
print(a <= b)
print(a >= b)

# tuples are immutable
a = (1, 3)
# ILLEGAL
# a[0] = 3
print(id(a))
a += (3, 4)
print(id(a))

