# Emacs Tutorial

## Regions

* To select a region. Move cursor to start selecting.
```
Ctrl-Space
```

* To change the mark and point in a region. Continue moving cursor
```
Ctrl-x Ctrl-x
```

* To mark the whole buffer
```
Ctrl-x h
```

* To cut the selected region
```
Ctrl-w
```

* To copy the selected region
```
Meta-w
```

## Moving Around

* To move to the end or the beginning of a buffer
```
Meta < : Beginning of the buffer
Meta > : End of the buffer
```

* Page down and up
```
Ctrl-v : Page down
Meta-v : Page up
Ctrl-l : Redisplay the screen where the current line is in the middle
```

* One word forward
```
Meta-f
```

* One word backward
```
Meta-b
```

* One paragraph forward
```
Meta-}
```

* One paragraph backward
```
Meta-{
```

* To go to a specific line number
```
Meta-g g
```

* To move to the beginning of the current line
```
Ctrl-a
```

* To move to the end of the current line
```
Ctrl-e
```

## Searching
* To search
```
Ctrl-s
```

* To replace a string
```
Meta-x replace-string
```

## Editing
* To insert a new line
```
Ctrl-o
```

## Files
* To open a file
```
Ctrl-x Ctrl-f
```

* Save the current buffer
```
Ctrl-x Ctrl-s
```

* Write the buffer to a file
```
Ctrl-x Ctrl-w
```

## Windows
* Splitting windows
```
Ctrl-x 2 : split top/bottom
Ctrl-x 3 : split left/right
Ctrl-x 1 : unsplit all
Ctrl-x 0 : delete the current window
```

* Move between windows
```
Ctrl-x o
```

* Resize windows
```
Ctrl-x { : shrink window 
Ctrl-x } : enlarge window
Ctrl-x ^ : enlarge window vertically
(shrink-window) : shrink window vertically
Ctrl-u -5 Ctrl-x ^: shrink window 5 lines vertically
```

## Buffers
* Kill the current buffer
```
Ctrl-x k
```

* Switch to another buffer
```
Ctrl-x b
```

* Go to next or previous buffer
```
Ctrl-x left-arrow
Ctrl-x right-arrow
```

* List all buffers
```
Ctrl-x Ctrl-b
```

## Minibuffer
* To cancel a command in the minibuffer
```
Ctrl-g
```

* To run a command
```
Meta-x: type the command name
```

## Cut, Copy, Paste, Undo, Redo
* To undo
```
Ctrl-x u
Ctrl-/
```

* To repeat a command 8 times
```
Ctrl-u 8 cmd
```

* To cut a line
```
Ctrl-k
```

* To paste
```
Ctrl-y
```

* To paste a previous pasted text
```
Meta-y (right after a yank operation)
```

* To delete a character to the right of the cursor
```
Ctrl-d
```

* To delete a word to the right of the cursor
```
Meta-d
```

* To repeat the last command
```
Ctrl-x z
Ctrl-x zzzzz : repeat the last command as long as we press z
```

## Special Cases

* To insert a literal tab character (rather than space for indentation purposes)
```
Ctrl-q TAB
```

## Shell
* To run a shell program
```
Meta-|
```

* To run a terminal in emacs
```
Meta-x term
```

* To go to line mode
```
Ctrl-c Ctrl-j
```

* To go back to char mode
```
Ctrl-c Ctrl-k
```

## Running Lisp
* To run a file in batch mode
```
emacs -batch -l input_file.el
```

## Help
* To show the command associated with a key combination
```
Ctrl-h k [key-combination]
```

* To display the doc string of a function
```
Ctrl-h f [function-name]
```

* To display the doc string of a variable
```
Ctrl-h v [variable-name]
```

* To search a command with a partial name
```
Ctrl-h a
```

* To list all key bindings
```
Ctrl-h b
```

