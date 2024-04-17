# Command Line Enviornments 

- How to run several processess at the same time, how to stop or pause a process and how to make them run in the background
- How to imporve shell and other tools by defining aliases, connfiguring them using dotfiles.
- How to work with remote machines 


## Job Contorl
A shell uses UNIX communication system called signal to coummunicate information with the processes. When a process receives a signal, it stops its execution and deals with the signal first, potientially chaning the flow of exectution. For this reason, signals are software interrupts. 
### Killing a Process
- When we type `Ctrl+C` to stop a process, it delivers a signal `SIGNINT` to the process.
- Following python program does not kill the process as it receives `SIGNINT` and ingroes it:

```python
import signal, time

def handler(signum, time);
	print('Not gonna kill the process')

signal.signal(signal.SIGNINT, handler)

# unbounded running
i = 0
while True:	
	time.sleep(.1)
	print('\r{}'.format(i), end="")
	i +=1
```

we can still use `SIGNQUIT` to quit this process. 
- `SIGNINT` and `SIGNQUIT` both are terminal realted requests, a more generic signal for asking a process to exit gracefully is `SIGNTERM` by using `kill -TERM <PID>`.

### Pausing and backgrounding process

- Signals can do other operations on processes as well:
	1. To puase a process: `SIGNSTOP` by using `Ctrl-Z`.
	we can continue paused job in background ori foreground by `bg` or `fg`.
	2. `jobs` command lists unfinshed jobs associated with current terminal.
	To access last background job, we can use `$!`. 
	3. `&` suffix (using at the end) will run a command in the background.
## Terminal Multiplexers
- Many times, we need to open multiple programs. One option is to use multiple winodws, however, a better option -- especially for remote machines -- is to use terminal multiplexers.
- Terminal multiplxers can open multiple termainl windows using panes and tabs so you can interact with multiple shell sessions. 
- Terminal multiplexers also help in terms of detach a window and reattaching it later.
- This is especially helpful when working with remote machines
- Most popular terminal multiplexer is tmux: it is highly configureable and bysing associated keybindings, you ca create multiple tabs and panes and quickly navigate through them. 
- `tmux` expects you to kow its key bindings. They all have the form `<Ctrl-b> x`. This means, it consists of
	1. pressing `Ctrl-b`
	2. realeaasing it
	3. pressing `x`
- Tmux have following hierarchy of objectts:
	1. **Sessions**: an independent working space with one or more windwos:
		- `tmux` strts a new session
		- `tmux new -s NAME` starts it with name
		- `tmux ls` lists all teh current sessions 
		- Within tmux, typing `<Ctrl-B> d` detaches the current session.
		- `tmux a` attaches the last session. You can use `-t` flag to specify which.
	2. **Windows**: Visually seperate part of same session:
		- 
	3. **Panes**: Like vim, panesl let you split mutliple shells in the same visul display

- You can have further reading [here](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/)

## Aliases
- A short form for another commaand that your shell will replace automatically for you. For instance, 
	```shell
	alias alias_name="command_to_alias arg1 arg2"
	```

	More useful uses of aliases
	```shell
	# Make shorthands for common flags
	alias ll="ls -lh"

	# Save a lot of typing for common commands
	alias gs="git status"
	alias gc="git commit"
	alias v="vim"

	# Save you from mistyping
	alias sl=ls

	# Overwrite existing commands for better defaults
	alias mv="mv -i"           # -i prompts before overwrite
	alias mkdir="mkdir -p"     # -p make parent dirs as needed
	alias df="df -h"           # -h prints human readable format

	# Alias can be composed
	alias la="ls -A"
	alias lla="la -l"

	# To ignore an alias run it prepended with \
	\ls
	# Or disable an alias altogether with unalias
	unalias la

	# To get an alias definition just call it with alias
	alias ll
	# Will print ll='ls -lh'
	```
- aliases don't presist shell sessions. you have to change dot files (e.g. `.bashrc`) for them to presist during startup.

## Dotfiles

- Many progarmsss can bee configured with plain text files that starts wtih a `.`, hence the name `dot files`. E.g. `.vimrc` for vim files and so on. 
- Shell i one example which is configured by dot files. On startup, your shell will read many files to lload itss configuration. Depending on the shell, it could be different and complext.Here is source that explains the process neatly: [link](https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html)
- For bash, editing `.bashrc` or `.bash_profile` works in most systems.
	1. We can include all the commands that we want to run at the startup e.g. alias or modification to path enviornment.
	2. Many shell programs have line like `export PATH="$.../bin"` in shell config file.

- Examples of the tools that can be configured with dot:
	1. `bash` - `~/.bashrc`, `~/.bash_profile`
	2. `git` - `~.gitconfig`
	3. `vim` - `~./vimrc` and the `~/.vim` folder
	4. `ssh` - `~/.ssh/config`
	5. `tmux` - ~/.tmux.conf`
### How to Organize `dotfiles`
- THey should be in their own folder, under version control and **symlinked** into place using a script.  This has many benfits.
	1. Easy installtion: it will only require a minute for customization
	2. Portability: Your tools will work the same way
	3. Sync: Update files at one place and they will work on all the places
	4. Change Tracking: You need to maintain these files and tracking a long term project is a good idea.
	
### What to put in the dot files
1. Learn tool's setting by man pages
2. Try finding blog posts that exaplains author's preferences
3. Read dotfile repos on github: [link](https://github.com/search?o=desc&q=dotfiles&s=stars&type=Repositories) and most popular here [link](https://github.com/mathiasbynens/dotfiles)
4. Dont copy things blindly
5. Good source [link](https://dotfiles.github.io/)

### Portability 
A common problem with dotfiles might not work with different machines, e.g. if they have differetn operating systems or shells. And sometimes we may want to apply some configurations to a specifc machine only.

Here are few tricks for thsi easier: 
1. If configuration file supports it, use if-else to sepcify custiomizatio. 
```shell

if [[ "$(uname)" == "Linux" ]]; then {do_something}; fi

# Check before using shell-specific features
if [[ "$SHELL" == "zsh" ]]; then {do_something}; fi

# You can also make it machine-specific
if [[ "$(hostname)" == "myServer" ]]; then {do_something}; fi
```
2. If configuration file supports it, use include statemetns. For example: `.gitconfig` can have a setting
```shell
[include]
	path = ~/.gitconfig_local
```
And then on each machine, ~/.gitconfig_local can contain machine-specific settings. You could even track these in a separate repository for machine-specific settings.

3. This idea is also useful if you want to use  same settings across different programs, e.g. same aliases for `bash` and `zsh`, we can write `.aliases` and ahve the following block in block:
```shell
# Test if ~/.aliases exists and source it
if [ -f ~/.aliases ]; then
    source ~/.aliases
fi
```

