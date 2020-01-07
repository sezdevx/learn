let words = { 1 : "one", 2: "two", 3: "three" }
for [key, val] in items(words)
  echo key . ': ' . val
endfor

for item in ['one', 'two', 'three']
  echo item
endfor

let items = ['one', 'two', 'three']
echo items
echo items[0]
echo items[1]
echo items[0:1]


let items ="onetwothree"
echo items[0]
echo items[1]
echo items[0:5]
echo items[-1]
echo items[-2:]

let first = ['1', '2', '3']
let second = ['4', '5']
echo first + second

echo first
call add(first, '7')
echo first

echo "length of the list is "  . len(first)

echo get(first, 122, 'default')
echo get(first, 1, 'default')
echo index(first, '1')
echo index(first, 'f')
echo reverse(first)
echo join(first, '-')

let c = 1
let total = 0
while c <= len(first)
  let total += first[c-1]
  let c = c + 1
endwhile

echo total
