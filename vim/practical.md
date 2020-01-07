# Vim Tutorial

## Regions
* To select a region (enter the visual mode). Move your cursor to select.
```
v
```

* To select a region by line (enter the visual mode).
```
V
```

* To change the mark and point in a region. Continue moving cursor
```
o
```

* To select a rectangle like area (in visual mode)
```
Ctrl-v
```

* To cut the selected area
```
d
```

* To cut all the lines in the selected area, even if it is a partial match
```
D
```

* To copy the selected area
```
y
```

* To copy all the lines in the selected area
```
Y
```

* To cancel the selection and exit the visual mode
```
Esc
```

* To select till a searched text
```
v/searchTerm
```

* To copy content of the region to a register
```
"ay
```

* To paste from a register
```
"ap
:put a
```

* In insert mode to insert a register content
```
Ctrl-r a
```

* To process a set of specific lines
```
:1,5y  "copy lines from 1 to 5
:%y    "copy the whole buffer
:%d    "delete the whole buffer
```

## Moving around
* To go to the beginning of file
```
gg
:0
```

* To go to the end of file
```
G
:$
```

* To go one page down
```
Ctrl-f
```

* To go one page up
```
Ctrl-b
```

* To go half page down
```
Ctrl-d
```

* To go half page up
```
Ctrl-u
```

* Align current line in the center
```
zz
```

* To move one word forward
```
w
```

* To move one word backward
```
b
```

* To go to the next sentence
```
)
```

* To go to the previous sentence
```
(
```

* To go to the next paragraph
```
}
```

* To go to the previous paragraph
```
{
```

* To move to the top, middle and bottom of the screen
```
H
M
L
```

* To go to a specific line number
```
9G
:9
180G
:180
```

* To show/hide line numbers
```
:set number
:set nonumber
```

* To display where you are in the status line
```
Ctrl-g
```

* To go to the end of line
```
$
```

* To go to the beginning of line
```
0
```

* To go to the first non-blank character in line
```
^
```

* To jump to the matching paranthesis
```
%
```

## Searching and Replacing

* To search forward
```
/string
```

* To find the next occurrence
```
n
```

* To change the search direction
```
N
```

* To search backward
```
?string
```

* To change the search direction
```
?Enter
```

* To search the word under cursor
```
*
```

* To highlight on/off search results
```
:set hlsearch
:nohlsearch
```

* To go over the search history
```
Type / and then up and down arrows
```

* To replace string globally and ask for confirmation before each replacement
```
:%s/target/replacement/gc
```

* To replace string globally
```
:%s/target/replacement/g
```

* To list lines containing a string
```
:g/string
```

* To delete all lines containing a string
```
:g/string/d
```

* To go to a specific character position
```
:goto 123
```

## Help
* To display help for a particular command
```
:h command
```

* To display help index
```
:h index
```

* To display help on u command when in visual mode
```
:help v_u
```

* To get help on Ctrl-h in insert mode
```
:help i_CTRL-H
```

* To get help on Ctrl-h in mini buffer
```
:help c_CTRL-F
```

* To get help on command line options
```
:help -t
```

* To get help on ex command
```
:help :quit
```

* To get help on command line (mini buffer)
```
:help cmdline
```

## Buffers
* To kill the current buffer
```
:bdelete
:bd
```

* Switch to the next buffer
```
:bnext
:bn
```

* Switch to the previous buffer
```
:bprevious
:bp
```

* To list all buffers
```
:ls
:buffers
```

* To switch to the first buffer
```
:b1
```

* To switch between the last two buffers
```
Ctrl-6
```

* To go to the last buffer
```
:bl
:blast
```

* To go to the first buffer
```
:bf
:bfirst
```

## Cut, Copy, Paste, Undo, Redo
* To undo
```
u
```

* To redo
```
Ctrl-r
```

* To cut a line
```
dd
```

* To copy a line
```
yy
```

* To paste
```
p
P
```

## Editing
* To insert a new line and switch to insert mode
```
o
```

* To get into the insert mode
```
i
```

* To go to the end of line and switch to insert mode
```
A
```

* To go to the beginning of line and switch to insert mode
```
I
```

