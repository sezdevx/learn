let d = {'a' : 1, 'b' : 2, 'c' : 3 }

echo d
echo d.a
let d.a = 'one'
echo d.a

let test = remove(d, 'a')
echo d

echo get(d, 'a', 'default')
echo get(d, 'b', 'default')

echo has_key(d, 'a')
echo has_key(d, 'b')

echo items(d)


