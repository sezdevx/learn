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

* To select the next defun (function)
```
Meta-Ctrl-h
```

* To select the next paragraph
```
Meta-h
```

## Moving Around

* To move to the end or the beginning of a buffer
```
Meta-< : Beginning of the buffer
Meta-> : End of the buffer
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

## Searching and replacing
* To search forward
```
Ctrl-s
```

* To search reverse
```
Ctrl-r
```

* To regex search forward
```
Meta-Ctrl-s
```

* To regex search reverse
```
Meta-Ctrl-r
```

* To replace a string
```
Meta-x replace-string
```

* To replace a string requiring confirmation for each occurrence
```
Meta-x query-replace
y: to replace
n: to skip
!: to continue without asking
```

* To list lines containing a string
```
Meta-x list-matching-lines
Meta-s o
Meta-x occur
```

* To delete lines containing a string
```
Meta-x delete-matching-lines
```

* To find major points of interest
```
Meta-x imenu
```

* To go to a line
```
Meta-g Meta-g
```

* To go to a character position
```
Meta-g c
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

* Revert the buffer to its last saved state
```
Meta-x revert-buffer
```

* To open a file as hex-decimal 
```
Meta-x hexl-find-file
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

* To redo
```
Ctrl-g ;; cancel undo
Ctrl-x u
;; Ctrl-g again to change direction
```

* To repeat a command 8 times
```
Ctrl-u 8 cmd
Meta-8 cmd
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

* To delete a word to the left of the cursor
```
Meta-- Meta-d
```

* To repeat the last command
```
Ctrl-x z
Ctrl-x zzzzz : repeat the last command as long as we press z
```

## Macros
* To start and end recording a macro
```
Ctrl-x ( : start recording a macro
Ctrl-x ) : end recording the current macro
```

* To run the last recorded macro
```
Ctrl-x e
```

* To name the last recorded macro
```
Meta-x name-last-kbd-macro
Ctrl-x Ctrl-k n
```

* To bind the last recorded macro to a key
```
Ctrl-x Ctrl-k b
```

* To insert lisp code for a named macro
```
Meta-x insert-kbd-macro
```

* To use a named macro
```
Meta-x name_of_the_macro
```

## Bookmarks
* To record the current point
```
Ctrl-x r Space [register character; such as a,b,c,d etc...]
```

* To jump to a saved point
```
Ctrl-x r j [register character; such as a,b,c,d etc...]
```

* To record the contents of a region in a register
```
Ctrl-x r s [register character; such as a,b,c,d etc...]
```

* To insert the contents of a register 
```
Ctrl-x r i [register character; such as a,b,c,d etc...]
```

* To store a number in a register
```
Ctrl-x r n [register character; such as a,b,c,d etc...]
```

* To increase a number in a register
```
Ctrl-x r + [register character; such as a,b,c,d etc...]
```

* To record the current file as a permanent bookmark
```
Ctrl-x r m
```

* To jump to a file in the bookmarks list
```
Ctrl-x r b
```

* To list all files in the boomarks list
```
Ctrl-x r l
```

## Shell
* To run a shell program
```
Meta-|
```

* To run a shell in emacs
```
Meta-x shell
```

* To run a terminal in emacs
```
Meta-x term
```

* To go to line mode in terminal
```
Ctrl-c Ctrl-j
```

* To go back to char mode in terminal
```
Ctrl-c Ctrl-k
```

## Running Lisp
* To run a file in batch mode
```
emacs -batch -l input_file.el
```

## Help
* To list all key bindings starting with a key prefix
```
Ctrl-x Ctrl-h
; lists all key bindings starting with Ctrl-x1

```

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

* To display info about major mode and its key bindings
```
Ctrl-h m
```

* To display info
```
Ctrl-h i
```

## Elisp
* To run code in a selected region
```
Meta-x eval-region
```

* To run code in the whole file
```
Meta-x eval-buffer
```

## Miscellaneous

* To insert a literal tab character (rather than space for indentation purposes)
```
Ctrl-q TAB
```

* To see the coding system in use for the current buffer
```
Ctrl-h C
```

* To exit the emacs
```
Meta-x kill-emacs
```

* To display calendar
```
Meta-x calendar
```

* To display faces
```
Meta-x list-faces-display
```

* To count words, lines and characters
```
Meta-x count-words
```

* To show spaces
```
Meta-x whitespace-mode
```

## Programming

* Move forward to end of paragraph
```
Meta-}
```

* Move backward to start of paragrah
```
Meta-{
```

* To comment a selected region
```
Meta-;
```
