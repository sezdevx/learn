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

## Buffers
* To kill the current buffer
```
:bdelete
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
```

* To go to the first buffer
```
:bf
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

## Windows
* To split a window horizontally
```
Ctrl-w s
```

* To split a window vertically
```
Ctrl-w v
```

* To cycle between windows
```
Ctrl-w w
Ctrl-w Ctrl-w
``

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

# Miscellaneous

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

* To cancel a command
```
Ctrl-c
```

* To explore a directory
```
:Explore path/to/dir
```

* To inspect the value of a variable
```
set path?
```


