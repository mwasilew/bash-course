# Lesson 6: Searching

## Goals

- Find words and lines inside files with `grep`
- Find files and folders by name, type or size with `find`

## Learn

```bash
cd ~/playground
```

### Searching inside files: `grep`

`grep` prints every **line** that contains the word you're looking for:

```bash
grep cat animals.txt
grep Bit story.txt
grep ERROR logs/server.log
```

The general form is:

```
grep  [options]  what_to_find  where_to_look
```

Useful options:

| Option | What it does | Example |
|---|---|---|
| `-i` | ignore upper/lowercase | `grep -i the story.txt` |
| `-c` | only **count** matching lines | `grep -c ERROR logs/server.log` |
| `-n` | show line numbers | `grep -n tea story.txt` |
| `-v` | show lines that do **not** match | `grep -v INFO logs/server.log` |
| `-w` | whole words only | `grep -w cat animals.txt` |
| `-r` | search all files in a folder and its subfolders | `grep -r clue treasure` |
| `-l` | only show the **names** of files that match | `grep -rl clue treasure` |

If what you're searching for has spaces, put it in quotes:

```bash
grep "logged in" logs/server.log
```

Try the difference between these two:

```bash
grep the story.txt
grep -w the story.txt
```

The first one also matches `there`, `then` and `other`.

### Patterns (a tiny taste)

`grep` understands special characters for patterns. Two very useful ones:

| Pattern | Means | Example |
|---|---|---|
| `^` | start of the line | `grep "^On" story.txt` |
| `$` | end of the line | `grep "tea,$" story.txt` |

```bash
grep "^c" animals.txt      # animals starting with c
grep "a$" animals.txt      # animals ending with a
```

Put patterns in quotes so Bash doesn't try to understand the special characters itself.

### Finding files: `find`

`grep` searches **inside** files. `find` searches for the **files themselves**.

```
find  where_to_look  what_to_look_for
```

Find by name:

```bash
find . -name "clue.txt"
find . -name "*.jpg"
```

(Remember `.` means "this folder". `find` also looks in all folders inside it.)

Ignore upper/lowercase with `-iname`:

```bash
find . -iname "*.TXT"
```

Only folders, or only files:

```bash
find . -type d          # d = directory
find . -type f          # f = file
find treasure -type d
```

Find by size, or by how recently they changed:

```bash
find . -size +1k              # bigger than 1 kilobyte
find . -empty                 # empty files and folders
find . -mmin -60              # changed in the last 60 minutes
```

Mix conditions; they must all be true:

```bash
find . -type f -name "*.txt"
```

Hidden files are found too, so `find` is a great way to cheat in a treasure hunt:

```bash
find treasure -name "treasure.txt"
```

### Errors while searching the whole computer

If you search from `/`, you'll see lots of `Permission denied` errors for folders
you're not allowed to look in. Hide error messages by adding `2>/dev/null`
(explained in Lesson 7):

```bash
find / -name "bash" 2>/dev/null
```

## Try it

1. Show all lines in `animals.txt` that contain `dog`.
2. Count how many times `ERROR` appears in the log.
3. Find all `.mp3` files in the playground.
4. List all folders inside `treasure`, including hidden ones.

## Exercises

Use `~/playground` for all of these.

1. How many lines in `logs/server.log` are `WARNING`s?
2. Show all log lines that are **not** `INFO`, with line numbers.
3. Which users logged in? Show only those lines.
4. On which line numbers of `story.txt` does the word `tea` appear?
5. Show all lines of `story.txt` that start with `On`. How many are there?
6. Which animals in `animals.txt` contain the letter `o`?
7. Find every file named `clue.txt` in the treasure hunt.
8. Use one `grep` command to find which file in `treasure` contains the secret word.
   (Hint: the secret is in a line containing `secret`.)
9. Find all empty files in the playground. Why are they empty?
10. Find all files in your **whole home folder** that end in `.txt`. How many are there?
    (You'll learn to count them easily in Lesson 7. For now, just look.)

## Quiz

1. What is the difference between `grep` and `find`?
2. Which option makes `grep` ignore uppercase and lowercase?
3. What does `grep -v` do?
4. What does `-type d` mean in `find`?
5. What does `^` mean in a `grep` pattern?

## Recap

| Command | What it does |
|---|---|
| `grep word file` | show lines containing word |
| `grep -i` / `-c` / `-n` / `-v` / `-w` | ignore case / count / line numbers / invert / whole words |
| `grep -r word folder` | search inside every file in a folder |
| `grep "^x"` / `"x$"` | lines starting / ending with x |
| `find . -name "*.txt"` | find files by name |
| `find . -type f` / `-type d` | only files / only folders |
| `find . -size +1k` | bigger than 1 KB |
| `find . -empty` | empty files and folders |
