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

```
