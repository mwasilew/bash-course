# Lesson 8: Permissions and installing programs

## Goals

- Read file permissions in `ls -l`
- Change permissions with `chmod`
- Understand what `sudo` is and when to use it (and when not to)
- Install, update and remove programs with `apt`
- See and stop running programs

## Learn

### Who is allowed to do what?

Linux is built for many users sharing one computer. Every file has an **owner**
and **permissions** that say who may do what with it.

```bash
cd ~/playground
ls -l
```

You'll see lines like:

```
-rw-rw-r-- 1 mieszko mieszko  168 Mar 14 10:00 welcome.txt
drwxrwxr-x 2 mieszko mieszko 4096 Mar 14 10:00 logs
```

The first column is the permissions. Let's take it apart:

```
 -    rw-    rw-    r--
type  user  group  others
```

- **type**: `-` is a file, `d` is a directory (folder)
- then three groups of three letters, for:
  - **user**: the owner of the file (you)
  - **group**: a group of users the file belongs to
  - **others**: everybody else

Each group of three is always in the same order:

| Letter | Permission | For a file | For a folder |
|---|---|---|---|
| `r` | read | look inside the file | list what's in it |
| `w` | write | change the file | add/remove files in it |
| `x` | execute | run it as a program | go into it with `cd` |
| `-` | — | not allowed | not allowed |

So `rw-rw-r--` means: the owner can read and write, the group can read and
write, everybody else can only read. Nobody can run it as a program.

### Changing permissions: `chmod`

`chmod` = **ch**ange **mod**e. Say **who** (`u` user, `g` group, `o` others,
`a` all), **add or remove** (`+` or `-`), and **what** (`r`, `w`, `x`):

```bash
echo "top secret" > secret.txt
ls -l secret.txt
chmod o-r secret.txt        # others can no longer read it
ls -l secret.txt
chmod u-w secret.txt        # even you can't change it now
echo "change" > secret.txt  # Permission denied!
chmod u+w secret.txt        # give it back
```

The most common use is making a script runnable, which you'll do in Lesson 9:

```bash
chmod +x myscript.sh
```

### The boss of the computer: `root` and `sudo`

There is one special user called **root** who is allowed to do *everything*:
change any file, install programs, even delete the whole system.

Your normal user can't change system files. Try:

```bash
ls -l /etc/hostname
echo test > /etc/hostname     # Permission denied. Good!
```

This protects the computer from mistakes. When you really need to do an admin job,
you put **`sudo`** in front of the command. It means "do this as root". It asks for
your password (nothing appears while you type it, not even stars; that's normal).

⚠️ **The `sudo` rule:** `sudo` turns off the safety net. Only use it when you
know exactly what the command does, and never with a command copied from the
internet that you don't understand. While learning, only use `sudo` with your
teacher.

### Installing programs: `apt`

Ubuntu gets programs from **software repositories**: big online collections of
programs (called **packages**) that are checked and safe. `apt` is the tool to use them.

First, update the list of available packages (do this before installing):

```bash
sudo apt update
```

Install some fun and useful programs:

```bash
sudo apt install tree cowsay sl ncal
```

`apt` shows what it will install and asks `Do you want to continue? [Y/n]`.
Press `Enter` (or `Y`).

Try them:

```bash
tree ~/playground/treasure
tree -a ~/playground/treasure     # include hidden
cowsay "I can install programs!"
sl                                # what happens if you mistype ls...
cal
```

Other `apt` commands:

```bash
apt search weather            # search for packages (no sudo needed)
apt show cowsay               # information about a package
sudo apt upgrade              # update all installed programs
sudo apt remove sl            # uninstall a program
```

### Running programs: processes

Every running program is a **process**. See yours:

```bash
ps
ps aux | less             # every process on the computer
```

`top` shows processes live, like a task manager (press `q` to quit).
A nicer version can be installed:

```bash
sudo apt install htop
htop
```

Stop a program that's stuck:

1. Find its number (the **PID**) with `ps aux | grep name`
2. `kill PID`

Let's practise with a harmless program that just waits:

```bash
sleep 1000 &          # & runs it in the background, so you can keep typing
ps                    # find the PID of sleep
kill 12345            # use the real PID you saw
ps                    # it's gone
```

### How much space? `df` and `du`

```bash
df -h               # free space on the disks
du -sh ~/playground # size of a folder
du -sh ~/*          # size of everything in your home folder
```

## Try it

1. Look at the permissions of `story.txt`. Who can read it? Who can change it?
2. Look at the permissions of `/usr/bin/ls`. Why does it have `x`?
3. Install `tree` (with your teacher) and draw the playground.
4. Start `sleep 500 &` and stop it with `kill`.

## Exercises

1. Create `private.txt` and change the permissions so **only you** can read and write it
   (no permissions at all for group and others). What does `ls -l` show?
2. Remove your own read permission from `private.txt` and try to `cat` it. What happens? Give it back.
3. Make a folder `locked` and remove your `x` permission from it. Can you `cd` into it? Can you `ls` it? Fix it.
4. Use `apt search` to find a package that plays a game in the terminal. (Ideas: `ninvaders`, `moon-buggy`,
   `bastet`, `nsnake`). With your teacher, install one and play it.
5. Use `apt show` to find out what the `fortune-mod` package does. Install it and combine `fortune` with
   `cowsay` using a pipe.
6. Which folder in your home folder takes up the most space?
7. How much free space is there on the main disk (the one mounted on `/`)?

## Quiz

1. What does `rwxr-xr--` mean?
2. What does `chmod +x file` do?
3. Who is `root`?
4. Why should you be careful with `sudo`?
5. Why do we run `sudo apt update` before installing?

## Recap

| Command | What it does |
|---|---|
| `ls -l` | show permissions |
| `chmod u+x file` | give the owner (u) execute (x) permission |
| `chmod o-r file` | take read permission away from others |
| `sudo command` | run a command as root (admin) |
| `sudo apt update` | refresh the list of packages |
| `sudo apt install pkg` | install a program |
| `sudo apt remove pkg` | uninstall a program |
| `apt search word` | search for programs |
| `ps`, `ps aux` | list running processes |
| `top` / `htop` | live process viewer (`q` to quit) |
| `command &` | run in the background |
| `kill PID` | stop a process |
| `df -h` / `du -sh` | free disk space / size of a folder |
