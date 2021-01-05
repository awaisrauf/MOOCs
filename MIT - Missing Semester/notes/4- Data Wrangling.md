# Data Wrangling 

- data in one format and we want it to other format called data wrangling
-

## `sed` Stream EDitor
`sed` command in bash acts as a stream editor on streaming text data. It gives you short commands for how to modify the file. There a lot of commands, but most important is `s`: substitution.  To substitute a pattern with a string, we can write: `s/pattern/string/`
```shell
echo "Let's replace 9" | sed s/[0-9]/'numbers'/
Let's replace numbers
```

## Regular Expressions
- Regular expressions are usually sorrounded by `/`.
- Most ASCII character keep their normal menaing but some have special matching meaning. 
- Some common patterns are:
	1. `.` means any one character except new line e.g. `.a` ==> any word where we have any alphabet before a i.e. ba, ca, da etc.
	2. `*` zero or more of the preceeding match e.g. `l*x` means any any number of l's edning with x i.e. Lx, LLx, LLLx
	3. `+` one ore more of preceeding match
	4. `[abc]`: any one character of a, b and c.
	5. `[a-m]`: any small alhabet between a and m.
	6. `(RX1|RX2)` either something that matches RX1 or RX2.
	7. `^` the start of the line
	8. `$`: end of the line
- `sed` require regex to be wrapped in `\` e.g.: sed s\[0-9]\1\
- 
