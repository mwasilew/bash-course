# Lesson 1: Meet the terminal

## Goals

- Know what the terminal and Bash are
- Open a terminal and type your first commands
- Use the keyboard shortcuts that save you time

## Learn

### What is the terminal?

Usually you tell the computer what to do by clicking with the mouse. The
**terminal** is another way: you **type** instructions, called **commands**, and
the computer types back its answer.

The program that reads your commands and runs them is called the **shell**. On
Ubuntu the shell is called **Bash**. That is why this course is called "Bash for
Beginners".

Why bother, when you have a mouse?

- Many jobs are much faster to type than to click.
- You can repeat a job a thousand times with one command.
- Servers, robots, Raspberry Pis and supercomputers are mostly controlled this way.
- Programmers use it every day.

### Opening the terminal

Press **`Ctrl` + `Alt` + `T`** (all three keys at once).

Or: click *Show Applications* in the bottom-left corner, type `terminal` and
press `Enter`.

A window opens with a line that looks something like this:

```
mieszko@laptop:~$
```

This is the **prompt**. It means "I am ready, type a command". It tells you:

| Part | Meaning |
|---|---|
| `mieszko` | your user name |
| `laptop` | the computer's name |
| `~` | the folder you are in (`~` means your home folder) |
| `$` | the end of the prompt; you type after it |

In this course, when you see a command like this:

```bash
echo hello
```

type it after the `$` and press **`Enter`**. Do not type the `$` itself.

### Your first commands

`echo` repeats whatever you write after it:

```bash
echo hello
echo My name is Mieszko
```

`date` shows today's date and time:

```bash
date
```

`whoami` tells you your user name:

```bash
whoami
```

`hostname` tells you the computer's name:

```bash
hostname
```

`uptime` shows how long the computer has been switched on:

```bash
uptime
```

`clear` wipes the screen clean (your commands are not lost, the screen is just tidied):

```bash
clear
```

### What a command looks like

Most commands have three parts:

```
command   -options   arguments
  ls        -l        Documents
```

- the **command**: what to do
- **options** (also called flags): *how* to do it; they usually start with `-`
- **arguments**: *what* to do it to

Spaces matter! They separate the parts. `echo hello` works; `echohello` does not.

Try `date` with an option:

```bash
date +%A
date +%Y
```

The first prints the day of the week, the second prints the year.

### When the computer does not understand

Type something that is not a command:

```bash
hello
```

You get:

```
hello: command not found
```

This is completely normal. The computer is just saying "I don't know a command
called that". Check your spelling and try again.

### Keyboard superpowers

| Key | What it does |
|---|---|
| `↑` and `↓` | go back through commands you typed before |
| `Tab` | finish a command or name for you (press twice to see choices) |
| `Ctrl` + `C` | stop the running command / cancel what you are typing |
| `Ctrl` + `L` | clear the screen (same as `clear`) |
| `Ctrl` + `Shift` + `C` | copy selected text in the terminal |
| `Ctrl` + `Shift` + `V` | paste into the terminal |

Note: in the terminal, plain `Ctrl` + `C` does **not** copy! It stops things.

Try `Tab` now: type `whoa` and press `Tab`. Bash finishes the word `whoami` for you.

### History

Bash remembers what you typed:

```bash
history
```

Each line has a number. To run command number 5 again, type `!5`.
To run the very last command again, type `!!`.

### Closing the terminal

```bash
exit
```

## Try it

1. Open a terminal with the keyboard shortcut.
2. Make the computer say `I am learning Bash`.
3. Find out your user name and the computer's name.
4. Use `↑` to bring back the `echo` command, change the text, and run it again.
5. Type `ech` and press `Tab`. What happens?
6. Close the terminal with `exit` and open it again.

## Exercises

1. Print the current date and time.
2. Print only the current month name. Hint: `date +%B`.
3. Print a message with three lines in one command. Hint: `echo -e "one\ntwo\nthree"`
   (`\n` means "new line" and `-e` tells echo to understand it).
4. Run `cal`. If it says "command not found", don't worry: you'll learn how to
   install it in Lesson 8. Write down what Ubuntu suggests.
5. Use `history` to find the number of your first `echo` command and run it again with `!` and the number.
6. Type `sleep 30` (it waits 30 seconds doing nothing). Don't wait: stop it.

## Quiz

1. What is the name of the shell we are learning?
2. What does `~` in the prompt mean?
3. Which key finishes a word for you?
4. What does `Ctrl` + `C` do in a terminal?
5. What does `command not found` usually mean?

## Recap

| Command | What it does |
|---|---|
| `echo text` | print text |
| `date` | show date and time |
| `whoami` | show your user name |
| `hostname` | show the computer's name |
| `uptime` | how long the computer has been on |
| `clear` | clear the screen |
| `history` | list previous commands |
| `exit` | close the terminal |
