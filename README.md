# Bash for Beginners

A hands-on course in using the Linux terminal and Bash on Ubuntu, written for
someone who has never typed a command before.

By the end of the course the learner can:

- open a terminal and move around the file system without a mouse
- create, copy, move, rename and delete files and folders
- read and edit text files from the terminal
- find files and search for words inside them
- combine small commands into powerful ones with pipes
- install programs and understand file permissions
- write small Bash scripts that use variables, questions, decisions and loops

## How the course works

There are 10 lessons and a final project. Each lesson takes about
**45–60 minutes** and has the same parts:

| Part | What happens |
|---|---|
| **Goals** | What you will be able to do after the lesson |
| **Learn** | Short explanations, each followed by commands to type |
| **Try it** | Small tasks to do straight away, inside the lesson |
| **Exercises** | Practice tasks; answers are in `solutions/` |
| **Quiz** | A few quick questions to check understanding |
| **Recap** | The commands from the lesson in one table |

Type every command yourself. Do not copy and paste: typing is how your fingers
and your memory learn.

## Before the first lesson (for the teacher)

1. Use a computer running Ubuntu (any recent version, desktop edition).
2. Copy this `bash-course` folder onto it.
3. Create the practice folder by opening a terminal (`Ctrl` + `Alt` + `T`) and running:

   ```bash
   bash ~/path/to/bash-course/practice/setup-playground.sh
   ```

   This creates `~/playground`, a folder of practice files that the exercises
   use. Nothing outside it is touched.
4. If the playground gets messed up, reset it to a fresh copy at any time:

   ```bash
   bash ~/path/to/bash-course/practice/setup-playground.sh --reset
   ```

Lesson 8 installs a few small programs with `sudo apt install`, so the learner
needs either the computer's password or a teacher sitting next to them.

## Lessons

| # | Lesson | Main commands |
|---|---|---|
| 1 | [Meet the terminal](lessons/01-meet-the-terminal.md) | `echo`, `date`, `whoami`, `clear`, `history` |
| 2 | [Finding your way around](lessons/02-finding-your-way.md) | `pwd`, `ls`, `cd` |
| 3 | [Making and changing files](lessons/03-files-and-folders.md) | `mkdir`, `touch`, `cp`, `mv`, `rm` |
| 4 | [Reading and writing text](lessons/04-reading-and-writing.md) | `cat`, `less`, `head`, `tail`, `wc`, `nano` |
| 5 | [Getting help](lessons/05-getting-help.md) | `--help`, `man`, `type`, error messages |
| 6 | [Searching](lessons/06-searching.md) | `grep`, `find` |
| 7 | [Pipes and redirection](lessons/07-pipes-and-redirection.md) | `>`, `>>`, `\|`, `sort`, `uniq`, `cut` |
| 8 | [Permissions and installing programs](lessons/08-permissions-and-programs.md) | `chmod`, `sudo`, `apt` |
| 9 | [Your first scripts](lessons/09-first-scripts.md) | shebang, variables, `read`, arguments |
| 10 | [Decisions and loops](lessons/10-decisions-and-loops.md) | `if`, `for`, `while` |
| ★ | [Final project](lessons/11-final-project.md) | everything |

Also included:

- [`cheatsheet.md`](cheatsheet.md): every command from the course on one page. Print it!
- [`solutions/`](solutions/): answers to all exercises. Try first, peek later.
- [`practice/setup-playground.sh`](practice/setup-playground.sh): creates the practice folder.

## Tips for the learner

- **You cannot break the computer** by working inside `~/playground`. Experiment!
- When stuck, press `Ctrl` + `C`. It stops whatever is running and gives you a fresh line.
- Error messages are not failures. Read them: they usually say exactly what is wrong.
- Use the `Tab` key. It finishes names for you and saves typing mistakes.
- Uppercase and lowercase are different in Linux: `Story.txt` and `story.txt` are two different files.
