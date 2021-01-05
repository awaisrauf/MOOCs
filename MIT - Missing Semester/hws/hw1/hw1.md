# Exercises

All classes in this course are accompanied by a series of exercises. Some give you a specific task to do, while others are open-ended, like “try using X and Y programs”. We highly encourage you to try them out.

We have not written solutions for the exercises. If you are stuck on anything in particular, feel free to send us an email describing what you’ve tried so far, and we will try to help you out.

:+1: For this course, you need to be using a Unix shell like Bash or ZSH. If you are on Linux or macOS, you don’t have to do anything special. If you are on Windows, you need to make sure you are not running cmd.exe or PowerShell; you can use [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/) or a Linux virtual machine to use Unix-style command-line tools. To make sure you’re running an appropriate shell, you can try the command `echo $SHELL`. If it says something like `/bin/bash` or `/usr/bin/zsh`, that means you’re running the right program.

:+1: Create a new directory called `missing` under `/tmp`.

:+1: Look up the `touch` program. The `man` program is your friend.

:+1:Use `touch` to create a new file called `semester` in `missing`.

:+1:Write the following into that file, one line at a time:

```
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu
```

The first line might be tricky to get working. It’s helpful to know that `#` starts a comment in Bash, and `!` has a special meaning even within double-quoted (`"`) strings. Bash treats single-quoted strings (`'`) differently: they will do the trick in this case. See the Bash [quoting](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) manual page for more information.

:+1:Try to execute the file, i.e. type the path to the script (`./semester`) into your shell and press enter. Understand why it doesn’t work by consulting the output of `ls` (hint: look at the permission bits of the file).

:+1:Run the command by explicitly starting the `sh` interpreter, and giving it the file `semester` as the first argument, i.e. `sh semester`. Why does this work, while `./semester` didn’t?

:a: ​both executed files in my case but commands were not found as the contents of the file are not commands. 

1. `sh file`: executes a shell-script in new shell process
2. `. file` executes a shell script in current shell process
3. `./file` execute the file in the current directory. The file can be binary executable or start with hashbang `#!..` to show how should it be executed i.e. `#!/usr/bin/ruby` means script should be executed as Ruby. 



:+1:Look up the `chmod` program (e.g. use `man chmod`).

:+1:Use `chmod` to make it possible to run the command `./semester` rather than having to type `sh semester`. How does your shell know that the file is supposed to be interpreted using `sh`? See this page on the [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) line for more information.

```shell
chmod ug+w semester
```

give write permissions to user and group

:+1:Use `|` and `>` to write the “last modified” date output by `semester` into a file called `last-modified.txt` in your home directory.

```shell
stat semester | grep Modify > last-modified
```



:+1:Write a command that reads out your laptop battery’s power level or your desktop machine’s CPU temperature from `/sys`. Note: if you’re a macOS user, your OS doesn’t have sysfs, so you can skip this exercise.
:a: Windows linux subsystem don't allow to access these, so instead I wrote a command to read the autosleep on or off. 

```shelll
# go to sys file
cat /sys/power/autosleep
```

