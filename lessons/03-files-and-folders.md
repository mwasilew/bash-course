# Lesson 3: Making and changing files

## Goals

- Create folders and empty files
- Copy, move, rename and delete files and folders
- Use wildcards to work with many files at once
- Delete things **safely**

## Learn

Do everything in this lesson inside the playground:

```bash
cd ~/playground
```

### Making folders: `mkdir`

`mkdir` = **m**a**k**e **dir**ectory.

```bash
mkdir games
ls
```

Several at once:

```bash
mkdir music films books
```

A folder inside a folder that doesn't exist yet needs `-p` (parents):

```bash
mkdir -p school/maths/homework
ls -R school
```

### Making empty files: `touch`

```bash
touch games/list.txt
ls games
```

`touch` creates an empty file (or, if the file already exists, just updates its
date). Several at once:

```bash
touch books/a.txt books/b.txt books/c.txt
```

### Copying: `cp`

`cp` = **c**o**p**y. First the thing to copy, then where to put it:

```bash
cp welcome.txt welcome_copy.txt     # copy and give it a new name
cp welcome.txt books/               # copy into a folder, keep the name
ls books
```

To copy a whole folder with everything inside, add `-r` (recursive):

```bash
cp -r shopping shopping_backup
ls shopping_backup
```

### Moving and renaming: `mv`

`mv` = **m**o**v**e. It moves a file to another folder:

```bash
mv welcome_copy.txt games/
ls games
```

In Linux, **renaming is moving** to a new name in the same folder:

```bash
mv games/welcome_copy.txt games/hello.txt
ls games
```

`mv` works on folders too, without needing `-r`:

```bash
mv films movies
```

### Deleting: `rm` and `rmdir`

⚠️ **Read this carefully.** In the terminal there is **no Recycle Bin**. Deleted
means **gone forever**.

Delete a file:

```bash
rm games/hello.txt
```

Delete an empty folder:

```bash
rmdir music
```

Delete a folder and everything inside it:

```bash
rm -r shopping_backup
```

Make `rm` ask before deleting each file (a very good habit when learning):

```bash
rm -i books/*.txt
```

Answer `y` for yes or `n` for no.

**Safety rules:**

1. Always check where you are with `pwd` before deleting.
2. Use `ls` with the same name first to see exactly what will be deleted.
3. Never type `rm -rf` with `/` or `~` after it. It would try to delete everything.
4. While learning, only delete things inside `~/playground`.

### Wildcards: working with many files at once

A **wildcard** is a special character that matches many names:

| Wildcard | Matches | Example | Matches |
|---|---|---|---|
| `*` | anything (any number of characters) | `*.jpg` | `cat.jpg`, `beach.jpg` |
| `?` | exactly one character | `song?.mp3` | `song1.mp3`, `song2.mp3` |
| `[...]` | one of the listed characters | `song[12].mp3` | `song1.mp3`, `song2.mp3` |

Look at the messy folder:

```bash
cd ~/playground/messy
ls
ls *.jpg
ls *.mp3
ls s*
ls song?.mp3
```

**Always try a wildcard with `ls` first** before using it with `rm` or `mv`.
This way you see what it matches.

### Brace expansion: a typing shortcut

Curly braces make Bash write out several words for you:

```bash
echo file{1,2,3}.txt
echo {a..e}
echo {1..10}
```

So this creates five folders in one go:

```bash
mkdir -p ~/playground/week/{monday,tuesday,wednesday,thursday,friday}
ls ~/playground/week
```

## Try it

1. In `~/playground`, create a folder `pets` with an empty file `dog.txt` inside.
2. Copy `dog.txt` to `cat.txt` in the same folder.
3. Rename `cat.txt` to `kitten.txt`.
4. Delete `kitten.txt` safely with `rm -i`.
5. Delete the `pets` folder and everything left in it.

## Exercises

### Tidy up the messy folder

The folder `~/playground/messy` has photos, music and documents all mixed up.

1. Inside `messy`, create three folders: `photos`, `music` and `documents`.
2. Move **all** `.jpg` and `.png` files into `photos` (two commands, or one if you're clever).
3. Move all `.mp3` files into `music`.
4. Move all `.txt` and `.csv` files into `documents`.
5. Check the result with `ls -R`. Nothing should be left outside the three folders.

### More exercises

1. In one command, create a folder `year` with the folders `jan`, `feb` and `mar` inside it.
2. Create 10 empty files named `test1.txt` to `test10.txt` in one command.
3. Delete all of them, but only those with **one-digit** numbers (`test1.txt` to `test9.txt`). Check with `ls` first!
4. Make a backup copy of the whole `treasure` folder called `treasure_backup`.
5. What happens if you `cp` a file to a name that already exists? Try it with two files in the playground.
   How can you make `cp` ask first? (Hint: the same option as for `rm`.)

When you're done, reset the playground if you like (ask your teacher).

## Quiz

1. What is the difference between `cp` and `mv`?
2. How do you rename a file?
3. Why do you need `-r` to copy a folder?
4. What does `*.txt` match?
5. Where do files go when you delete them with `rm`?

## Recap

| Command | What it does |
|---|---|
| `mkdir name` | make a folder |
| `mkdir -p a/b/c` | make nested folders |
| `touch file` | make an empty file |
| `cp from to` | copy a file |
| `cp -r from to` | copy a folder |
| `mv from to` | move or rename |
| `rm file` | delete a file (forever!) |
| `rm -i file` | delete, but ask first |
| `rm -r folder` | delete a folder and its contents |
| `rmdir folder` | delete an empty folder |
| `*`, `?`, `[ab]` | wildcards |
| `{a,b,c}`, `{1..5}` | brace expansion |