* To cut a line
```
dd
```

* To delete a line until the end of line
```
d$
```

* To change a word
```
cw
```

* To delete a line till the end and go into insert mode
```
c$
C
```

* To change a word before the cursor
```
cb
```

* To paste
```
y
```

* To join with the next line
```
J
```

* To switch back to normal mode
```
Esc
```

* To delete the character under cursor
```
x
```

* To indent a line
```
>G
```

* To indent a line in normal mode
```
>>
3>> indent 3 times
```

* To unindent a line in normal mode
```
<<
```

* In insert mode to indent
```
Ctrl-T
```

* In insert mode to unindent
```
Ctrl-D
```

* To write changes and exit
```
ZZ
```

* To delete a single character
```
x
```

## Shell
* To run a shell program
```
:!ls
```

* To go to shell temporarily. Type exit when you are done, you will go back to vim.
```
:shell
```

* To execute a shell script and insert its output to the current file
```
:read ! ls
```

* To process the current buffer with a shell program
```
:!cat %
% refers to the path of the current file
```

* To process a range of the current buffer with a shell program
```
:1,5write !more
```

* To execute a vim script
```
:source file.vim
```

## Files
* To open a file
```
:e path/to/file
:edit path/to/file
```

* To reload a file discarding all changes
```
:edit!
```

* To save a file
```
:w
```

* To exit vim
```
:q
```

* To force exit vim
```
:q!
```

* To read a file and insert it into the current buffer
```
:read /path/to/file
```

* To open a file in read-only mode
```
:view /path/to/file
```

## Macros
* To start recording a macro and store it in register a
```
qa
```

* To stop recording a macro
```
q
```

* To execute a macro stored in register a
```
@a
```

## Bookmarks
* To mark the current position in register a
```
ma
```

* To go to the exact position stored in register a
```
`a
```

* To go to the line stored in register a
```
'a
```

* To delete up until the position stored in register a
```
d`a
```

* To list all marks
```
:marks
```

## Key bindings 

* Display key bindings for normal mode
```
:nmap 
```

* Display key bindings for visual mode
```
:vmap
```

* Display key bindings for insert mode
```
:imap
```

* Display key bindings for all modes
```
:map
```

* Do a non-recursive mapping
```
nmap x dd
" non-recursive mapping, \ is mapped to default value of x, instead of dd
" normal mode
nnoremap \ x
```

* To do a mapping for special keys
```
nnoremap <space>m x
nnoremap <c-k> dd
nnoremap <c-k> A<cr>hello
```

* To assign a leader key to be used in mappings
```
let mapleader=','
nnoremap <leader>d dd
```

* To disable a key
```
inoremap <left> <nop>
```

* To define a key mapping local to the buffer
```
nnoremap <buffer> <leader>x dd
```

## Windows
* To split a window horizontally
```
Ctrl-w s
```

* To split a window vertically
```
Ctrl-w v
```

* To create a new file in a horizontally split window
```
:sp filename
```

* To create a new file in a vertically split window
```
:vsp filename
```

* To cycle between windows
```
Ctrl-w w
Ctrl-w Ctrl-w
```

* To close current window
```
Ctrl-w q
```

* To focus on the window on the left
```
Ctrl-w h
```

* To focus on the window on the right
```
Ctrl-w l
```

* To focus on the window on the top
```
Ctrl-w k
```

* To focus on the window on the bottom
```
Ctrl-w j
```

* To maximize height of the active window
```
Ctrl-w _
```

* To maximie width of the active window
```
Ctrl-w |
```

* To equalize window sizes
```
Ctrl-w =
```

* Set the active window height to N rows
```
N Ctrl-w _
```

* Set the active window width to N columns
```
N Ctrl-w |
```

* To keep the active window only
```
:only
```

* Increase window size by 1
```
Ctrl-w +
```

* Decrease window size by 1
```
Ctrl-w -
```

# Miscellaneous

* To repeat a command
```
.
```

* To insert the full path of the file into the buffer
```
:read !echo %:p
```

* To see all register contents
```
:reg
```

* To see contents of a particular register
```
:reg "a
```

