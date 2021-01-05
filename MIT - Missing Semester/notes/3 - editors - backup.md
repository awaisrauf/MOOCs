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
- 

