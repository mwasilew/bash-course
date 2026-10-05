# Lesson 7: Pipes and redirection

## Goals

- Save the output of a command into a file
- Feed the output of one command into another with a pipe `|`
- Sort, remove duplicates, and cut columns
- Build your own "command chains" to answer questions

This is where the terminal becomes really powerful. Each command does one small
job well. Pipes let you **snap them together like LEGO bricks**.

## Learn

```bash
cd ~/playground
```

### Saving output to a file: `>`

Normally a command prints its output to the screen. `>` sends it into a file
instead:

```bash
ls > list.txt
cat list.txt
```

⚠️ `>` **replaces** the whole file if it already exists:

```bash
echo "first" > test.txt
echo "second" > test.txt
cat test.txt              # only "second"
```

### Adding to the end of a file: `>>`

`>>` **appends**: it adds to the end and keeps what was already there:

```bash
echo "first" > test.txt
echo "second" >> test.txt
echo "third" >> test.txt
cat test.txt
```

A handy diary trick:

```bash
date >> diary.txt
echo "Learned about pipes today" >> diary.txt
```

### Errors are separate: `2>`

Normal output and error messages travel on two different "channels". `>` only
redirects normal output. To redirect errors use `2>`:

```bash
ls story.txt nothere.txt > out.txt 2> errors.txt
cat out.txt
cat errors.txt
```

`/dev/null` is a special file that throws away everything sent to it, like a black hole:

```bash
ls nothere.txt 2>/dev/null
```

### Pipes: `|`

The **pipe** `|` (`Shift` + `\` on most keyboards) sends the output of the
command on the left into the command on the right:

```bash
ls | wc -l
```

`ls` lists the files; instead of going to the screen, the list goes into `wc -l`,
which counts the lines. So this counts the files in the folder!

More examples:

```bash
grep ERROR logs/server.log | wc -l          # how many errors?
cat story.txt | head -n 3                   # (same as head -n 3 story.txt)
ls -l /usr/bin | less                       # scroll through a long list
history | grep cd                           # which cd commands have I typed?
```

You can join as many commands as you like:

```bash
grep "logged in" logs/server.log | grep ala | wc -l
```

### Sorting: `sort`

```bash
sort animals.txt              # A to Z
sort -r animals.txt           # Z to A (reverse)
sort numbers.txt              # careful! sorts as text: 100 comes before 15
sort -n numbers.txt           # sorts as numbers
sort -nr numbers.txt          # biggest first
```

### Removing duplicates: `uniq`

`uniq` removes repeated lines, but **only if they are next to each other**. That's
why you almost always `sort` first:

```bash
sort animals.txt | uniq
sort animals.txt | uniq -c          # count how many of each
sort animals.txt | uniq -c | sort -nr    # most common first
sort animals.txt | uniq -d          # only the ones that are duplicated
```

### Cutting columns: `cut`

`scores.csv` is a table. Each line has columns separated by commas:

```bash
cat scores.csv
```

`cut` picks out columns. `-d,` says "columns are separated by commas", `-f1`
says "give me field (column) 1":

```bash
cut -d, -f1 scores.csv            # names
cut -d, -f2 scores.csv            # games
cut -d, -f1,3 scores.csv          # names and points
```

And sort the table by its third column, as numbers:

```bash
sort -t, -k3 -n scores.csv
```

(`-t,` = columns separated by commas, `-k3` = sort by column 3.)

### Skipping the header line

The first line of `scores.csv` is a header, not data. `tail -n +2` means "start from line 2":

```bash
tail -n +2 scores.csv
```

### Building a chain step by step

Question: *Which game is the most popular?*

Build the answer one brick at a time, running it after each step:

```bash
tail -n +2 scores.csv
tail -n +2 scores.csv | cut -d, -f2
tail -n +2 scores.csv | cut -d, -f2 | sort
tail -n +2 scores.csv | cut -d, -f2 | sort | uniq -c
tail -n +2 scores.csv | cut -d, -f2 | sort | uniq -c | sort -nr
tail -n +2 scores.csv | cut -d, -f2 | sort | uniq -c | sort -nr | head -n 1
```

This is how everybody builds long commands: add one piece, check, add the next.

### See and save at the same time: `tee`

`tee` saves to a file **and** passes the text along to the screen:

```bash
sort animals.txt | uniq | tee unique_animals.txt
```

### More small tools

```bash
cat numbers.txt | tr '\n' ' '           # tr: replace characters (new lines with spaces)
echo hello | tr a-z A-Z                 # lowercase to uppercase
seq 1 10                                # print numbers 1 to 10
seq 1 10 | paste -sd+ | bc              # add them up! (bc is a calculator)
```

## Try it

1. Save the output of `date` into `today.txt`. Then add the output of `whoami` to the same file.
2. Count the files in `messy` with a pipe. (Reset the playground first if you tidied it in Lesson 3.)
3. Sort `numbers.txt` from biggest to smallest.
4. Show each animal only once, in alphabetical order.

## Exercises

1. How many **different** animals are in `animals.txt`? (One chain of commands.)
2. Which animal appears most often? (There might be a tie!)
3. What is the biggest number in `numbers.txt`? Show only that number.
4. Who scored the most points in `scores.csv`? Show only their name.
5. How many people played chess?
6. Create `all_shopping.txt` containing both shopping lists, sorted, with no duplicates.
7. Which item is on **both** shopping lists?
8. Show the 3 most recent `ERROR` or `WARNING` lines in the log.
   (Hint: `grep -v INFO`)
9. Count how many `.txt` files there are in your whole home folder (look back at Lesson 6, exercise 10).
10. Make a file `top_words.txt` with the 5 most common words in `story.txt`.
    Hints: `tr ' ' '\n'` puts each word on its own line; `tr -d '.,"'` deletes punctuation;
    `tr A-Z a-z` makes everything lowercase; `grep -v "^$"` removes empty lines.
11. **Challenge:** what is the total of all the points in `scores.csv`?

## Quiz

1. What's the difference between `>` and `>>`?
2. What does `|` do?
3. Why do we use `sort` before `uniq`?
4. Why does `sort numbers.txt` put `100` before `15`? How do you fix it?
5. What is `/dev/null`?

## Recap

| Symbol / command | What it does |
|---|---|
| `cmd > file` | save output to a file (replace) |
| `cmd >> file` | add output to the end of a file |
| `cmd 2> file` | save error messages to a file |
| `2>/dev/null` | throw away errors |
| `cmd1 \| cmd2` | send output of cmd1 into cmd2 |
| `sort` / `-n` / `-r` | sort / as numbers / reverse |
| `sort -t, -k3` | sort by column 3, comma separated |
| `uniq` / `-c` / `-d` | remove adjacent duplicates / count / only duplicates |
| `cut -d, -f2` | take column 2, comma separated |
| `tail -n +2` | everything from line 2 onwards |
| `tee file` | save and show at the same time |
| `tr a b` | replace characters |
| `seq 1 10` | count from 1 to 10 |
