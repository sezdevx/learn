# Useful sites
* [bash cheatsheet](https://devhints.io/bash)

# Examples
## [timestamp_file_names.sh](timestamp_file_names.sh)
* generates file name with a timestamp
* use of date to generate timestamp

## [process_file.sh](process_file.sh)
* process a given file through a command line
* reading from a file
* incomplete argument error message {$1:?"Error Message"}

## [terminal_capabilities.sh](terminal_capabilities.sh)
* save and restore terminal/screen content

## [horizontal_line.sh](horizontal_line.sh)
* to generate a horizontal line dynamicall based on screen size

## [file_type.sh](file_type.sh)
* if then
* case statement
* function
* readability check
* file pattern matching in if expression

## [comment_counter.sh](comment_counter.sh)
* loop reading from stdout or from a file
* counting and incrementing a counter
* regular expressions, white space matching, beginning of line matching
* regex operator =~

## [list_files.sh](list_files.sh)
* iterating files in a directory
* arrays
* array size
* directory check
* size of a file
* find command
* basename of a path
* for loop

## [list_dirs.sh](list_dirs.sh)
* iterating directories in a directory
* arrays
* array size
* directory check
* size of a file
* find command
* basename of a path
* for loop
* error for when no value is provided for an argument

## [line_no.sh](line_no.sh)
* reading a file line by line
* arrays
* printf
* while loop
* for loop

## [capitalize.sh](capitalize.sh)
* tr to capitalize
* character processing of a string
* argument processing

## [recognize.sh](recognize.sh)
* regular expressions
* shows

## [can_i_drive.sh](can_i_drive.sh)
* if expressions
* read answer from user

## [check_env_vars.sh](check_env_vars.sh)
* environment variable
* -z to check if a variable is defined or has zero length
* -n to check if a variable has non-zero length

## [file_info.sh](file_info.sh)
* File test operators (readable, executable, writable etc...)
* File size

## [check_latest_enwiki_dump.sh](check_latest_enwiki_dump.sh)
* Download from internet
* Silent curl command
* Check the success of a program and use it as a condition
* Ignore rm errors
* Silent grep command

## [file_access.sh](file_access.sh)
* find root path of the running script
* return a value from a function
* dirname of a path

## [daemon.sh](daemon.sh)
* trap signals
* send signals
* append to a file
* while infinite loop
* get file size
* crude logging
* nohup use for daemonizing
* measure time of a function using date
* getting process id, pid ($$)
* -z to check if a variable is defined
* remove any aliasing (e.g. \mv)
* check the exit status (exit code) of a previously run program ($?)

## [guess_my_number.sh](guess_my_number.sh)
* random number generation
* modulus operator
* regular expressions
* argument processing using getopts
* showing help
* read with a timeout
* check exit status (exit code) $? for timeout of read
* prompt with read

## [dedup.sh](dedup.sh)
* making a temporary file name or directory
* detecting platform
* iterating files in a directory
* cleaning up at the exit of the program

## [random.sh](random.sh)
* using /dev/urandom
* fold output for a specific width
* use of uuidgen

## [sort_by_size.sh](sort_by_size.sh)
* sort numerically
* sort in reverse order
* arrays (adding, looping)
* declaring arrays
* iterating files
* use of IFS

## [quiz.sh](quiz.sh)
* select loop
* until loop
* use of seq in for loop

## [string_info.sh](string_info.sh)
* string length
* string concatenation
* string last char removal
* string first char removal
* building comma separated list
* replace a string

## [check_bash_files_against_readme.sh](check_bash_files_against_readme.sh)
* reading from a pipe
* processing output of ls using while loop
* checks if any bash file is not documented in readme.md
* xargs, passing multiple commands to xargs, using the same argument twice

## [unquote.sh](unquote.sh)
* -n to test if string is non-zero length
* conditional last char removal
* condition first char removal

## [debug.sh](debug.sh)
* debugging bash script
* set -x and set +x

## [analyze_data.sh](analyze_data.sh)
* IFS to process comma separated files
* processing a file using io redirection in a while loop
* reading a line into an array using IFS
* you can't do float arithmetic in bash, you can do division though

## [builtin_data.sh](builtin_data.sh)
* read from here documents (here strings)
* a mini ascii art
* processing data from here documents
* adding to an array
* printing contents of an array

## [difficult_to_kill.sh](difficult_to_kill.sh)
* trapping signals with arguments

## [send_email.sh](send_email.sh)
* customized error messages for missing arguments for options
* reading from standard input to an array
* getopts

## [ascii_art.sh](ascii_art.sh)
* use of here documents
* pipes

## [sort_arrays.sh](sort_arrays.sh)
* assigning to arrays
* sorting arrays
* numerical sorting
* iterating sorted arrays

## [terminal_size.sh](terminal_size.sh)
* tput
* hide cursor/show cursor
* trap window change signal
* cleaup at exit
* clear the entire screen
* changing background color
* you need ncurses and tput to make this example work
* press q to exit, reading a single key without pressing enter key

## [colors.sh](colors.sh)
* displays various colors in a formatted manner
* terminal color codes for foreground and background
* for loop with {..}

## [passwords.sh](passwords.sh)
* read password
* IFS to process a line with a specific delimiter
* Iterating through a file line by line

## [analyze_filename.sh](analyze_filename.sh)
* Use of the %, %%, #, ## operator
* Getting file name and extension

## [is_common.sh](is_common.sh)
* use of grep with regular expressions

## [parallel_md5.sh](parallel_md5.sh)
* parallel (background) vs serial execution speed
* waiting on bacgkround processes
* getting the previous command $!

## [file_types.h](file_types.sh)
* finding out the type of a file
* associative arrays

## [create_album.sh](create_album.sh)
* a template to create albums from an image directory
* here document
* function
* for loop, iterating files, file name matching

# Notes
* Brace expansion
```bash
mkdir dir{1,2,3}{a,b}
ls
# dir1a dir1b dir1c dir2a dir2b dir2c dir3a dir3b dir3c
touch file{a..z}
ls
# filea fileb filec .... filex filey filez
```

* To see all defined shell variables and values
```bash
set | less
```

* To check if the shell is interactive
```bash
interactive=0
if [[ $- == *i* ]]
then
    interactive=1
fi
```

* To get the pid of the last started process
```bash
echo $!
```

* To avoid alias
```bash
\ls -l
```

* To avoid shell expansion and substitution use single quotes
```bash
echo 'Hello, the item is 10$!'
```

* To redirect standard error to standard output
```bash
program 2>&1
```

* To discard error output or direct it to a specific file
```bash
program 2> /dev/null
gcc *.cc 2> errors.txt
```

* To direct both standard error and standard output to the same file
```bash
program >& everything.txt
```

* To run multiple commands and direct their output all at once
```bash
( program1; program2; program3 ) > output.txt
```

* Run multiple programs
```bash
# unconditional, doesn't matter if previous command runs or not
first ; second ; third
# conditional, run the next one only if the previous command is successfully run
first && second && third
# unconditional, run in parallel
first & second & third
```

* Conditional running of another command
```bash
if command1; then
    command2
fi
```

* Called scripts can not change the exported variables. The caller has to read
the value back from the output of the called script and assign it to the value.

* To see all set variables in the environment
```bash
set
```

* To see all exported variables in the environment
```bash
env
```

* To process all arguments
```bash
for argV in "$@"
do
    echo "Processing $argV"
done
```

* To assign a default value, if the variable is not set before or is empty
```bash
cd ${TMPDIR:=/tmp}
```

* To assign a default value (including empty), if the variable is not set before
```bash
cd ${TMPDIR=/tmp}
```
In this case, empty string is valid and /tmp won't be assigned if TMPDIR is set to an empty string.

* To assign a more complex value
```bash
cd ${TMPDIR:="$(tmpDirGetCommand)"}
```
You can run commands and assign their results to your variable. In general you can assign
to other variables, tilde expansion (e.g. `~userName`), command substitution, and arithmetic expansion (e.g. `$((number+1))`)

* Security tips
```bash
# set a secure path, avoid aliases
\export PATH=$(getconf PATH)
# clear all aliases
\unalias -a
# clear the hash table
hash -r
# turn off core dumps
ulimit -S -c 0
# set a good IFS
IFS=$' \t\n'
# set a good umask
UMASK=022
umask $UMASK
# create a random temp directory
# and set the trap to remove it once program is done
until [ -n "$tempDir" -a ! -d "$tempDir" ];
do
    tempDir="/tmp/myProgram_${RANDOM}${RANDOM}${RANDOM}"
done
mkdir -p -m 0700 $tempDir || (echo "Failed to create '$tempDir': $?"; exit 1)
# setup trap so tempDir is removed when we exit the program
rmTmpDir="\\rm -rf $tempDir"
trap "rmTmpDir" ABRT EXIT HUP INT QUIT
```

* To evaluate an expression at a later time
```bash
check='test -d $DIR_NAME -a -r $DIR_NAME -a -w $DIR_NAME -a -x $DIR_NAME'
if ! eval $check; then
    echo "Not directory or readable or writable or searchable"
fi
```

* Functions can be exported using `export` command, to make them available
to subprocesses
```bash
export -f funcName
```

* To clear a file, to set its size to 0
```bash
# when noclobber is in effect (always set noclobber)
: >| file.name
```

* To disable globbing (file name generation using metacharacters)
```bash
set -f
ls *
ls: cannot access '*': No such file or directory
set +f
ls *
...
```

* To print input lines as they are read
```bash
set -v
ls
ls
a/ b/
set +v
ls
a/ b/
```

* System wide config files
```
/etc/profile
/etc/inputrc (system-wide Readline initialization)
/etc/profile.d (system-wide for specific programs)
/etc/bashrc or /etc/bash.bashrc (bash specific config)
```

* Individual user config files
```bash
~/.bash_profile
~/.bash_login
~/.profile
~/.bashrc
~/.bash_logout
```

* To search bash history press `ctrl-r` and start typing

* Some useful bash key bindings. Type to see all `bind -p`
```
Ctrl + t : swap two characters
Alt + t : swap two words
Alt + . : prints last argument from previous command
Ctrl + x + * : expand glob/star in the command line before execution
Ctrl + arrow : move forward a word
Alt + f : move forward a word
Alt + b : move backward a word
Ctrl + x + Ctrl + e : opens the command line string in an editor so that you can edit it
Ctrl + e : move cursor to end
Ctrl + a : move cursor to start
Ctrl + xx : move to the opposite end of the line
Ctrl + u : cuts everything to the beginning of line from current position
Ctrl + k : cuts everything to the end of line from current position
Ctrl + y : pastes from the buffer
Ctrl + l : clears screen
```

* Writing a simple bash completion code
```bash
# make sure bash-completion is installed
complete -W 'google.com apple.com microsoft.com facebook.com' host
host [TAB]
```

* To display the type of a command
```bash
type command
# examples
$ type type
type is a shell builtin
$ type which
which is /usr/bin/which
$ type cd
cd is a shell builtin
```

* To get help for a shell builtin
```bash
help type
help cd
```

* Escape $ sign in double quotes
```bash
echo "Hello \$world"
# or
echo 'Hello $world'
```

* To list of bash builtins
```bash
help -d
```

* To bypass an alias
```bash
\ls
# to remove all aliases
\unalias -a
```

* To list all functions defined
```bash
declare -F
```

* To view the source code of a function
```bash
type -a getMd5
```

* To view where a function is defined
```bash
shopt -s extdebug
declare -F getMd5
```

