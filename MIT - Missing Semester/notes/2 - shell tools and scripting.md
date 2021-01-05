# Shell Tools and Scripting 

[TOC]

## Shell Scripting 

### Basic Script Language Introduction 

- Every shell have their own scripting language with variables, control flow and syntax
- scripting language is optimized for performing shell-related tasks. Thus creating commands, , saving results into files and reading standard inputs are primitive in shell scripting.  This makes it easier to use than general purpose scripting language. 

#### Variable Assignment

- Assigning variable `foo=bar` and accessing variable `$foo`.  single quote and double quote strings a little bit different meaning. 

```shell
foo=bar
echo "value is $foo"
# prints value is bar
echo 'value is $foo'
# prints value is $foo
```



- Spaces are for separating arguments and may cause issues. 

#### Control Flow and Functions 

- bash supports `if`, `case`, `while` nd `for` and functions.

- Bash supports functions. Basic syntax

  ``` shell
my_function () {
      commands
    return 4 # can only return numeric arugmentts
  }
  ```
  
  To use `my_function` as command, we first need to load it in current process via `source my_function.sh`. This function will return 4 with `$?`.
  
  **Example:**

  Here is  function that makes a directory and cd into it. To use mcd command, run `source mcd` to load mcd in current process and then run `mcd file1` to run the function. 

  ```shell
mcd () {
  mkdir -p '$1'
cd '$1'
  }
```
  
where `$1` means first variable. bash uses a number of special variables to refer to arguments
  
- `$0`: name of the script
  
- `$1` - `$9`: arguments to the script 
  
- `$@`: all the arguments 
  
- `$#`: number of arguments 
  
  - `$?`: return code of the pervious command
  
  - `$$`: process identification number (PID) of the current script.
  
  - `!!`: entire last command 
  
    > A common pattern is to execute a command only for it to fail due to missing permissions; you can quickly re-execute the command with sudo by doing `sudo !!`
  
  - `$_`: last argument from the last command.

####  Command Communications

-  Commands will return output using `STDOUT`, errors with `STDERR` and return to code to report errors in the more script-friendly manner. 

  - return code or exit status is the way how commands communicate how execution went. 

  - 0 means everything okay, anything else means some errors


#### Short circuit operators

Exit codes can be used to conditionally execute commands in series using `&&` (and) and `||`(or).  `first command || second command` will first execute first command and  will only execute second command if first is false. 

```shell
false || echo 'will print'
true || echo 'will not print'

false && echo 'will pirnt'
true && echo 'will not print'
```

- ​	`;` can be used to execute multiple commands.

  ```shell
  false || echo 'will print' ; true && 'will print'
  # will print
  # will print
  ```

  

#### Command substitution with variables

 to get output of a command as variable use: `$(command)`

```shell
echo "this will echo files: $(ls)"
```

#### Process Substitution

`<( command )` will execute the command and place output in a temp file that can be then give to a command that require arguments as files.  

- **Example**:

```shell
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted

echo "Running program $0 with $# arguments with pid $$"

for file in "$@"; do
    echo "$file"
    grep foobar "$file" > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

### Exploiting Patterns in Arguments 

- **Wildcard**: `?` and `*` for two types of wild card matching, to match one or any kind of characters. 
  - `?`: suppose files `foo, foo1, foo2, foo10, bar`, `rm foo?` will remove `foo1, foo2` 
  - `*`: `rm foo*` will remove all the files except `bar`.
- **Curly Braces `{ . }`**: whenever we have a common substring in series of files. For instance, moving all `.png` files will be: `cp /path/to/project/{foo, bar, baz}.sh /newpath` 

```shell
convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files


mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch {foo,bar}/{a..h}
touch foo/x bar/y
# Show differences between files in foo and bar
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y
```



### Running Generic script 

- You can run any script with bash by giving appropriate execution folder in shebang: e.g. for python `#!/usr/local/bin/python`.
  - kernel know how to execute it because of the shebang
  - can use `env` command to  write shebang so  that it will resolve wherever the command lives in the system.

