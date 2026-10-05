# Solutions: Lessons 1–4

Try every exercise yourself before looking here. There is often more than one
correct answer: if yours works, it's right!

## Lesson 1: Meet the terminal

**Exercises**

1. `date`
2. `date +%B`
3. `echo -e "one\ntwo\nthree"`
4. On a fresh Ubuntu you'll see something like:
   `Command 'cal' not found, but can be installed with: sudo apt install ncal`.
   Ubuntu tells you which package to install. You'll do that in Lesson 8.
5. `history`, find the number (say 7), then `!7`.
6. Press `Ctrl` + `C`.

**Quiz**

1. Bash.
2. Your home folder.
3. `Tab`.
4. It stops the running command (it does **not** copy).
5. There's no command with that name: a typo, or the program isn't installed.

## Lesson 2: Finding your way around

**Treasure hunt**

```bash
cd ~/playground/treasure
cat start.txt
cd forest
cat clue.txt
cd old_tree
cat clue.txt
cd ../..
cd mountain/cave
cat clue.txt
ls -a
cd .hidden_chest
cat treasure.txt
```

The secret word is **PENGUIN**. (The `river` folder is a dead end.)

**Exercises**

1. `ls ~/playground/shopping`
2. `cd ~/playground/treasure/forest/old_tree` then `cd ../../..`
3. `cd /home/YOUR_NAME/playground` (or `cd ~/playground`, which Bash turns into the absolute path)
4. `ls /home`. Normally each user has one folder there. Often it's only you.
5. Lines starting with `d` are directories; lines starting with `-` are files.
6. `ls -a ~` and count the names starting with `.` (don't count `.` and `..`).
   The number depends on the computer.

**Quiz**

1. Print working directory.
2. `/home` is an absolute path (the `home` folder in the root). `home` is relative:
   a folder called `home` inside the current folder.
3. The folder above the current one.
4. `/home/mieszko`
5. `ls -a`

## Lesson 3: Making and changing files

**Tidy up the messy folder**

```bash
cd ~/playground/messy
mkdir photos music documents
mv *.jpg *.png photos/
mv *.mp3 music/
mv *.txt *.csv documents/
ls -R
```

**Exercises**

1. `mkdir -p year/{jan,feb,mar}`
2. `touch test{1..10}.txt`
3. `ls test?.txt` to check, then `rm test?.txt`. (`?` is exactly one character, so `test10.txt` is not matched.)
4. `cp -r treasure treasure_backup`
5. The old file is replaced without asking! `cp -i` asks first.

**Quiz**

1. `cp` makes a copy and the original stays; `mv` moves it, so the original is gone from the old place.
2. With `mv old_name new_name`.
3. A folder contains other files; `-r` (recursive) tells `cp` to copy everything inside.
4. All names ending in `.txt`.
5. Nowhere: they're gone for good. There's no Recycle Bin in the terminal.

## Lesson 4: Reading and writing text

**Exercises**

1. `tail -n 1 story.txt` → `THE END`
2. `wc -w welcome.txt` → 46 words
3. `head -n 2 shopping/monday.txt shopping/tuesday.txt`
4. `nano animals.txt`, add the animals, `Ctrl`+`O`, `Enter`, `Ctrl`+`X`. `wc -l animals.txt` → 18 lines.
5. `head -n 1 scores.csv` → `name,game,points`. It's the **header**: it names the columns.
6. Two steps: `head -n 6 story.txt > part.txt` then `tail -n 1 part.txt`.
   Answer: `Bit could sweep the floor, carry boxes and make tea,`
   (After Lesson 7 you can do it in one: `head -n 6 story.txt | tail -n 1`.)
7. `file *`

**Quiz**

1. `q`
2. `tail`
3. `Ctrl` + `X`: exit.
4. Lines.
5. `less` shows one page at a time and lets you scroll and search; `cat` dumps it all at once.
