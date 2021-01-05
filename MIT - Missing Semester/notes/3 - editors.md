# Editors (Vim)

### How to start  a new Editor

1. Start with a tutorial 

2. stick with all the text editing needs even if it slows you down

3. > Look things up as you go: if it seems like there should be a better way to do something, there probably is.

4. It will take <2 hours for basic functionality and >20 hours to be fully fluent. 



### What editor to use

VS-Code is famous editor and Vim is most famous command-line based editor. 

### Vim and its Philosophy

- Code is mostly about reading/editing and less about writing. For this reason, Vim is a modal editor: it has many modes for different works like edit, insert, command, visual etc 
- Vim is programmable and it's interface is also a programming language.: keystrokes are commands and they are composable. 
- Vim avoids use of keyboard and keys that slows down (arrow).

#### Modal Editing 

Vim editing modes and keystrokes have different meaning in these modes: 

1. **Normal**: for moving around a file and making edits 
2. **Insert**: for inserting text
3. **Replace**: for replacing text
4. **Visual**: for selecting blocks of text
5. **Command Line**: for running commands

**Example: **

> For example, the letter `x` in Insert mode will just insert a literal character ‘x’, but in Normal mode, it will delete the character under the cursor, and in Visual mode, it will delete the selection.

##### Getting into different modes 

- Vim shows current mode at the bottom
- Initial mode is Normal mode

Getting into different modes

1. Switch to Normal mode: `<ESC>`
2. From normal to
   1.  insert: `i`
   2. replace `R`
   3. visual `v`
   4. visual line `V`
   5. Visual Block `Ctrl-V`
   6. command line `:`

##### Inserting Mode

Vim acts like any normal editor in this mode. However, if we do all the editing in this mode, it may not be as efficient. 

##### Buffers, tabs, and windows

- Vim maintains a set of open files called "buffers". 
- A vim session consists of a number of *tabs*, each of which has  number of windows (split panes).
- Each window show one buffer, but, one buffer can be shown in multiple windows. 

##### Command Line 

- Enter by typing `:` in Normal mode and commands can be typed at the bottom. 
- Important commands
  - `:q`: quit (close window)
  - `:w`: save (write)
  - `:wq`: save and quit
  - `: {name of the file}`: open file for editing
  - `:ls`: show open buffers

### Vim's interface is  programming language 

- vim's interface is a programming language 

#### Movements 
- Most of time is spent in Normal mode, where using movement commands to navigate the buffer. 
- Movements in vim are called "nouns" because they refer to chunk of text. Some basic movements:
	1. Basic Movements: `hjkl` (left, down, up, right)
	2. Words: `w` (next word), `b`: (begining of word), `e`: (end of word)
	3. Lines: `0`: begining of the line,  `^` (first non-blank character), `$`: end of line
	4. Screen: `H`: top of screen, `M`: middle of screen `L`: bottom of screen.
	5. Scroll: `Ctrl-u`: up, `Ctrl-d` down
	6. File: `gg`: begining of file,  `G`: end of file
	7. Line Numbers: `:{number}<CR> or `{number}G
	8. Misc: `%`:  corresponding item
	9. Search `:g/{regex}, n/N for navigating matches

#### Selection
Visual modes (Visual, Visual Line, Visual Block) cna use movement keys to make selection. 

#### Edits
-  everything that is performed with mouse can be done with keyboard in this mode with editingcommands that compose with movemetns commands. 
- In this mode, Vim's interface truely look like programming lanugage. 
- Vim's editing commands are also called "verbs", becuases they act on  nouns (Movement commands). Some of the commaands:
	1. `i` enter the insert mode
		- but for 
	2. `o / 0`: insert line below and go back to insert mode
	3. `d{motion}`: delete with motion e.g. `dw`: delete word, `d$`: delete end of the line
	4. `c{motion}`: change {motion}, e.g. `cw`: change word.
	5. `x`: delete character
	6. `s`: substitute character
	7. Visual mode + manipulation
	8. `u` to undo `Ctrl-r`: redo
	9. `y` to copy "yank" (`d` also copy)
	10. `p` to paste
	11. Lots more
#### Counts
- we can combine nouns and verbs with a count to do a specifc tihng for specific number of times.
	1. `2h`: 2 left
	2. `3l`: 3 right 
	3. `4dw`: delete 7 words

#### Modifiers 
- To change the meaning of a noun. 
> Some modifiers are i, which means “inner” or “inside”, and a, which means “around”. ci( change the contents inside the current pair of parentheses ci[ change the contents inside the current pair of square brackets da' delete a single-quoted string, including the surrounding single quotes

#### Demo
```python
def fizz_buzz(limit):
    for i in range(1, limit):
        if i % 3 == 0:
            print('fizz', end=" ")
        if i % 5 == 0:
            print('fizz'), end=" ")
        if i % 3 and i % 5:
            print(i)

def main():
    fizz_buzz(10)
main()
```

### Customizing Vim
- Vim can be customized via plain-text configuration file in `~/.vimrc` (containing vim script commands)
- 

### Extending Vim
- There are a lot of plugins for extending vim. Vim 8.0 has a built-in package management system. Simply create the directory `~/.vim/pack/vendor/start/`, and put plugins in tehre (e.g. via `git clone`)
- [Vim Awesome](https://vimawesome.com/)

### Vim mode in other programs
Many programs offer vim emulations
1. Shell
2. Readline
even browsers, VScode and jupyter notebook allow vim bindings.

###  Multiple Windows
- `:sp` / `:vsp` to split windows
- can have multiple views of same buffer
### Macros
> q{character} to start recording a macro in register {character}
q to stop recording
@{character} replays the macro
Macro execution stops on error
{number}@{character} executes a macro {number} times
Macros can be recursive
first clear the macro with q{character}q
record the macro, with @{character} to invoke the macro recursively (will be a no-op until recording is complete)
Example: convert xml to json (file)
Array of objects with keys “name” / “email”
Use a Python program?
Use sed / regexes
g/people/d
%s/<person>/{/g
%s/<name>\(.*\)<\/name>/"name": "\1",/g
…
Vim commands / macros
Gdd, ggdd delete first and last lines
Macro to format a single element (register e)
Go to line with <name>
qe^r"f>s": "<ESC>f<C"<ESC>q
Macro to format a person
Go to line with <person>
qpS{<ESC>j@eA,<ESC>j@ejS},<ESC>q
Macro to format a person and go to the next person
Go to line with <person>
qq@pjq
Execute macro until end of file
999@q
Manually remove last , and add [ and ] delimiters


### Resources
> vimtutor is a tutorial that comes installed with Vim - if Vim is installed, you should be able to run vimtutor from your shell
Vim Adventures is a game to learn Vim
Vim Tips Wiki
Vim Advent Calendar has various Vim tips
Vim Golf is code golf, but where the programming language is Vim’s UI
Vi/Vim Stack Exchange
Vim Screencasts
Practical Vim (book)


