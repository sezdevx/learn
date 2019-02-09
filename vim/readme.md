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
```
* To delete a word
```
dw
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
```

