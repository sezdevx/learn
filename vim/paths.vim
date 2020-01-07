" relative path, depends on how you open the file
echo expand("%")

" absolute path
echo expand("%:p")

" path to the foo.txt in current directory
echo fnamemodify('foo.txt', ':p')

echo globpath('.', '*')

echo split(globpath('.', '*'), '\n')

echo split(globpath('~/learn', '**'), '\n')


