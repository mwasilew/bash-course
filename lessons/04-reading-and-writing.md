# Lesson 4: Reading and writing text

## Goals

- Show what is inside a file
- Read long files page by page
- Look at just the start or the end of a file
- Count lines and words
- Write and edit files with the `nano` editor

## Learn

```bash
cd ~/playground
```

### Show a whole file: `cat`

```bash
cat welcome.txt
```

`cat` prints the whole file to the screen. Great for short files. It can also
show several files one after another (its name comes from "con**cat**enate",
which means joining together):

```bash
cat shopping/monday.txt shopping/tuesday.txt
```

Add line numbers with `-n`:

```bash
cat -n animals.txt
```

### Read long files: `less`

For a long file, `cat` scrolls past too fast. `less` shows one screen at a time:

```bash
less story.txt
```

Inside `less`:

| Key | What it does |
|---|---|
| `Space` or `Page Down` | next page |
| `b` or `Page Up` | previous page |
| `↑` / `↓` | one line up / down |
| `g` / `G` | go to start / end |
| `/word` then `Enter` | search for "word" (`n` = next match) |
| `q` | **quit** |

The most important one is **`q`** to get out!

### The start or the end: `head` and `tail`

```bash
head story.txt          # first 10 lines
head -n 3 story.txt     # first 3 lines
tail story.txt          # last 10 lines
tail -n 5 story.txt     # last 5 lines
```

`tail` is very useful for log files, where the newest lines are at the end:

```bash
tail -n 3 logs/server.log
```

### Counting: `wc`

`wc` = **w**ord **c**ount. It counts lines, words and characters (bytes):

```bash
wc story.txt
```

Output like `37 238 1299 story.txt` means 37 lines, 238 words, 1299 characters.

Just one of them:

```bash
wc -l animals.txt       # lines
wc -w story.txt         # words
wc -c story.txt         # characters (bytes)
```

### What kind of file is it? `file`

File names don't always tell the truth. `file` looks inside:

```bash
file story.txt
file logs
file /usr/bin/bash
```

### Writing files: the `nano` editor

`nano` is a simple text editor that runs inside the terminal.

```bash
nano diary.txt
```

If the file doesn't exist, nano creates it. Now just type. Use the arrow keys to
move around (the mouse doesn't work in nano).

At the bottom you'll see commands like `^O Write Out` and `^X Exit`.
The `^` symbol means the **`Ctrl`** key. So:

| Keys | What it does |
|---|---|
| `Ctrl` + `O`, then `Enter` | save ("write out") |
| `Ctrl` + `X` | exit (it asks if you want to save: press `Y` then `Enter`) |
| `Ctrl` + `K` | cut a whole line |
| `Ctrl` + `U` | paste the cut line |
| `Ctrl` + `W` | search |
| `Ctrl` + `G` | help |

Write a few lines, save, exit, then check:

```bash
cat diary.txt
```

### A quick way to write one line: `echo` with `>`

You'll learn this properly in Lesson 7, but here's a sneak peek:

```bash
echo "Today I learned nano" > note.txt
cat note.txt
```

The `>` sends the output of `echo` into a file instead of the screen.

## Try it

1. Show `numbers.txt` with line numbers.
2. Open `story.txt` in `less`, search for the word `Friday`, then quit.
3. Show the first 5 lines of `animals.txt`.
4. How many lines does `logs/server.log` have?
5. Use `nano` to create `hello.txt` containing your name and your favourite food.

## Exercises

1. Show the last line of `story.txt`.
2. How many words are in `welcome.txt`?
3. Show lines 1–2 of **both** shopping lists with one command. (Hint: `head` accepts several files.)
4. Open `animals.txt` in `nano`, add three new animals at the end, save, and check with `cat`.
   How many lines does it have now?
5. Show the first line of `scores.csv`. What do you think it is for?
6. **Challenge:** show **only line 6** of `story.txt`. (Hint: combine the idea of `head` and `tail`. You'll learn
   the "proper" way to join commands in Lesson 7, but you can already do it in two steps by saving into a file.)
7. Run `file` on every item in the playground at once using a wildcard.

## Quiz

1. How do you quit `less`?
2. Which command shows the last 10 lines of a file?
3. In nano, what does `^X` mean?
4. What does `wc -l` count?
5. Why is `less` better than `cat` for long files?

## Recap

| Command | What it does |
|---|---|
| `cat file` | show the whole file |
| `cat -n file` | show it with line numbers |
| `less file` | read page by page (`q` to quit) |
| `head -n N file` | first N lines |
| `tail -n N file` | last N lines |
| `wc -l` / `-w` / `-c` | count lines / words / characters |
| `file name` | what kind of file is it |
| `nano file` | edit a file (`Ctrl`+`O` save, `Ctrl`+`X` exit) |
