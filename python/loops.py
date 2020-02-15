count = 1
while count < 5:
    print(count)
    count += 1

a = "abcqdefg"
i = 0
while i < len(a):
    if a[i] == 'q':
        break
    print(a[i], end = '')
    i += 1
print()


a = "abcqdefg"
i = 0
while i < len(a):
    if a[i] == 'q':
        i+=1 # without this it is an infinite loop
        continue
    print(a[i], end = '')
    i += 1
print()


a = "abcqdefg"
i = 0
while i < len(a):
    i += 1
    if a[i-1] == 'q':
        continue
    print(a[i-1], end = '')
print()


a = "abcdefg"
i = 0
while i < len(a):
    if a[i] == 'q':
        break
    print(a[i], end = '')
    i += 1
else:
    print("\nNo q is found")
print()

a = "abcqdefg"
for c in a:
    if c == 'q':
        break
    print(c, end = '')
print()

a = "abcqdefg"
for c in a:
    if c == 'q':
        continue
    print(c, end = '')
print()


a = "abcdefg"
for c in a:
    if c == 'q':
        break
    print(c, end = '')
else:
    print("\n No q is found")
print()


for a in range(0, 5):
    print(a, end = ',')
print()
for a in range(0, 10, 2):
    print(a, end = ',')
print()


