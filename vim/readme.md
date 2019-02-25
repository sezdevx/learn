## Basics
* Insert mode, normal mode
```
i: to enter into insert mode before the character under the cursor
a: to enter into insert mode after the character under the cursor
Esc " to exit the insert mode
```

* To open a file
```
" you can use tabs here
:e file_name
```
If a new file is opened, `[New File]` is displayed in the status bar.

* To save a file
```
:w
```

* To exit vim
```
:q
```

* To forcefully exit vim, discarding changes
```
:q!
```

* Dot command: Repeat the last change
```
.
```

* To delete the character under cursor
```
x
```

* To undo changes
```
u
```

* To undo changes in a line
```
U
```

* To undo the undo change
```
Ctrl-r
```

* To delete a line
```
dd
D: deletes till the end of line
```
* To delete a word
```
dw
```

* To delete to the end of word
```
de
```

* To add a new line below the current line and switch to insert mode
```
o
```

* To add a new line above the current line and switch to insert mode
```
O
```

* To indent a line
```
>G
```

* Write changes and exit
```
ZZ
```

* Navigation commands
```
h: left
l: right
j: down
k: up
```

* To get help
```
:help
:help subject
:help x
:help deleting
:help index
:help CTRL-A
:help i_CTRL-H # insert mode CTRL-H
:help -t # command line t option
:help v_u # visual mode command u
:help :quit # ex-mode commands
:help c_<Del> # command line editing
:help 'textwidth'
```

* To repeat a command n number of times
```
8k # go up 8 times
4j # go down 4 times
3a!<Esc> # !!! is inserted
3x # delete 3 characters
```

* To delete a word
```
dw
```

* To delete until the end of line
```
d$
```


* To delete a word multiple times
```
d3w: delete three words once
3dw: delete one word 3 times
```

* Change word
```
cw: delete a word and go into insert mode
cc: delete a line and go into insert mode
c$: delete till end of line and go into insert mode
C: delete till end of line and go into insert mode
```

* Move by word
```
w: move forward over a word
b: move backward over a word
```

* Move over line
```
$: end of line
End: real end of line
^: beginning of line
Home: real beginning of line
```

* Searching in a line
```
fy: search y to the right within the same line
Fy: search y to the left within the same line
ty: search y to the right but stop before the letter
Ty: search y to the left but stop after the letter
```

* Go to a line number
```
9G: go to line 9
180G: go to line 180
```

* To show line numbers
```
:set number: turn on line numbers
:set nonumber: turn off line numbers
```

* Display where you are in a status line
```
Ctrl-g: display a status line
```

* Scroll up and down
```
Ctrl-U: up half a screen
Ctrl-D: down half a screen
```

* To join lines
```
J
```

* To replace a character with a new character
```
rs: replace the current char with s
5ra: replace 5 chars with a
```

* Swap letter cases
```
~: change upper to lower case, lower to upper case
```

* Recording and stopping macros
```
qa: start recording a macro and store it in register a
q: stop recording the macro
@a: execute macro stored in a
```

* Simple search
```
/string: search string
n: find the next occurrence
/ then UP or DOWN to go over the history
:set hlsearch: to highlight search results
:nohlsearch
:set incsearch: do incremental search
:set noincsearch: do not do incremental search
?string: search string backward
?<Enter>: to change the search direction
N: reverse search and search again
```

* To paste
```
p: paste after
P: paste before
```

* Marking a point
```
ma: mark the current position into register a
`a: go to the mark point stored in a
'a: go to the line that contains the mark point stored in a
d'a: delete up until and including the line which contains the mark stored in a
d`a: delete up until the point which contains the mark stored in a
:marks: to list all the marks
    ': last place the cursor was
    ": where we were left last in this file
    [: start of last insert
    ]: end of last insert
```

* To copy
```
y motion: copies text rather than deletes (same as d)
Y: copies a single line the whole line
```