### Important  Points 

1. functions have to be in the same language as shell but scripts can be written in any language. 
2. functions are loaded once when their definition is read, scripts are loaded every time we execute them. 
3. functions are executed in current shell environment while scripts execute in their own process. Thus functions can modify env variables but scripts cant. 

## Shell Tools

### Finding how to use commands

1. **`command --help`**
2. **`man command`**
3. [TLDR](https://tldr.sh/) pages for short version of help; install them and use like `tldr ls`.
4. Install [shellcheck](https://www.shellcheck.net/)  to find errors in script

### Finding Files

- **`find [pattern]`**: will recursively find a while that matches a specific pattern.

  ```shell
  # Find all directories named src
  find . -name src -type d
  # Find all python files that have a folder named test in their path
  find . -path '*/test/*.py' -type f
  # Find all files modified in the last day
  find . -mtime -1
  # Find all zip files with size in range 500k to 10M
  find . -size +500k -size -10M -name '*.tar.gz'
  ```

- **Actions on found files via `find`**:

  ```shell
  # Delete all files with .tmp extension
  find . -name '*.tmp' -exec rm {} \;
  # Find all PNG files and convert them to JPG
  find . -name '*.png' -exec convert {} {}.jpg \;
  ```

- **Alternatives of `find`**:
  comparison [link](https://unix.stackexchange.com/questions/60205/locate-vs-find-usage-pros-and-cons-of-each-other)

  - `fd`: simple to use with regex
  - `locate`: builds a database of all the files

### Finding Code

`grep` can be used to find a string patterns in any of the files 

- `grep -C 5 `: -C is for context and will show 5 lines above and below a match
- `grep -v`: for inverting the match i.e. alll lines that don't match pattern.
- `grep -R` will **R**ecursively go into directories and look for files for matching string. 

**Alternatives of `grep`**:

1. ack
2. ag
3. rg

Here, we will stick with `rg` (ripgrep).

Installation:

```shell
$ curl -LO https://github.com/BurntSushi/ripgrep/releases/download/12.1.1/ripgrep_12.1.1_amd64.deb
$ sudo dpkg -i ripgrep_12.1.1_amd64.deb
```

Examples 

```shell
# Find all python files where I used the requests library
rg -t py 'import requests'
# Find all files (including hidden files) without a shebang line
rg -u --files-without-match "^#!"
# Find all matches of foo and print the following 5 lines
rg foo -A 5
# Print statistics of matches (# of matched lines and files )
rg --stats PATTERN
```



### Finding Previously Typed commands 

1. up arrow
2. `history`: will give you access to all the commands you have typed. You can search through history like `history | grep find`
3. `Ctrl+R`: Let you do backward search 
4. [fish](https://fishshell.com) shell can be used to have history based auto-suggestions
5. If you type a command with leading space, it will not show up in history 

### Directory Navigation 

> As with the theme of this course, you often want to optimize for the common case. Finding frequent and/or recent files and directories can be done through tools like [`fasd`](https://github.com/clvv/fasd) and [`autojump`](https://github.com/wting/autojump). Fasd ranks files and directories by [*frecency*](https://developer.mozilla.org/en/The_Places_frecency_algorithm), that is, by both *frequency* and *recency*. By default, `fasd` adds a `z` command that you can use to quickly `cd` using a substring of a *frecent* directory. For example, if you often go to `/home/user/files/cool_project` you can simply use `z cool` to jump there. Using autojump, this same change of directory could be accomplished using `j cool`.
>
> More complex tools exist to quickly get an overview of a directory structure: [`tree`](https://linux.die.net/man/1/tree), [`broot`](https://github.com/Canop/broot) or even full fledged file managers like [`nnn`](https://github.com/jarun/nnn) or [`ranger`](https://github.com/ranger/ranger).