# Course overview + the shell

- The purpose of this class is to introduce basic computer skills that can aid cs students in their work.

## Shell

- Will be covering bourne-again-shell or bash here. 
- A bash screen looks like following:

```bash
missing:~$ date
Fri 10 Jan 2020 11:49:31 AM EST
missing:~$ 
```

- **Shell Commands**: shell parses the command by splitting it by white spaces. 
  - first word tells what program to run
  - all subsequent words are arguments that program can access 
  - any argument with white space should be either use( `"My Photes")` or escape just the relevant character with `\` (`My\ Photos`)

- **Running Commands**: Shell is a programming environment just like python or ruby so it has variables, conditionals, loops etc. A command in shell is small piece of code that shell interprets. 

  - shell first try to interpret a command provided by user
  - if command does not match  one of its programming keywords it consult `environment variables` called `$PATH` that lists which directories the shell should search for programs when it is given a command.

- **Shell Commands and `$PATH`**: All the shell commands are basically path to an executable file that do all the magic. 

  - We can use following command to see all the PATH variables

  ```bash
  echo $PATH
  ```

  - when we run command echo, shell sees that it should run the command `echo`, and then searches through the `:` separated  list of directories in`$PATH` for a file by the name of echo. 

  - If it finds a file by the name of the command, it runs it assuming that it is executable. We can see which file runs a particular command by following:

    ``` bash
    which echo
    /bin/echo
    ```

  - we can bypass `$PATH` by providing the file we want to execute. 

    ``` 
    \bin\echo $PATH
    ```

### Navigating the shell

- **Path**: A path in shell is delimited list of directories; separated by `/` on Linux/macOS and `\` on Windows. 

  - On Linux and macOS, the path `/` is the root of the file system under which all directories and files lie
  - On windows, there is one root for each disk (`C:\`.)
  - A path starting with `\` is called absolute path. Any other path is relative based on current working directory. We can use `pwd` command to see current working directory. 
  - We can change path with `cd` command.
  - In path, `.` refers to current directory and `..` refers to parent directory. 
  - In general, program runs in the current directory, unless told otherwise. 

- **`ls` command** see what lives in a given directory, we run `ls` command. 

- Most commands also accepts flags to modify their behavior. They start with `-`.  Usually `--help` flag can tell you all options that are available with a command. 

- `ls -l` gives us detailed description of each file:

  ```bash
  ls -l /home
  drwxr-xr-x 1 missing  users  4096 Jun 15  2019 missing
  ```

  - first d: the missing is a directory 
  - three group of three chars `rwx` : tells us permissions of three groups (owner, use and everyone else). Each char represent one level of permission:
    - `r`: read permission - to read contents 
    - `w` write permission
    - `x`: execute permission means who can search 
    - `-`: this permission is not available for a particular user. 

- `mv`: to move or rename a file 

- `cp`: to copy a file 

- `mkdir`: to create a new directory 

- `rm`: to remove a file

- `rm -r` to remove a directory and everything in it recursively 

- `rmdir`: to remove a directory that is empty

- `man ls`: to see the manual page of a command `q` to exit. 

- `ctrl+l` to clear the shell

- `grep`: search text

  ```
  curl --head --silent google.com | grep Date
  ```

  

### Connecting Programs 

- In the shell, programs have two primary streams associate with  them: input stream and output stream. 

  - When a program tries to read input, it read from input stream
  - when a it prints something, it prints to output stream

- Default for both streams is terminal (keyboard as input and screen as output)

- We can change the input stream by `< file` and output`> file`

  ```
  echo awais > file.txt
  ```

- To append, use `>>` e.g.:

  ```
  echo awais >> file.txt
  ```

  

- input/output redirection really shines in the use of pipes `|`. Pipes chain programs such that the output of one program in input of the second one:

  ```bash
  ls -l / | tail -n1
  ```

  here `ls -l` will get details of all the files in current directory , `/` means only show name and not whole path, and `tail` command is there to show only last ten lines followed by `-n1`flag which means that only one line should be shown.

### A versatile and powerful tool

- Most unix systems have `root` as the special user and have all the accesses and can create, read, update and delete any file in the system. 
- Default user is not the `root` as you can accidently do something wrong. 
- When you need to run a command with root permission, use `sudo` before the command, `sudo`(super user do).
- When we have permission denied error, it usually means that we need `sudo`. 

- you need `sudo` to write the `sysfs` file system mounted under `\sys. sysfs` exposes a number of kernel parameters as  files, so that you can easily re-configure kernel on the fly. 

  > For example, the brightness of your laptop’s screen is exposed through a file called `brightness` under
  >
  > ```
  > /sys/class/backlight
  > ```

- Following command will not work despite being valid. 

  ```
  $ sudo echo 3 > brightness
  ```

  - The reason is that the operations like `|`, `>` and `<` are done by shell and not by programs. `echo` and its friends don't know about  `|`. They just read input and write output.

  - >In the case above, the *shell* (which is authenticated just as your user) tries to open the brightness file for writing, before setting that as `sudo echo`’s output, but is prevented from doing so since the shell does not run as root. Using this knowledge, we can work around this:

    ```
    $ echo 3 | sudo tee brightness
    ```

    > Since the `tee` program is the one to open the `/sys` file for writing

### Quoting in Shell

To preserve literal meaning of a string, we can use following (see this l[ink](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) for more details):

1. `\` escape character: it preserves literal meaning of any word after it except new line
2. `'.'` single quote: preserves literal meaning of any chars within it except single quote itself
3. `"."` double quotes: preserves literal meaning of a string except f ‘$’, ‘`’, ‘\’, and, when history expansion is enabled, ‘!’

### Different ways of running shell script 

1. `sh file`: executes a shell-script in new shell process
2. `. file` executes a shell script in current shell process
3. `./file` execute the file in the current directory. The file can be binary executable or start with hashbang `#!..` to show how should it be executed i.e. `#!/usr/bin/ruby` means script should be executed as Ruby. 