* Filtering
```
!motion command: to filter the part of the buffer
!10Gsort: sort the file till 10th line
!!sort: sort the entire file
!!ls: run ls and insert the ls command output
!!date: run date
```

* Editing another file
```
:vi newFile: closes the current file and opens the new file
:vi! newFile: if the current file changes are not saved and you want to disregard them
:write: save the changes
:view newFile: open the file in read-only mode
:write!: to force saving changes to read-only file
```

* Switching between open files
```
:next: next file
:next!: when there are changes
:previous: previous file
:Next: previous file
:previous!: when there are changes
:wprevious: write the current file and then go to the previous file
:rewind: first file
:first: first file
:last: last file
Ctrl-^: switch to the other file (alternate file)
```

* To force write when there are changes
```
:set autowire
:set noautowire
```

* To see which file you are on
```
:args
```

* To open a new window
```
:split
Ctrl-ww: to move to the other window
Ctrl-w Ctrl-w: same as Ctrl-ww
Ctrl-wj: go to down window if there is any
Ctrl-wk: to to up window if there is any
:q: close the window
Ctrl-wc: close the window
:split file: open a new window with the given file
:5 split: open a new window 5 lines heigh
:new: same as split except new file
:sbuffer number: split and open the buffer number in the split window
```

* Change window sizes
```
Ctrl-w+: increase by 1 line
Ctrl-w-: decrease by 1 line
Ctrl-w=: equalize
```

* Buffers
```
:buffers: list of buffers
 %: current buffer
 #: alternative buffer
 +: buffer is modified
 -: inactive buffer
 h: hidden buffer
:buffer 1: change to the buffer 1
:buffer 2: change to the buffer 2
:buffer filename: change to the buffer for the given file name
:bnext: next buffer
:sbnext: split and go to next buffer
:bprevious: previous buffer
:bNext: same as bprevious
:brewind: first buffer
:bfirst: first buffer
:blast: last buffer
:bmodified: go to the first modified buffer in the list
```

* Visual mode
```
v: enter the visual mode
V: visual mode by selects line by line
Ctrl-v: like v, but allows you to select a rectangle area
select text by moving cursor
d: to delete the selected text
D: to delete all lines, even if part of the line is selected
y: to copy
Y: to copy by lines
Esc: cancel visual mode
rx: replaces all selected text with character x
```

* To join lines
```
J
```

* Indenting
```
>: indents to the right by shift width
<: indents to the left by shift width
Ctrl-]: to go to function definition, works with tags
K: manual lookup, the one underneath the cursor
Ctrl-d: back up one shift width (when in insert mode)
=motion: indents selected text using vim's internal formatting
```

* Turn on syntax
```
:syntax on
" to learn the value of background
:set background?
:set background=light
" to set the type of syntax highlighting
:set filetype=c
" to learn file type of the current buffer
:set filetype?
```

* Locating things in source code
```
[Ctrl-I, ]Ctrl-I : search for a word under cursor
gd: search for a definition of a local variable
gD: search for a definition of a global variable
]Ctrl-D, [Ctrl-D: jump to a macro definition
[D, ]D, ]d, [D: display macro definition
%: on (, {, [ it finds the matching pair, also #ifdef with #endif
>%: shift the text within {} including {}s
>i{: shift the text within {} excluding {}s
K: runs the man for the word under the cursor
Ctrl-]: go to the definition of function the cursor is in
" Run ctags *.cc
:tags: to see the list of tags you traversed
Ctrl-t: go back to in the tag list history
:stag: split the window and go to the function definition
Ctrl-w]: split the window and go to the function definition
:tag: go to the function definition
:tag /regex: regular expression search
:tag /[dD]o_[Ff]ile: regexe search example
:tselect: to show all tags
```

* Makefiles
```
:set list: to show tabs and new lines
Ctrl-V<Tab>: if expandtab is set, to insert a tab
```






