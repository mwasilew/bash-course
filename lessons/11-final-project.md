# Final project

Time to put everything together! Pick **one** project (or more, if you're
enjoying it). Each one uses commands and ideas from the whole course.

Plan before you type:

1. Write down, in plain words, what the script should do, step by step.
2. Build it a little at a time. Run it after every few lines.
3. When it works, add comments so someone else can understand it.
4. Show it to your teacher and explain how it works.

---

## Project A: My diary

A script `diary.sh` that keeps a diary in `~/diary.txt`.

**Must have:**

- When run with `add`, it asks "What happened today?" and appends the date and the answer to the diary.
- When run with `show`, it shows the whole diary with `less`.
- When run with `last`, it shows the last 5 entries.
- When run with `search WORD`, it shows the entries containing that word.
- When run with anything else (or nothing), it prints how to use it.

**Ideas for extras:** count how many entries there are; add a mood (`happy`, `tired`...) to each entry and
show statistics of moods with `sort | uniq -c`.

Example:

```
$ ./diary.sh add
What happened today? I learned bash loops
Saved!
$ ./diary.sh search loops
2026-03-14 18:05 | I learned bash loops
```

---

## Project B: The quiz master

A script `quiz.sh` that asks the player questions and keeps score.

**Must have:**

- At least 5 questions (they can be about Bash!).
- Says "Correct!" or "Wrong, the answer was ..." after each.
- At the end prints the score, e.g. `You got 4 out of 5`.
- Prints a different message depending on the score (e.g. 5 = "Bash master!", 3–4 = "Well done", less = "Try again").

**Ideas for extras:** read the questions and answers from a file `questions.txt`, one per line like
`What command shows your current folder?|pwd`, and use `cut -d'|'` to split them; ask questions in random
order with `shuf`; save the high score to a file.

---

## Project C: The folder tidier

A script `tidy.sh` that takes a folder as an argument and sorts its files into subfolders by type.

**Must have:**

- Checks that it was given exactly one argument, and that it is a folder.
- Creates `images`, `music`, `documents` and `other` folders inside it, if they don't exist.
- Moves `.jpg`, `.png`, `.gif` into `images`; `.mp3`, `.wav` into `music`; `.txt`, `.pdf`, `.csv` into `documents`;
  everything else into `other`.
- Prints what it moved, and at the end, how many files went into each folder.

**Ideas for extras:** a `--dry-run` option that only *shows* what it would do without moving anything;
work with upper-case endings like `.JPG` too.

Test it on `~/playground/messy` (reset the playground first). **Never test it on a real folder until you're sure it works!**

---

## Project D: System report

A script `sysreport.sh` that writes a report about the computer into `report_DATE.txt`.

**Must have:**

- Date and time, user name, computer name, and how long it has been on.
- Free disk space for `/`.
- The 5 biggest items in your home folder (`du -sh ~/* | sort -h | tail -n 5`).
- How many `.txt`, `.jpg` and `.sh` files are in your home folder.
- Prints "Report saved to ..." at the end.

**Ideas for extras:** show the 5 processes using the most memory (`ps aux --sort=-%mem | head -n 6`);
show a warning if the disk is more than 90% full.

---

## Checklist for every project

- [ ] Starts with `#!/bin/bash`
- [ ] Is runnable (`chmod +x`)
- [ ] Has comments explaining the main parts
- [ ] Variables in tests are in double quotes
- [ ] Checks its arguments and prints a usage message when they're wrong
- [ ] Has been tested with good input **and** with bad input

Congratulations on finishing the course! 🎉
