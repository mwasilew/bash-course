# Solutions: Lessons 5–8

## Lesson 5: Getting help

**Exercises**

1. `-t` sorts by modification time, newest first. `ls -lt ~/playground`
2. `ls -S` sorts by size, biggest first. `ls -lS ~/playground`
3. It doesn't exist: `head -S story.txt` prints `head: invalid option -- 'S'`. You can also check `head --help`.
4. `wc -L` prints the length of the longest line. For `story.txt` it's 64.
5. `whatis tac` or `man tac`: it prints a file with the lines in reverse order. It's `cat` backwards!
6. `help cd`: `-P` means "use the physical directory structure without following symbolic links".
   (Symbolic links are shortcuts to other files or folders.)
7. For example:
   - `cat nothere.txt` → `No such file or directory`. Fix: use a file that exists.
   - `cat logs` → `Is a directory`. Fix: `cat logs/server.log`.
   - `cp story.txt` → `missing destination file operand`. Fix: `cp story.txt story2.txt`.

**Quiz**

1. `q`
2. `apropos`
3. The file or folder doesn't exist where you said: spelling mistake, or you're in a different folder.
4. Press `Ctrl` + `C` (you probably forgot to close a quote).
5. A command you don't understand could delete your files or damage the system, especially with `sudo` or `rm`.

## Lesson 6: Searching

**Exercises**

1. `grep -c WARNING logs/server.log` → 10
2. `grep -vn INFO logs/server.log` (15 lines)
3. `grep "logged in" logs/server.log` (15 lines; users ala, bartek and celina)
4. `grep -n tea story.txt` → lines 6 and 31
5. `grep "^On" story.txt` → 8 lines
6. `grep o animals.txt` → dog, koala, lion, octopus (dog appears 3 times)
7. `find treasure -name clue.txt` (4 files)
8. `grep -r secret treasure` → `treasure/mountain/cave/.hidden_chest/treasure.txt: The secret word is: PENGUIN`
9. `find . -empty` → the 13 files in `messy`. They were made with `touch`, so nothing was ever written in them.
10. `find ~ -name "*.txt"`. The number depends on the computer.

**Quiz**

1. `grep` searches for text **inside** files; `find` searches for **files** by name, type, size...
2. `-i`
3. Shows lines that do **not** match.
4. Only directories (folders).
5. The start of the line.

## Lesson 7: Pipes and redirection

**Exercises**

1. `sort animals.txt | uniq | wc -l` → 10
2. `sort animals.txt | uniq -c | sort -nr | head -n 3` → `cat` and `dog`, 3 times each (a tie!)
3. `sort -n numbers.txt | tail -n 1` → 100
4. `sort -t, -k3 -n scores.csv | tail -n 1 | cut -d, -f1` → Franek
5. `grep -c chess scores.csv` → 4
6. `cat shopping/*.txt | sort | uniq > all_shopping.txt` (or `sort -u shopping/*.txt > all_shopping.txt`)
7. `cat shopping/*.txt | sort | uniq -d` → milk
8. `grep -v INFO logs/server.log | tail -n 3`
9. `find ~ -name "*.txt" 2>/dev/null | wc -l`
10. Result: the (20), bit (17), and (10), on (8), a (7). The command:

```bash
cat story.txt | tr -d '.,"' | tr A-Z a-z | tr ' ' '\n' | grep -v "^$" | sort | uniq -c | sort -nr | head -n 5 > top_words.txt
```

11. `tail -n +2 scores.csv | cut -d, -f3 | paste -sd+ | bc` → 234

**Quiz**

1. `>` replaces the file; `>>` adds to the end.
2. Sends the output of the command on the left into the command on the right.
3. `uniq` only removes duplicates that are **next to each other**; sorting puts them together.
4. It sorts as text, character by character, and `1` comes before `5`. Use `sort -n`.
5. A special "black hole" file: everything written to it disappears.

## Lesson 8: Permissions and installing programs

**Exercises**

1. `touch private.txt` then `chmod go-rwx private.txt`. `ls -l` shows `-rw-------`.
2. `chmod u-r private.txt`, `cat private.txt` → `Permission denied`. Fix: `chmod u+r private.txt`.
3. `mkdir locked`, `chmod u-x locked`. `cd locked` → `Permission denied`. `ls locked` shows the
   names (sometimes with errors), but you can't get inside. Fix: `chmod u+x locked`.
4. `apt search game` or `apt search invaders`, then e.g. `sudo apt install ninvaders` and run `ninvaders`.
5. `apt show fortune-mod`: it prints random quotes and jokes. `sudo apt install fortune-mod`, then
   `fortune | cowsay`. (If `fortune` isn't found right away, try `/usr/games/fortune | cowsay`.)
6. `du -sh ~/* | sort -h | tail -n 1`
7. `df -h /` and look at the `Avail` column.

**Quiz**

1. The owner can read, write and execute; the group can read and execute; others can only read.
2. Gives everybody permission to execute (run) the file.
3. The administrator user, who is allowed to do anything.
4. It switches off the protection: one wrong command can damage the whole system.
5. So `apt` knows about the newest versions of the packages.
