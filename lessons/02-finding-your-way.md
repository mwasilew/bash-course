# Lesson 2: Finding your way around

## Goals

- Understand how files and folders are organised in Linux
- Know where you are, look around, and move to other folders
- Understand paths, `~`, `.` and `..`
- Find hidden files

## Learn

### Files and folders are a tree

Everything on the computer is stored in **files**. Files are kept in
**folders** (in the terminal, folders are often called **directories**: same
thing). Folders can contain other folders, so they form a tree, upside down:

```
/                       <- the "root": the very top
├── home
│   └── mieszko         <- your home folder (~)
│       ├── Desktop
│       ├── Documents
│       ├── Downloads
│       ├── Pictures
│       └── playground  <- our practice folder
├── usr
├── etc
└── tmp
```

### Where am I? `pwd`

`pwd` means **p**rint **w**orking **d**irectory: it shows the folder you are in now.

```bash
pwd
```

You'll see something like `/home/mieszko`. That's your **home folder**.

### What's here? `ls`

`ls` means **l**i**s**t. It shows what is in the current folder:

```bash
ls
```

Ubuntu shows folders in **blue** and ordinary files in white.

Useful options:

```bash
ls -l        # long list: size, date, owner
ls -a        # all: show hidden files too
ls -la       # both together
ls -lh       # sizes in readable units like K and M
```

Anything after a `#` is a **comment**. Bash ignores it; it's there to explain things to you.
You don't need to type the comments.

You can also list a folder without going into it:

```bash
ls Documents
ls /
```

### Moving around: `cd`

`cd` means **c**hange **d**irectory.

```bash
cd playground
pwd
ls
```

Now you're inside `playground`. To go back **up** one level use `..`
(two dots mean "the folder above"):

```bash
cd ..
pwd
```

Some special shortcuts:

| Command | Takes you to |
|---|---|
| `cd` | your home folder (from anywhere) |
| `cd ~` | also your home folder |
| `cd ..` | one folder up |
| `cd ../..` | two folders up |
| `cd -` | back to where you were before |
| `cd /` | the root of the whole tree |

Remember `Tab`! Type `cd pla` and press `Tab`: Bash completes `playground/`.

### Paths

A **path** is the address of a file or folder.

An **absolute path** starts with `/` and gives the full address from the root.
It works from anywhere:

```bash
cd /home/mieszko/playground/treasure
```

(Use your own user name instead of `mieszko`. `whoami` tells you what it is.)

A **relative path** does **not** start with `/`. It starts from where you are now:

```bash
cd ~/playground       # start from home
cd treasure/forest    # relative: from playground into treasure, then forest
```

`~` is a shortcut for your home folder, so `~/playground` is the same as
`/home/mieszko/playground`.

One more: a single dot `.` means "this folder, right here". It will be useful later.

### Hidden files

Files and folders whose names start with a dot (like `.bashrc`) are **hidden**.
They're usually settings files. Normal `ls` doesn't show them; `ls -a` does:

```bash
cd
ls
ls -a
```

### Names with spaces

Bash uses spaces to separate parts of a command, so names with spaces need
quotes:

```bash
cd "My Folder"
```

Or avoid the problem: use `_` or `-` instead of spaces in your own file names,
like `my_folder` or `my-folder`.

### A tree picture

The `tree` program draws folders as a tree. It may not be installed yet; you'll
install it in Lesson 8. Until then, `ls -R` (recursive) lists everything inside,
folder by folder:

```bash
ls -R ~/playground/treasure
```

## Try it

1. Go to your home folder and check you're there with `pwd`.
2. List what's in it. Then list it again including hidden files.
3. Go into `playground` and list it in the long format.
4. Go to `/` and look around. Then go back with `cd -`.
5. Go back home with one short command.

## Exercises

### The treasure hunt

There is a treasure hidden somewhere in `~/playground/treasure`. Find it using
**only** `cd`, `ls`, `pwd` and `cat` (`cat file.txt` shows what's inside a file;
you'll learn more about it in Lesson 4).

Start like this:

```bash
cd ~/playground/treasure
ls
cat start.txt
```

Follow the clues. Write down the **secret word** at the end.

### More exercises

1. From your home folder, list the contents of `~/playground/shopping` without using `cd`.
2. Go into `~/playground/treasure/forest/old_tree`. Now go back to `~/playground` using a **relative** path.
3. Do the same thing using an **absolute** path.
4. What is in the folder `/home`? How many users does the computer have?
5. Run `ls -l ~/playground`. Which items are folders? How can you tell, other than the colour?
   (Hint: look at the first letter of each line.)
6. How many hidden files and folders are in your home folder?

## Quiz

1. What does `pwd` stand for?
2. What is the difference between `/home` and `home`?
3. What does `..` mean?
4. You're in `/home/mieszko/playground/treasure`. Where does `cd ../..` take you?
5. How do you show hidden files?

## Recap

| Command | What it does |
|---|---|
| `pwd` | show which folder you are in |
| `ls` | list files and folders |
| `ls -l` / `-a` / `-h` | long list / include hidden / readable sizes |
| `cd folder` | go into a folder |
| `cd ..` | go up one level |
| `cd` or `cd ~` | go home |
| `cd -` | go back to the previous folder |
| `ls -R` | list everything inside, recursively |

| Symbol | Meaning |
|---|---|
| `/` | the root (when at the start of a path) or separator between folders |
| `~` | your home folder |
| `.` | this folder |
| `..` | the folder above |
