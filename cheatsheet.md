# Bash Cheat Sheet

## Keys

| Keys | Action |
|---|---|
| `Ctrl`+`Alt`+`T` | open a terminal |
| `Tab` / `Tab Tab` | complete a name / show choices |
| `↑` `↓` | previous / next command |
| `Ctrl`+`C` | stop / cancel |
| `Ctrl`+`L` | clear the screen |
| `Ctrl`+`Shift`+`C` / `V` | copy / paste |
| `q` | quit `less`, `man`, `top` |

## Moving around

| Command | Action |
|---|---|
| `pwd` | where am I? |
| `ls`, `ls -la`, `ls -lh` | list (all, long, readable sizes) |
| `cd folder`, `cd ..`, `cd`, `cd -` | go into / up / home / back |
| `~` `.` `..` `/` | home / here / up / root |

## Files and folders

| Command | Action |
|---|---|
| `mkdir -p a/b` | make folders |
| `touch f` | make an empty file |
| `cp a b`, `cp -r A B` | copy file / folder |
| `mv a b` | move or rename |
| `rm f`, `rm -i f`, `rm -r D` | delete (forever!) |
| `*` `?` `[ab]` `{1..5}` | wildcards / expansion |

## Reading and writing

| Command | Action |
|---|---|
| `cat f`, `less f` | show / page through |
| `head -n 5 f`, `tail -n 5 f` | first / last lines |
| `wc -l f` | count lines |
| `nano f` | edit (`Ctrl`+`O` save, `Ctrl`+`X` exit) |

## Help

`cmd --help` · `man cmd` · `help cd` · `apropos word` · `type cmd`

## Searching

| Command | Action |
|---|---|
| `grep word f` | lines containing word |
| `grep -i -c -n -v -w -r` | ignore case, count, numbers, invert, whole word, recursive |
| `find . -name "*.txt"` | find files by name |
| `find . -type d` | find folders |

## Pipes and redirection

| Command | Action |
|---|---|
| `cmd > f`, `cmd >> f` | save / append output |
| `cmd 2>/dev/null` | hide errors |
| `a \| b` | send output of a into b |
| `sort`, `sort -n`, `sort -r` | sort / numbers / reverse |
| `uniq`, `uniq -c` | remove / count duplicates (sort first) |
| `cut -d, -f2` | column 2 |

## System

| Command | Action |
|---|---|
| `chmod +x f` | make runnable |
| `sudo cmd` | run as admin (careful!) |
| `sudo apt update`, `sudo apt install p` | update list / install |
| `ps`, `top`, `kill PID` | processes |
| `df -h`, `du -sh D` | disk space / folder size |

## Scripts

```bash
#!/bin/bash
name="Ala"                      # variable (no spaces around =)
echo "Hi $name"                 # use it
today=$(date +%A)               # command output
sum=$(( 3 + 4 ))                # maths
read -p "Age? " age             # ask
echo "First argument: $1, count: $#"

if [ "$age" -ge 18 ]; then      # -eq -ne -lt -le -gt -ge
    echo "adult"                # =  !=  -z  -n   (text)
elif [ -f "notes.txt" ]; then   # -e -f -d        (files)
    echo "file exists"
else
    echo "neither"
fi

for i in {1..5}; do echo "$i"; done

while [ "$n" -gt 0 ]; do n=$(( n - 1 )); done

case "$x" in
    a|b) echo "a or b" ;;
    *)   echo "something else" ;;
esac
```

Run it: `chmod +x script.sh` then `./script.sh`