* To literally insert a tab character
```
Ctrl-V TAB
```

* To insert any character with its number
```
Ctrl-v065
```

* To cancel a command
```
Ctrl-c
```

* To explore a directory
```
:Explore path/to/dir
```

* In insert mode to switch to normal mode and execute a single mode and return back to insert mode
```
Ctrl-o
e.g. Ctrl-o0 to go the beginning of line
```

* To inspect the value of a variable
```
set path?
```

## Programming
* Search for a definition of a local variable
```
gd
```

* Search for a definition of a global variable
```
gD
```

* To create an abbreviation in insert mode
```
iabbrev adn and
iabbrev tehn then
iabbrev iff if ()<cr><up><left>
iabbrev @@ my_username@company.com
```

* To create buffer-local abbreviations
```
iabbrev <buffer> --- &mdash
```

* To create abbreviations specific to a language
```
autocmd FileType python :iabbrev <buffer> iff if:<left>
```

## Command Line Mini Buffer
* To delete the word before the cursor
```
Ctrl-w
```

* To delete everything before the cursor
```
Ctrl-u
```

## Insert mode
* To insert a tab character literally
```
Ctrl-v TAB
```

* To indent 
```
Ctrl-t
```

* To unindent
```
Ctrl-d
```

* To insert a new line
```
Ctrl-j
```

* To insert a register content
```
Ctrl-r
```

## Vimscript
* To write a file to disk as soon as you edit one
```
autocmd BufNewFile * :write
```

* To write all text files to disk as soon as you edit one
```
autocmd BufNewFile *.txt :write
```

* To auto indent html files right before saving them to disk
```
autocmd BufWritePre *.html :normal gg=G
```

* To prevent duplicate autocmds when reloading scripts, group them
```
augroup pythongroup
  autocmd!
  autocmd FileType html nnoremap <buffer> <localleader>f Vatzf
augroup
```

* Movement mappings
```
" dp will delete within parantheses
onnoremap p i(
```

* Normal mode command
```
:normal gg
```

* Execute a string as vim script
```
:execute "write"
```

* Variables
```
let foo = "bar"
echo foo
set textwidth=80
echo &textwidth
let &textwidth=100
let &textwidth = &textwidth + 10
```

* Local options
```
let &l:number = 1
```

* Registers as variables
```
let @a = "hello"
echo @a
```

* Buffer local variables
```
let b:hello = "world"
```

* To permanently show a message im messages
```
:echom "Permanent message"
:messages
```

* If conditions
```
if 1
  echom "One"
endif

if 0
  echom "Zero"
elseif 1
  echom "One"
endif

if 0 > 1
  echom "Impossible"
endif

setignorecase
if "foo" == "Foo"
  echom "yes, vim ignores case"
endif

" case-insensitive comparison
if "foo" ==? "FOO"
  echom "This is going to be displayed"
endif

" case sensitive comparison
if "foo" ==# "FOO"
  echom "This is NOT going to be displayed"
endif
```

* Functions
```
function Hello()
  return "Hello World"
endfunction

echom Hello()
call Hello()

function HelloW(who)
  return "Hello " . who
endfunction

echom HelloW("World")

function VarArgExample(...)
  echom a:0
  echom a:1
  echom a:000
endfunction

call VarArgExample("a", "b")
```

* Arithmetic
```
echo 2 * 2.0
echo 3 / 2
echo 3 / 2.0
```

* String functions
```
echo strlen("foo")
echo len("foo")
echo split("one two three")
echo split("one,two,three", ",")
echo join(["one", "two", "three"], ";")
echo tolower("FOO")
echo toupper("foo")
```

* To force normal mode to execute a command even though the command is remapped to something else
```
" even if G is remapped to something else, the default will be executed
normal! G
```

* To enter regular expression the way it works in other languages
```
" start with \v
execute "normal! gg" . "/\vfor .+" 
" :help magic for more information 
```

* Loops
```
while 1 > 0
  call functionName()
endwhile

let words = { 1 : "one", 2: "two", 3: "three" }
for [key, val] in items(words)
  echo key . ': ' . val
endfor
```


