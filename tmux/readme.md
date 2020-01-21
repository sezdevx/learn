## tmux
* Default command prefix is `Ctrl-b`, but you can change it to `Ctrl-space`

### Outside the tmux
* Create a new session `tmux`
* Create a new session with a name `tmux new -s "My New Session"`
* Attach to a currently existing session `tmux attach`
* Attach to a named session `tmux attach -t "My New Session"`
* Kill all sessions `tmux kill-server`
* Kill a named session `tmux kill-session -t "Mt New Session"`
* List all sessions `tmux ls`
* Attach to a specific session `tmux attach -t 0`

### Inside the tmux
* Detach from tmux `tmux detach`
* Kill all sessions `tmux kill-server`

#### Using keyboard
* Detatch from tmux `Ctrl-b-d`
* Create a window within the same session `Ctrl-b-c`
  * To move between windows `Ctrl-b-p` (previous) or `Ctrl-b-n` (next)
  * To jump to a specific window `Ctrl-b-[0-9]`
  * To choose a window or pane from a list `Ctrl-b-w`
  * `exit` to close the window
  * `Ctrl-b-&` to kill all processes in an unresponive window
* Split the window `Ctrl-b-%` or `Ctrl-b-"`
  * To move between panes `Ctrl-b-o`
  * To switch to another pane `Ctrl-b-arrow key`
  * To zoom in on a pane `Ctrl-b-z`
  * To zoom out on a pane `Ctrl-b-z`
* To switch to another session `Ctrl-b-(` or `Ctrl-b-)`
* Type `exit` to kill a pane or a window or a session or alternatively `Ctrl-b-x`

#### Resizing panes
* `Ctrl-b-:` to go to command mode in tmux
* Assuming we are on the top pane
    * `resize-pane -U 2` to move the separator up 2 lines
    * `resize-pane -D 2` to move the separator down 2 lines
* Assuming we are on the left pane
    * `resize-pane -L 2` to move the separator left 2 lines
    * `resize-pane -R 2` to move the separator right 2 lines

#### Scroll in a pane
* `Ctrl-b-[` to go to scroll mode, in scroll mode you can use
arrows and other keys to go up and down. `q` to exit the scroll mode.

