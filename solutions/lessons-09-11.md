# Solutions: Lessons 9–11

The example scripts are in the [`scripts/`](scripts/) folder. All of them have
been tested. Run them with `./name.sh` from inside that folder.

## Lesson 9: Your first scripts

| Exercise | Script |
|---|---|
| 1 | [`about_me.sh`](scripts/about_me.sh) |
| 2 | [`age.sh`](scripts/age.sh) |
| 3 | [`calc.sh`](scripts/calc.sh) |
| 4 | [`backup.sh`](scripts/backup.sh) |
| 5 | [`dice.sh`](scripts/dice.sh) |
| 6 | [`report.sh`](scripts/report.sh): 50 lines, 5 errors, 10 warnings |

**Quiz**

1. The **shebang** (`#!/bin/bash`). It tells Linux which program should run the script.
2. There must be no spaces around `=`: `name=Bob`.
3. Double quotes replace `$name` with its value; single quotes print `$name` literally.
4. `./game.sh` (after `chmod +x game.sh`), or `bash game.sh`.
5. `$1` = `Ala`, `$2` = `cake`, `$#` = `2`.

## Lesson 10: Decisions and loops

| Exercise | Script |
|---|---|
| 1 | [`password.sh`](scripts/password.sh) |
| 2 | [`times.sh`](scripts/times.sh) |
| 3 | [`fizzbuzz.sh`](scripts/fizzbuzz.sh) |
| 4 | [`sort_files.sh`](scripts/sort_files.sh) |
| 5 | [`dice_game.sh`](scripts/dice_game.sh) |
| 6 | [`check.sh`](scripts/check.sh) |
| 7 | [`guess.sh`](scripts/guess.sh) |

**Try it, question 4:** 7 tries always work. Each guess in the middle of what's
left halves the possibilities: 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1.

**Quiz**

1. `if` ends with `fi`; `for` (and `while`) end with `done`.
2. There must be spaces inside the brackets: `[ $x -eq 5 ]`.
3. `[ "$a" = "$b" ]`
4. `for` goes through a list of items; `while` repeats as long as a test is true.
5. `Ctrl` + `C`.

## Final project

An example solution for Project A (the diary) is in [`diary.sh`](scripts/diary.sh).
The other projects have no single right answer. Check them against the checklist
at the end of the project page.
