# Lesson 5: Getting help

## Goals

- Find out what a command does and what options it has
- Read manual pages
- Understand common error messages
- Know how to get unstuck

Nobody remembers every command and every option, not even experts. Experts are
just very good at **looking things up**. That's what this lesson teaches.

## Learn

### Quick help: `--help`

Most commands print a short help text when you add `--help`:

```bash
ls --help
```

It's long. Look at the top part first (it tells you how to use the command), then
scan for the option you need. You can read it page by page by sending it into `less`
(the `|` symbol is explained in Lesson 7):

```bash
ls --help | less
```

### The manual: `man`

Almost every command has a **manual page**:

```bash
man ls
```

It opens in the same viewer as `less`, so the same keys work: `Space` for the next
page, `/word` to search, **`q` to quit**.

A manual page has sections:

| Section | What it tells you |
|---|---|
| NAME | the command and one line about it |
| SYNOPSIS | how to type it; things in `[ ]` are optional |
| DESCRIPTION | what it does, and all the options |
| EXAMPLES | (in some pages) examples, often the most useful part! |
| SEE ALSO | related commands |

There's even a manual about the manual:

```bash
man man
```

### Search the manuals: `apropos`

Don't know the name of the command? Search the one-line descriptions:

```bash
apropos "list directory"
apropos "copy files"
```

### What is this command? `type` and `which`

```bash
type ls
type cd
type echo
which python3
```

- `type` tells you what kind of thing a command is. `cd` is a **shell builtin**:
  it's part of Bash itself, not a separate program.
- `which` tells you where the program file lives.

For builtins, use `help` instead of `man`:

```bash
help cd
```

### One-line descriptions: `whatis`

```bash
whatis cp mv rm
```

### Reading error messages

Errors are the computer telling you what went wrong. Read them carefully: the
answer is usually right there.

| Error | What it means | What to do |
|---|---|---|
| `command not found` | no command with that name | check spelling; maybe it isn't installed (Lesson 8) |
| `No such file or directory` | the file or folder doesn't exist **here** | check spelling, check where you are with `pwd`, use `Tab` |
| `Permission denied` | you're not allowed to do that | see Lesson 8 |
| `Is a directory` | you used a folder where a file was expected | maybe you need `-r`, or the wrong name |
| `Not a directory` | you used a file where a folder was expected | check the path |
| `invalid option` | that option doesn't exist for this command | check `--help` |
| `missing operand` | you forgot to say *what* to do it to | add the file or folder name |

Let's make some errors on purpose:

```bash
cd ~/playground
cat stroy.txt
cd welcome.txt
rmdir treasure
ls -z
cp story.txt
```

For each one, read the message and explain in your own words what went wrong.

### Stuck? A checklist

1. **Nothing happens and you can't type?** A command is still running or waiting. Press `Ctrl` + `C`.
2. **A `>` appeared at the start of the line?** Bash thinks you haven't finished, often
   because of a missing closing quote `"`. Press `Ctrl` + `C`.
3. **Stuck inside a screen with text?** Try `q` (for `less`/`man`) or `Ctrl` + `X` (for `nano`).
4. **The terminal shows strange characters?** Type `reset` and press `Enter`.
5. **Still stuck?** Close the terminal window and open a new one. Nothing is lost.

### Searching the internet

When you search online, include the word `bash` or `linux` and the exact error
message, e.g. `bash "No such file or directory" cd`. Be careful: **never paste a
command from the internet that you do not understand**, especially if it contains
`sudo` or `rm`. Ask a grown-up or your teacher first.

## Try it

1. Open the manual for `cp`. Find the option that makes `cp` ask before overwriting. Quit.
2. Use `apropos` to find a command that has something to do with `password`.
3. Find out whether `pwd` is a builtin or a separate program.
4. Make an unfinished quote on purpose: type `echo "hello` and press `Enter`. What do you see? Get out of it.

## Exercises

1. Use `man ls` to find out what `ls -t` does. Try it in the playground.
2. Use `ls --help` to find the option that sorts files by **size**. Use it.
3. What does the `-S` option of `head` do... does it exist? How did you find out?
4. What does `wc -L` do? Find it in the manual and try it on `story.txt`.
5. Find out what the command `tac` does without running it first. Then run it on `numbers.txt`. Why is it called `tac`?
6. Use `help` to find out what `cd -P` does. (You don't need to understand the whole answer!)
7. Make each of these errors happen on purpose, then fix the command:
   `No such file or directory`, `Is a directory`, `missing operand`.

## Quiz

1. How do you quit a manual page?
2. Which command do you use when you know *what* you want to do but not the name of the command?
3. What does `No such file or directory` mean?
4. What should you do if you see `>` instead of your normal prompt?
5. Why should you be careful about copying commands from the internet?

## Recap

| Command | What it does |
|---|---|
| `command --help` | short help |
| `man command` | full manual (`q` to quit) |
| `help builtin` | help for Bash builtins like `cd` |
| `apropos word` | search manual descriptions |
| `whatis command` | one-line description |
| `type command` | what kind of command it is |
| `which command` | where the program file is |
| `reset` | fix a confused terminal |
