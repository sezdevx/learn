# Online resources
* [emacs rocks](http://emacsrocks.com/)
* [xah emacs](http://ergoemacs.org/)
* [what the emacs.d](http://whattheemacsd.com/)
* [Emacs Elisp Programming](https://github.com/caiorss/Emacs-Elisp-Programming)
* [Emacs Wiki](https://www.emacswiki.org/emacs/SiteMap)
* [Emacs Starter Kits](https://github.com/eschulte/emacs-starter-kit)
* [Starter Kits](https://www.emacswiki.org/emacs/StarterKits)

# Emacs Lisp (elisp)
To run the examples below `emacs -batch -l file_name.el`

## Somewhat useful modes
* whitespace-mode

## [lorem.el](lorem.el)
* Defining functions
* Assigning a global key to a function
* Use it with `load-file` from within emacs
* Format time string, current time
* current-kill, current-buffer, condition-case
* thing-at-point
* insert

## [emacs.el](emacs.el)
* insert: inserts text to the current buffer
* switch-to-buffer: switch to another buffer with the name or buffer object
* current-buffer: current buffer
* other-buffer: other buffer (based on some order)
* buffer-string: to get the string of the whole buffer
* defun: to define a function
* getenv, concat, split-string
* extract documentation of a function
* read-string, read-file-name, read-directory-name
* using interactive form to get user input for function arguments


## [simple_arithmetic.el](simple_arithmetic.el)
* using message to output to stderr
* using print to output to stdout
* using format to format data
* using arithmetic expression
* defining a variable and setting a value to it

## [functions.el](functions.el)
* defining and calling functions
* reading input from user
* use of mapcar function
* applying function to a list
* use of cdr and car
* setq function

## [lists.el](lists.el)
* mapcar function
* quote function
* add-to-list function
* cons, cdr, car

## [sequences.el](sequences.el)
* length
* elt
* copy-sequence
* reverse
* sort

## [arrays.el](arrays.el)
* arrayp
* fillarray
* make-vector
* vectorp

## [load_paths.el](load_paths.el)
* load-path list
* mapcar function
* message

## [version_info.el](version_info.el)
* emacs version
* major version
* minor version

## [numbers.el](numbers.el)
* Comparison
* max, min functions
* number, integer, float predicates

## [strings.el](strings.el)
* string predicate
* concat
* make-string function
* characters
* substring

# Emacs packages to install
```
ggtags ; used with (gtags from global apt package)
```

# Emacs
* To debug configuration
```
emacs --debug-init
```

* To run a file in batch mode
```
emacs -batch -l lisp_code.el
```

* To list packages
```
Meta-x package-list-packages
; to install a package : i
; to unmark a package: u
; to delete a package: d
; to quit the interface: q
```

* To select a region
```
Ctrl-Space
```

* To change the mark and point in a region
```
Ctrl-x Ctrl-x
```

* To mark (select) the whole buffer
```
Ctrl-x h
```

* To move to right or left the selected region
```
; after selecting the region
Ctrl-x TAB
; then left or right arrows to indent
```

* To count number of lines, words and characters in a region
```
Meta-=
```

* To (cut) delete the whole region
```
Ctrl-w
```

* To copy the whole region without killing it
```
Meta-w
```

* To run a shell command with the region as input
```
Meta-|
```

* To move to the end or beginning of the buffer
```
Meta <: Move to the beginning of the buffer
Meta >: Move to the end of the buffer
Alt-Home: Move to the beginning of the buffer
Alt-End: Move to the end of the buffer
```

* Page down and up
```
Ctrl-v: Page down
Meta-v: Page up
Meta-Ctrl-V: Page down in the other window
Ctrl-l: Redisplay the screen where current line is in the middle
```

* To add a literal tab character
```
Ctrl-q TAB
```

* To go to a specific line number
```
Meta-g g: Go to the given line number
```

* Undo
```
Ctrl-x u
Ctrl-/
```

* Repeat a command
```
Ctrl-u 8 cmd
```

* To show the command associated with a key combination
```
Ctrl-h k
; then type the key
```

* To find the doc string of a function
```
Meta-x describe-function
Ctrl-h f
```

* To find the doc string of a variable
```
Meta-x describe-variable
Ctrl-h v
```

* To search a command with a partial name
```
Ctrl-h a
```

* To see all key bindings
```
Ctrl-h b
Meta-x describe-bindings
```

* To make the buffer read-only
```
Ctrl-x Ctrl-q
```

* To find and open a file
```
Ctrl-x Ctrl-f
```

* To open/insert/create a new line
```
Ctrl-o
```

* To cancel a command in the minibuffer
```
Ctrl-g
```

* To display colors and faces
```
Meta-x list-colors-display
Meta-x list-faces-display
```

* The completion
```
TAB: Complete text as much as possible
Space: Complete text up to end of word
?: Display list of possible completions
Return: TAB + enter the command if it is completed
```

* To repeat the last command
```
Ctrl-x z: repeat the last command once
Ctrl-x zzzzz: repeat the last command 5 times
```

* Split windows
```
Ctrl-x 2: split top/bottom
Ctrl-x 3: split left/right
Ctrl-x 1: unsplit all
Ctrl-x 0: delete current one
Ctrl-x o: move to the other window
```

```
Ctrl-x {: shrink window to the left
Ctrl-x }: enlarge windows to the right
Ctrl-x ^: make the window larger vertically
```

* To run a command
```
Meta-x: type the command name
```

* Managing buffer
```
Ctrl-x k: kill buffer
Ctrl-x b: switch to buffer
Ctrl-x Ctrl-b: list all buffers
Ctrl-x Ctrl-s: save buffer to a file
Ctrl-x Ctrl-w: save to a specific file
```

* To go to the next or previous buffer
```
Ctrl-x left: to go to the previous buffer
Ctrl-x right: to go to the next buffer
```

* Moving around
```
Ctrl-f: one character forward
Ctrl-b: one character backward
Ctrl-n: next line
Ctrl-p: previous line
Meta-f: move one word forward
Meta-b: move one word backward
Meta-{: previous paragraph
Meta-}: next paragraph
Ctrl-a: beginning of current line
Ctrl-e: end of current line
```

* To see the documentation of a variable
```
F1 v VARIABLE_NAME
```

* Some variables are buffer local, e.g. `tab-width`. Such variables
may be set to have default values.
```
(setq-default tab-width 2)
```

* To load an emacs file
```
(load-file "~/file.el")
```

* To load a library
```
; require searches through list of directories in load-path
(require 'module)
(module-mode)
```

* To delete a characters
```
Ctrl-d: delete a single character to the right of the point
Meta-\: delete all space and whitespace around point
Ctrl-k: delete current line
;;Ctrl-x Ctrl-o: delete all empty lines around the current line
Meta-d: delete a word to the right of the point
```

* Yanking (Pasting) text
```
Ctrl-y: yank the most recently killed text
Ctrl-u Ctrl-y: same as Ctrl-y, but cursor is going to be at the beginning of the text
```

* To find the face at point
```
Ctrl-u Ctrl-x =
```

* To highlight a symbol at point
```
Meta-s .
```

* To see indentation symbol for a given line
```
; go to the line you want to indent
Ctrl-c Ctrl-o
```

* To run a terminal in emacs
```
Meta-x term
# to scroll up or down go into line mode (C-c C-j)
# (C-c C-k) to go back into char mode
Meta-x shell
```

* To find occurrences of a regular expression
```
Meta-s o
; to move to the next occurrence in the list
Ctrl-x `
```

## Emacs Lisp

* The following are the same
```
(setq x 1)
(set (quote x) 1)
```

* To run (evaluate) an interactive lisp command line interface
```
Meta-x ielm
```

* To run a shell (like ielm)
```
; https://www.gnu.org/software/emacs/manual/html_mono/eshell.html
Meta-x eshell
```

* To evaluate a selected region
```
Meta-x eval-region
```

* To evaluate the whole buffer
```
Meta-x eval-buffer
```

* To print a message. The message will also appear in `*Messages*` buffer
```
(message "My name is %s" "Joe")
```

* To see the `*Messages*` buffer
```
Ctrl-h e
```

* Arithmetic
```
(+ 4 5 1)  ; 10
(- 9 2)    ; 7
(/ 8 2)    ; 4
(/ 7 2.0)  ; 3.5
(% 8 4)    ; 2
(expt 2 3) ; 8
```

* Conversion
```
(float 3) ; 3.0
(truncate 3.3) ; 3
(floor 3.3) ; 3
(ceiling 3.3) ; 4
(round 3.6) ; 4
(round 3.3) ; 3
(string-to-number "3")
(number-to-string 3)
```

* In lisp nill is false, everything else is true. Empty list () is same as nil.
```
(if () "yes" "no")     ; "no"
(if nil "yes" "no")    ; "no"
(if '() "yes" "no")    ; "no"
(if (list) "yes" "no") ; "no"

(if t "yes" "no")      ; "yes"
(if 0 "yes" "no")      ; "yes"
(if "" "yes" "no")     ; "yes"
(if [] "yes" "no")     ; "yes"
```

* and and or
```
(and t nil)  ; nil
(or t nil)   ; t
(and t nil t nil) ; nil
```

* Comparing strings
```
(equal "abc" "abc")        ; t
(string-equal "abc" "abc") ; t
(string-equal "abc" "Abc") ; nil
(string-equal "abc" 'abc)  ; t
```

* Generic comparisons
```
(equal 3 3)      ; t
(equal 3.0 3.0)  ; t
(equal "e" "e")  ; t
(equal '(3 4 5) '(3 4 5)) ; t
(equal '(3 4 5) '(3 4 "5")) ; t
(= 3 4) ; nil
(= 3 3) ; t
(not (= 3 4)) ; t
```

* Global variables
```
(setq x 1)
(setq x 1 y 2 z 3) ; multiple assignments
```

* Local variables
```
(let (a b)
    (setq a 1)
    (setq b 5)
    (+ a b)
); 6
(let ((a 1) (b 5)) (+ a b) ) ; 6
```

* If then else
```
(if (< 3 4) "3 < 4" "! 3 < 4") ; 3 < 4
```

* When
```
(when (< 3 4) (message "3 < 4") (message "3 is less than 4"))
```

* To group block of expressions
```
(progn (message "3 < 4") (message "3 is less than 4"))
```

* Loops
```
(setq x 1)
(while (< x 4)
    (print (format "x is %d" x))
    (setq x (+ 1 x))
)
```

* To define a function
```
(defun myFunc()
    "A simple function"
    (message "Hello World")
)
```

* To define a command
```
(defun writeHello()
    "Insert Hello to buffer"
    (interactive)
    (insert "Hello")
 )
```

* To evaluate an expression in the buffer. Place the cursor to the end of the expression.
```
Alt-x eval-last-sexp
Ctrl-x Ctrl-e
```

* Text processing functions
```
; Cursor Position
(point) ; current cursor position
(region-beginning) ; position of beginning of the selection
(region-end) ; position of the end of the selection
(line-beginning-position)
(line-end-position)
(message "%s" (current-word)); prints the current word
```

```
; Move Cursor
(goto-char 39)
(forward-char 5)
(backward-char 5)
(search-forward "text")
(search-backward "text")
(re-search-forward "[0-9]*")
(re-search-backward "[0-9]*")
(skip-chars-forward "a-z") ; move cursor to the first char that is NOT a...z
(skip-chars-backward "a-z")
```

```
; Change Buffer
(delete-char 5) ; delete 5 chars from current position
(delete-region 5 10) ; delete from 5 to 10
(insert "Hello World")
(setq x (buffer-substring 30 300)) ; x is assigned to substring of the buffer
(capitalize-region 30 300)
(erase-buffer) ; erase the current buffer
```

```
; String
(length "abcdefg")
(substring "abcdefg" 2 5) ; cde
(replace-regexp-in-string "[0-9]+" "N" "123abc") ; Nabc
```

```
; Buffer
(buffer-name)
(buffer-file-name) ; full path of the buffer
(set-buffer "*Messages*") ; switch to the *Messages* buffer
(save-buffer)
(kill-buffer "*Messages*") ; close this buffer
(with-current-buffer "myNewBuffer" ; temporarily sets the current working buffer
    ; do somethig with the buffer
)
```

```
; File
(find-file "~/") ; open the home directory
(write-file "~/myNewFile.txt") ; save the current buffer as the given path
(insert-file-contents "~/myNewFile.txt")
(append-to-file 0 10 "~/myNewFile.txt") ; append part of of this buffer to the file
(rename-file "~/myNewFile.txt" "~/myRealNewFile.txt")
(copy-file "~/myNewFile.txt" "~/myCopiedFile.txt")
(delete-file "~/myCopiedFile.txt")
(file-name-directory "/tmp/whatever/file.txt") ; /tmp/whatever
(file-name-nondirectory "/tmp/whatever/file.txt") ; file.txt
(file-name-extension "/tmp/whatever/file.txt") ; txt
(file-name-sans-extension "/tmp/whatever/file.txt") ;/tmp/whatever/file
```

```
; Cursor
(message "%d" (point)) ; current cursor position
(message "%d" (region-beginning)) ; beginning of selected region
(message "%d" (region-end)) ; end of selected region
(message "%d" (point-min)) ; beginning of the buffer
(message "%d" (point-max)) ; end of the buffer
(goto-char 300) ; go to char position 300
(forward-char 3) ; move cursor 3 chars forward
(backward-char 3) ; move cursor 3 chars backward
(beginning-of-line); move the cursor to the beginning of line
(end-of-line); move the cursor to the end of line
(search-forward "foo") ; move forward to the first matched foo string
(search-backward "foo") ; move backward to the first matched foo string
(re-search-forward "[0-9]+") ; move forward to the first matched regex
(re-search-backward "[0-9]+") ; move backward to the first matched regex
```

```
; get current line
(message "%s" (buffer-substring-no-properties (line-beginning-position) (line-end-position) ))
; get things at the point: filename, word, symbol, list, sexp, defun, url, email, sentence ...
(setq str (thing-at-point 'filename))
(message "%d" (line-beginning-position))
(message "%d" (line-end-position))
(forward-line -1) ; previous line
(forward-line 1) ; next line
```

```
; cut/copy/paste
(kill-region 1 100) ; cuts the first 100 chars
(copy-region-as-kill 1 100) ; copies the first 100 chars
(kill-new "this is copied to kill ring")
(yank) ; to paste from the kill ring
```

```
; to get the universal argument C-u and then a number into your function
; http://ergoemacs.org/emacs/elisp_universal_argument.html
(defun f (x)
  "example"
  (interactive "P")
  (message "%s" x)
)
```

```
(defun r (searchStr)
  "example"
  (interactive "sEnter search string:")
  (let ((case-fold-search t)) ; make it case insensitive

  (goto-char (point-min))

  (while (search-forward searchStr nil t)
    (replace-match "Hello World"))
  )
)
```

```
; to process marked dired files
; use m to mark them, use u to unmark them
(defun dired-process-file ()
  "apply a function to all marked files in dired."
  (interactive)
  (require 'dired)
  (mapc 'customProcessFile (dired-get-marked-files))
)
```
