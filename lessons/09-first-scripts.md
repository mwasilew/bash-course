# Lesson 9: Your first scripts

## Goals

- Write a script: a file full of commands that runs with one word
- Use variables to remember things
- Ask the user questions with `read`
- Give a script information when you start it (arguments)
- Do maths in Bash

## Learn

### What is a script?

A **script** is a text file containing commands. Running the script runs all the
commands, one after another. Anything you can type in the terminal you can put
in a script.

Make a folder for your scripts:

```bash
mkdir -p ~/scripts
cd ~/scripts
```

### Script number one

```bash
nano hello.sh
```

Type this in:

```bash
#!/bin/bash
# My first script
echo "Hello!"
echo "Today is:"
date
echo "You are in:"
pwd
```

Save (`Ctrl`+`O`, `Enter`) and exit (`Ctrl`+`X`).

- The first line `#!/bin/bash` is called the **shebang**. It tells Linux "run this
  file with Bash". It must be the very first line.
- Lines starting with `#` are comments, for humans.
- `.sh` at the end of the name is just a convention so that people know it's a shell script.

Run it:

```bash
bash hello.sh
```

### Making it runnable

Remember permissions from Lesson 8? Give the script the `x` (execute) permission:

```bash
chmod +x hello.sh
./hello.sh
```

Why `./`? For safety, Bash only looks for commands in a list of special folders, not in
the folder you're in. `./` means "the file `hello.sh` in **this** folder".

### Variables

A **variable** is a named box that holds a value.

```bash
name="Mieszko"
echo "Hello, $name"
```

Rules:

- **No spaces** around `=`. `name = "Mieszko"` does **not** work.
- To **use** the value, put `$` in front: `$name`.
- Use **double quotes** `"..."` around text with variables. Single quotes `'...'`
  show the text exactly as typed, without replacing variables:

```bash
echo "Hello, $name"     # Hello, Mieszko
echo 'Hello, $name'     # Hello, $name
```

When a variable is directly followed by letters, wrap its name in `{ }`:

```bash
animal="cat"
echo "I have two ${animal}s"
```

Linux has some variables already set for you:

```bash
echo $HOME
echo $USER
echo $PWD
echo $RANDOM      # a random number each time!
```

### Saving the output of a command: `$( )`

`$( command )` runs the command and puts its output in that spot:

```bash
today=$(date +%A)
echo "Today is $today"

count=$(ls ~/playground | wc -l)
echo "The playground has $count items"
```

### Asking questions: `read`

`read` waits for the user to type something and stores it in a variable.
`-p` shows a question first:

```bash
#!/bin/bash
read -p "What is your name? " name
read -p "What is your favourite animal? " animal
echo "Hi $name! I like ${animal}s too."
```

Save this as `ask.sh`, make it runnable, and run it.

### Maths: `$(( ))`

Bash can do maths with **whole numbers** inside `$(( ))`:

```bash
echo $(( 2 + 3 ))
echo $(( 10 - 4 ))
echo $(( 6 * 7 ))
echo $(( 20 / 3 ))      # 6, whole numbers only
echo $(( 20 % 3 ))      # 2, the remainder
echo $(( 2 ** 10 ))     # 1024, power

a=5
b=8
echo "$a + $b = $(( a + b ))"
```

Inside `$(( ))` you don't need `$` before variable names.

### Arguments: information given at the start

You can give a script information on the same line you run it:

```bash
./greet.sh Mieszko pizza
```

Inside the script, the first word is `$1`, the second is `$2`, and so on.
`$#` is how many there are, and `$0` is the script's own name:

```bash
#!/bin/bash
# greet.sh - greet someone and mention their favourite food
echo "Hello, $1!"
echo "I heard you like $2."
echo "(You gave me $# arguments.)"
```

### Where to keep scripts so they run from anywhere

If you create a folder called `bin` in your home folder, Ubuntu adds it to the
list of places where Bash looks for commands (you need to log out and in again
the first time):

```bash
mkdir -p ~/bin
cp ~/scripts/hello.sh ~/bin/hello
```

After logging out and in, you can just type `hello` from any folder.

## Try it

1. Write `hello.sh`, make it runnable and run it with `./hello.sh`.
2. Store your favourite colour in a variable and print a sentence using it.
3. Print a random number with `$RANDOM`. Run it a few times.
4. Calculate how many seconds there are in a day using `$(( ))`.

## Exercises

Write each script in `~/scripts`, make it runnable, and test it.

1. **`about_me.sh`**: prints your name, the date, the computer's name and how long it has been
   switched on. Use `whoami`, `date`, `hostname` and `uptime -p`.
2. **`age.sh`**: asks for your name and the year you were born, then prints
   `Hi NAME, you are about AGE years old.` (Use `$(date +%Y)` for the current year.)
3. **`calc.sh`**: takes two numbers as arguments and prints their sum, difference, product, quotient and
   remainder. Example: `./calc.sh 17 5`.
4. **`backup.sh`**: copies the folder `~/playground/shopping` into a new folder whose name includes today's
   date, like `shopping_2026-03-14`. (Hint: `date +%F`.)
5. **`dice.sh`**: prints a random number from 1 to 6. (Hint: `$RANDOM % 6` gives 0 to 5.)
6. **`report.sh`**: prints how many lines, `ERROR`s and `WARNING`s are in `~/playground/logs/server.log`.

## Quiz

1. What is the first line of a Bash script called, and what does it do?
2. What's wrong with `name = Bob`?
3. What's the difference between `echo "$name"` and `echo '$name'`?
4. How do you run a script called `game.sh` that's in the folder you're in?
5. In `./greet.sh Ala cake`, what are `$1`, `$2` and `$#`?

## Recap

| Thing | Example | What it does |
|---|---|---|
| shebang | `#!/bin/bash` | first line: run this with Bash |
| comment | `# note` | ignored by Bash |
| make runnable | `chmod +x s.sh` | allow running the script |
| run | `./s.sh` | run a script in this folder |
| variable | `x="hi"` / `$x` | store / use a value |
| command output | `$(date)` | put a command's output here |
| maths | `$(( 3 * 4 ))` | whole number calculations |
| ask | `read -p "Q? " ans` | ask the user and store the answer |
| arguments | `$1`, `$2`, `$#` | words given when the script is run |
