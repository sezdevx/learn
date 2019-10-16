* [Vim Wiki](https://vim.fandom.com/wiki/Vim_Tips_Wiki)

# Pro Vim
* To go into command line window `q:` or while in command line mode `<C-f>`

* To list the command history `:history`

* To get documentation `:h text-objects`

* Display key bindings for normal mode `:nmap`

* Display key bindings for visual mode `:vmap`

* Display key bindings for insert mode `:imap`

* Display key bindings for all modes `:map`

* To display help index `:h index`

* To insert a file into the buffer `:read path-file-file`

* To insert output of a shell script `:read !ls -a | grep -v '^\.'`

* Go to the next buffer `:bn`

* Go to the previous buffer `:bp`

* List all buffers `:ls`

* Go to a specific buffer (buffer 1) `:b1`

* Switch between the last two buffers `<C-6>` or `<C-^>`

* Go to the first buffer `:bf`

* Go to the last buffer `:bl`

* Go to the next modified buffer `:bm`

* To write the buffer `:w`

* To quit the vim `:q`

* To quit and discard all changes `:qa!`

* To write all modified buffers and quit `:wqa`

* To create a new buffer in a horizonally split window `:new`

* To create a new buffer within the current window `:enew`

* To create a new buffer within a vertical split window `:vnew`

* To create a new buffer within a new tab `:tabnew`

* To get the full file path `%:p` e.g. `read !echo %:p` will insert
the full path of the file into the current file.

* You can change the current working directory of vim using
`cd ~/projects/x`

* To go to the header of the full path `cd %:p:h`

* The general editing command structure `[count] {operator} {[count] motion | text object}`

* To paste from a register `"2p`

* To see register contents `:reg`

* To do block editing in visual block mode `I`, or to append in block mode `A`

* To append to end of line in visual block mode press `$` before selecting the block,
so vim knows you are going to append to the end of each line.

* (Closing the buffer but keeping the window)[https://vim.fandom.com/wiki/Deleting_a_buffer_without_closing_the_window#Alternative_Script]

# Practical Vim
* Dot command repeat the last changes `.`

* To delete a single character `x`

* Delete 10 characters `10x`

* Undo: `u`

* Delete a whole line and copy it into paste buffer `dd`

* Copy line into paste buffer `yy`

* Paste from paste buffer below cursor `p`

* Paste from paste buffer above cursor 'P'

* Left `h`

* Down `j`

* Up `k`

* Right `l`

* Go to the end of file `G`

* Go to the beginning of file `gg`

* Go to line 10 `10G`

* Indent line `>[Right Arrow]`

* Go to the end of line `$`

* Go to the beginning of line `0`

* Go to the beginning of line with a first non-whitespace character `^`.

* Go to the end of line and start editing `A`

* Go to the beginning of line and start editing `I`

* Start editing after cursor `a`

* Start editing before cursor `i`

* Insert a new line before current line and start editing `O`

* Insert a new line below current line and start editing `o`

* To delete text and start editing `c`

* To change a word forward `cw`

* To change a word backwards `cb`

* To delete till the end of line and start editing `C`

* To delete the whole line and start editing `S`

* To delete a single character and start editing `s`

* Move forward one word `w`

* Move backward one word `b`

* Delete one word forward `dw`

* Delete one word backward `db`

* Search forward a character in the current line `f`{char}

* Search backward a character in the current line `f`{char}

* Search forward a character in the current line the cursor is placed on the left of the char `t`{char}

* Search backward a character in the current line the cursor is placed on the left of the char `t`{char}

* Repeat the last char search `;`

* Repeat the last char search in the opposite direction `,`

* Repeat the last char search but reverse direction `;`

* Scan file forward for next match `/pattern`

* Scan file backward for next match `?pattern`

* Go to the next match `n`

* Go to the next match but reverse direction `N`

* Substitute target with replacement `:s/target/replacement`

* Substitute target with replacement globally `:%s/target/replacement/g`

* To search the word under the cursor `*`

* To increase or decrease a number under the cursor `Ctrl-a` and `Ctrl-x`
Prefix it with a number to increase or decrease that much.

* Change `c`

* Delete `d`

* Yank (copy) into register `y`

* Make lower case `gu`

* Make upper case `gU`

* Swap case `g~`

* Shift right `>`

* Shift left `<`

* Auto indent `=`

* Filter lines through an external program `!`

* Insert mode commands. `Ctrl-h` to delete back one character.
`Ctrl-w` to delete back one word. `Ctrl-u` to delete back to start of line.

* Switch to normal mode `Esc` or `Ctrl-[`

* Switch to insert normal mode `Ctrl-o`, a single command can be executed
but then it returns back to insert mode.

* Redraw screen with current line in the middle of window `zz`

* In insert mode paste from register `Ctrl-r{register}`

* In insert mode evaluate an expression and insert the result `Ctr-l=`

* To insert any character with its number `Ctrl-v065` inserts A, or
`Ctrl-vu263a` inserts ☺.

* To see the numeric value of any character `ga` shows the character
under cursor

* To literally insert a tab character `Ctrl-V<Tab>`

* To insert a digraph `Ctrl-k{char1}{char2}`. To view digraphs `:digraphs`.

* To replace characters `R`

* To replace characters where a tab is considered as space `gR`

* Visual mode character wise `v`

* Visual mode line wise `V`

* Block wise visual mode `Ctrl-v`

* Go to the other end of selection while in visual mode `o`

* In visual mode you can use commands such as `w` or `b` for forward and backward word selection.

* Delete lines from 1 to 5 `:1,5delete`

* Copy lines from 1 to 6 `:1,5yank`

* To go to the 23rd line `:23`

* To go to the end of file `:$`

* To print the current line `:print` `:p`

* To print 3rd line `:3p`

* To print from 2nd line to 5th line `:2,5p`

* To print the whole file `:%p` or `:1,$p`

* To print current line to 2 lines down from current line `:.,.+2p`

* To go to a line marked in a `:'a`

* To copy lines from 5,10 to line 1 `:5,10copy1` or `:5,10t1`

* To duplicate the current line `:t.`

* To copy the current line to the end of file `:t$`

* To copy the currently selected text to the beginning of the file `:'<,'>t0`

* To move lines `:[range]move{address}` e.g. `:1,2move$` or `:1,2m$`

* To run a command in normal mode for multiple lines `:'<,'>normal.`

* To enter a semicolon at the end of each line for all lines `:%normal A;`

* To repeat the last ex command `@:`, after that you can press `@@` to repeat that again.

* To choose a color scheme `:colorscheme [color_scheme_name]`

* To list all possible completions `Ctrl-d`

* To adjust command completions use `:command-complete`

* While in command line copy the word under cursor and insert it into command prompt `Ctrl-r Ctrl-w`

* To search for the current word under the cursor `*`

* To go through history of commands `:` and the press `<up>` and `<down>` keys.

* To go through history of search history `/` and then press `<up>` and `<down>` keys.

* To cancel an operation in command line `Ctrl-c`

* To get into the command line window `q:`

* While editing a command you can get into command line window by pressing `Ctrl-f`

* To get into the search history window `q/`

* Executing programs from the shell `!ls`

* In command line `%` refers to the current file name

* To go to shell temporarily `:shell` and when you type exit you get back to vim

* To pass the contents of the file to a command `:write ! sh` will execute
each line in the file in a sub-shell.

* To sort a range of lines `:2,$!sort -t',' -k2`, this will replace the lines too
so that the range is sorted.

* To execute a shell command and insert its output `read !ls`

* Execute a shell command with the range of lines from the current buffer as input
`1,5write !more`

* To execute a vim script on a file `:source batch.vim`

* To navigate between files provided through command line `:first` `:last` `:next` `:previous`

* To get the command line arguments `:args`

* To execute a batch command on all files given through command line `:argdo source batch.vim`

* To see a list of files `:ls`

* To navigate buffers `:bnext` `:bfirst` `:blast` `:bprevious` or `:buffer N` or `:buffer {bufferName}`

* To delete a buffer `:buffer N` or `:buffer {bufferName}`

* Populate args and open files `:args *.txt`

* To reload a file discarding `:edit!`

* To write all modified buffers `:wall`

* To close all windows discarding changes `:qall!`

* To split a window `Ctrl-w s` horizontally, to split a window vertically `Ctrl-w v`

* To split horizontally and open a file `:split {file}`

* To split vertically and open a file `:vsplit {file}`

* To cycle between windows `Ctrl-w w` or `Ctrl-w Ctrl-w`

* To focus on the window on the left `Ctrl-w h`

* To focus on the window on the right `Ctrl-w l`

* To focus on the window on the top `Ctrl-w k`

* To focus on the window on the bottom `Ctrl-w j`

* To close the active window `:close`

* To keep the active window only open window `:only`

* Equalize window sizes `Ctrl-w =`

* Maximize height of the active window `Ctrl-w _`

* Maximize width of the active window `Ctrl-w |`

* Set the active window height to N rows `N Ctrl-w _`

* Set the active window width to N rows `N Ctrl-w |`

* To edit a file in a tab `:tabedit {filename}`

* To move the current file into a tab `Ctrl-w T`

* To close a tab `:tabclose`

* To keep an active tab as the only tab `:tabonly`

* To go to next tab `gt` or `:tabnext`

* To go to previous tab `gT` or `:tabprevious`

* To go to N tab `Ngt` or `:tabnext N`

* To move the active tab to the end `:tabmove`

* To move the active tab to the beginning `:tabmove 0`

* To get the current working directory `:pwd`

* To open a file relative to a current buffer `:edit %:h<TAB>`

* Add a path `:set path+=~/`

* Search in a path `:find fileName`

* You can open a directory using `:edit dirName`

* To open the directory of the current buffer `:Explore`

* To go between the last two buffers `Ctrl-^` or `Ctrl-6`

* To display line numbers `:set numbers`

* To go up and down in display lines (not necessarily rea lines) `gk` `gj`

* To go to the first character of the display line `g0`

* To go to the end of a display line `g$`

* To go to the first non-blank line of a display line `g^`

* To go to the next WORD `W`

* To select with a search enter visual mode with `v` then `/text`.

* You can also delete with text search `d/text` deletes from current cursor till text.

* Visual text object selection after pressing `v` `a)` or `i)` while within ().
Others `a}`, `a]`, `a>`, `a'`, `a"` `at` to select xml tags.

* Other text object selections `iw`, `iW`, `is`, `ip` or `aw` `aW` `as` `ap`.

* Marking the current cursor location `m{a-zA-z}` to jump to the marker
 line `'m`, to go the exact cursor location use backtick instead of '.

* To jump to the matching parenthesis `%`

* To go the position before the last jump within current file `''`

* To list all jumps `:jumps`

* To move between jumps `Ctrl-o` back `Ctrl-i` (or `TAB`) forward.

* To go to a specific line `[count]G`

* To jump to the top, middle and bottom of the screen `H` `M` and `L`

* To jump to the file name under the cursor `gf`

* To use with `gf` `:set suffixesadd+=.cc`

* To inspect the path `:set path?`​

* To jump the definition of the word under cursor `Ctrl ]`

* Go to next and previous sentences `(` `)`

* Go to the next and previous paragraphs `{` `}`

* To see the change list `:changes`

* To undo and then redo `u` then `Ctrl r`

* Do a global mark that works across files `mV` and then `'V` to go to that file and line.
Lowecase letters do local markers, uppercase letters mark global markers.

* Paste before `P`, paste after `p`

* To copy to a register `"ayW` to paste from register a `"ap`

* To inspect the contents of a register `:reg "a`

* Lowercase letter registers replaces the contents, whereas upper case letter
registers append the contents.

* To paste but go to the other side of the paste `gp` or `gP`

* In insert mode you can insert any register by `Ctrl r` and then type the register name.

* Paste from system clipboard `"+p`

* To record a macro to a register `qa`, to stop recording the macro `q`. To look
at the contents of the register `:reg a` and to run it `@a` or `@@` to invoke
the last macro. To append to a register that already holds a macro use uppercase
letter, e.g. `qA`

* To swap case `~`

* You can execute a macro on selected text using `:normal @a`

* To save changes to all files `:wall`

* To write and go to next file `:wnext`

* To run a macro in all files in args `:argdo normal @a`

* Assign a value to a variable `:let i=0`

* Show the contents of a variable `:echo i`

* Increment a variable `:let i+=1`

* To put the contents of a register `:put a`. You can edit the line
and store (yank) it back to a register with `0"ay$dd`.

* To ignore case in searches `:set ignorecase`. Per search pattern you
can use `\c` to ignore case and `\C` to force case sensitivity.

* You can also set the smartcase option `:set smartcase` where if
the pattern is all lowercase, the search is case insensitive, but
a single upper case letter forces ignoring case.

* To use a regular expression like perl's use `\v` flag e.g. `/\v([0-9]{3})

* To go to the next search result `n`

* To change the search direction `N`

* To capture a regular expression `/\v(\w+)\_s+\1`, to make sure that
we are talking about words `/\v<(\w+)>\_s+\1

* To turn off the special meanings of `. + *` symbols, use `\V` e.g.
`/Vhttp:\/\/domain.name/`, but you still need to escape some
characters like `\/ \?`

* To replace all occurrences of a searched text `:%s/test/text/g`.
To replace just one occurrence in the current line `:s/test/text`.
To replace all occurrences in a single line `:s/test/text/g`.
In order to confirm before a change `:%s/test/text/gc`

* Leaving the search text field blank tells vim to use the last
pattern.



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
:set nolist: hide tabs and new line indicators
Ctrl-V<Tab>: if expandtab is set, to insert a tab
```

* How to sort multiple lines
```
go to the start of the list
mark this location with ma
go to the bottom of the list
!'a sort

In visual mode
Press V and select the text
!sort
```

* Making
```
:make
:cnext (next error)
:clast
:cprevious
:cfirst (:crewind)
:cnfile (next error in the second file in the list)
:cc (current error)
:clist (list of errors)
:clist 3,5 (errors 3 through 5)
:clist 5, (errors 5 through the end)
:cquit (exit with an error code 1)
```

* Grepping
```
:grep estimate *.c
then move among results using cc, clist clast etc...
```

* Abbreviatins
```
:abbreviate us using
:abbreviate (to list all abbreviations)
to insert a space in abbreviation use <space>
```

* Mapping keys
```
" Insert {} around a word under the cursor
:map <F4> i{<Esc>ea}<Esc>
:map (list all mappings)
```

* Controlling how backspace key works
```
:set backspace=indent
:set backspace=eol
:set backspace=start
:set backspace=indent,eol (1)
:set backspace=indent,eol,start (2)
```

* To see which files are being read
```
:version
```

* Auto commands
```
" only for c, c++ files
:autocmd FileType c,cpp set formatoptions=croql
    \nocindent comments&
" for all files
:autocmd FileType * set formatoptions=tcql
```

* Setting the text width
```
:set textwidth=80
```

* Showing line numbers
```
:set number
```

* Printing lines
```
:1,5 print (print lines 1 through 5)
:print (print current line)
:. print (print current line)
:1,$ print (print lines 1 through the end)
:% print (print lines 1 through the end)
:1,/estimate/print (print lines 1 through the line that contains estimate)
```

* Marking and printing
```
ma
move and then
mz
:'a,'z print (prints from a to z position)
```

* Visual mode
```
V
:print
```

* Substitute command
```
:range substitute /from/to flags
:% substitute /exxcell/excell/g
g: global
p: print the modified line
c: ask for confirmation
  - y: make this replacement
  - n: skip this replacement
  - a: replace all remaining without confirmation
  - q: quit, don't make any more changes
  - Ctrl-E: scroll one line up
  - Ctrl-Y: scroll one line down
:% s /\([^,]*\),\(.*\)$/\2,\1/g
```

* Reading a file and inserting it
```
:read filename
you can highlight a text and write it to a file with
:'<,'>write filename
```

* Go to shell
```
:shell
When done type exit
```

* Settings the text width
```
:set textwidth=80
```

* To format a piece of text into a paragraph
```
Select the text in visual mode
gq
Or
gq5j (format the next 5 lines)
```

* To center text
```
:1,5 center 50
select text and then :center 50
```

* To create left margin
```
:1,5 left 5
```

* To control how J joins two lines
```
:set joinspaces (if the current line ends with . two spaces are inserted)
:set nojoinspaces (only a single space is added)
```

* formatoptions
```
:set formatoptions=characters
t: automatically wrap text
c: automatically wrap comments
r: insert comment leader when a new line is inserted
o: insert comment leader when a new line is created
q: allow gq to format comments
2: format based on the indent of the second line
v: do old style vi text wrapping
b: wrap only on blanks you type
l: do not break line in insert mode
```

* Using an external formatting program
```
:set formatprg=fmt
```

* Setting file format
```
" try unix first, then ms-dos
:set fileformats=unix,dos
" to see the detected file format
:set fileformat?
" to set the current file format
:set fileformat=unix
```

* End of file line
```
" the file ends with a linew always
:set endofline
:set noendofline
```

* Text moving commands
```
): one sentence forward
(: one sentence backward
}: one paragraph forward
{: one paragragh backward
```

* Auto completion
```
Ctrl-p
Another Ctrl-p and VIM searches again for completion
Ctrl-n: searches forward for completion
:set ignorecase (ignore case when searching for completion)
:set complete=key,key,key
    .: current file
    b: files in loaded buffers
    d: definitions in current file and in files included with #include
    i: files included with #include
    t: tags file
    u: unloaded buffers
    w: files in other windows
    k: file defined in dictionary
    kfile: file named "file"
```

* Specifying a dictionary
```
:set dictionary=file,file...
:set complete=k/usr/dict/words,k/usr/alt/words.txt
```

* Controlling what is searched by pressing Ctrl-x
```
Ctrl-d: macro definitions
Ctrl-f: file names
Ctrl-k: dictionary
Ctrl-i: current files and includes
Ctlr-l: whole lines
Ctrl-]: tags
Ctrl-p: same as Ctrl-p
Ctrl-n: same as Ctrl-n
```

* Autocmd and groups
```
function DateInsert()
    $read !date
endfunction

"map <F12> :call DateInsert()<CR>\|:write<CR>
autocmd FileWritePre * :call DateInsert()<CR>

augroup cprograms
    autocmd FileReadPost *.c :set cindent
    autocmd FileReadPost *.cpp :set cindent
augroup END
" same as before except not within the augroup block
autocmd cprograms FileReadPost *.h :set cindent
```

* Events
```
BufNewFile
BufReadPre
BufReadPost (BufRead)
BufFilePre
BufFilePost
FileReadPre
FileReadPost
FilterReadPre
FilterReadPost
StdinReadPre
StdReadPost
BufWritePre
BufWritePost
BufWrite
FileWritePre
FileWritePost
FileAppendPre
FileAppendPost
FilterWritePre
FilterWritePost
FileChangedShell
FocusGained
FocusLost
CursorHold
BufEnter
BufLeave
BufUnload
BufCreate
BufDelete
WinEnter
WinLeave
GuiEnter
VimEnter
VimLeavePre
VimLeave
FileEncoding
```

* File patterns: Same as unix file patterns

* Listing all auto commands
```
:autocmd
```

* Remove an auto command group
```
:autocmd! gorupName
:autocmd! gorupName event pattern
```

* You can ignore events
```
:set eventignore=WinEnter,WinLeave
```

* Read only mode
```
vim -R fileName
view fileName
```

* To obscure file (weak encryption)
```
vim -x secret.txt
" to turn off the encryption
:set key=
" to turn on the encryption
:set key=secret (not a good idea)
" instead do this
:X
```

* Batch processing
```
cat changes.vim
:%s/person/Jane/g
:write
:quit
vim -es input.file <changes.vim
```

* Backups
```
:set backup
:set backupext=.bak " instead of ~ .bak will be used
:set patchmode=.org
:set backupdir=~/tmp/
```

* To get a list of recoverable files
```
vim -r
" to get the swap file name for the current buffer
:swapname
" for turning off swap files
:set noswapfile
" configuring swap files
:set updatetime=23000
:set updatecount=400
```

* To control where the swap file is written
```
:set directory=/tmp (Not good to set it to /tmp, because names will conflict)
:set directory=.,/tmp
```

* To write to the swap file but not the real file
```
:preserve
```

* To recover a file
```
:recover file.txt
vim -r file.txt
" discard any changes to file.txt
:recover! file.txt
```



