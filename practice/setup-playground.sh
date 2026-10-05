#!/bin/bash
# Creates the practice folder ("playground") used by the exercises in the course.
#
# Usage:
#   bash setup-playground.sh           create ~/playground (refuses if it already exists)
#   bash setup-playground.sh --reset   delete ~/playground and create a fresh copy

PLAYGROUND="$HOME/playground"

if [ -e "$PLAYGROUND" ]; then
    if [ "$1" = "--reset" ]; then
        echo "Removing the old playground..."
        rm -rf "$PLAYGROUND"
    else
        echo "The playground already exists at $PLAYGROUND"
        echo "To start again from scratch run:  bash $0 --reset"
        exit 1
    fi
fi

mkdir -p "$PLAYGROUND"
cd "$PLAYGROUND" || exit 1

# --- welcome -------------------------------------------------------------
cat > welcome.txt <<'EOF'
Welcome to your playground!

Everything in this folder exists only so you can practise.
You can look at it, change it, move it and even delete it.
If you break something, ask for the playground to be reset
and you get a fresh copy.

Have fun!
EOF

# --- lists for sorting and counting --------------------------------------
cat > animals.txt <<'EOF'
cat
dog
zebra
elephant
cat
lion
giraffe
dog
penguin
cat
koala
lion
octopus
dog
bear
EOF

cat > numbers.txt <<'EOF'
42
7
100
3
58
21
9
77
15
64
EOF

cat > scores.csv <<'EOF'
name,game,points
Ala,chess,12
Bartek,football,30
Celina,chess,25
Darek,minecraft,47
Ewa,football,18
Franek,minecraft,52
Gosia,chess,9
Henryk,chess,41
EOF

# --- a longer text for head, tail, less and grep -------------------------
cat > story.txt <<'EOF'
The Robot Who Wanted to Learn
=============================

Once upon a time, in a small workshop at the edge of a town,
there lived a little robot called Bit.
Bit could sweep the floor, carry boxes and make tea,
but Bit was not happy.

"I want to learn new things," said Bit one morning.
The old inventor looked up from her desk and smiled.
"Then you must learn to talk to the computer," she said.

The computer sat in the corner of the workshop.
It had a black screen with a small blinking cursor.
Bit typed the first word it could think of: hello.
The computer answered: command not found.

Bit was confused, but did not give up.
The inventor showed Bit a word called echo.
Bit typed: echo hello
And the computer answered: hello

From that day on, Bit learned one new command every day.
On Monday Bit learned ls, and saw all the files in the folder.
On Tuesday Bit learned cd, and walked from folder to folder.
On Wednesday Bit learned mkdir, and built new folders.
On Thursday Bit learned grep, and found words in long files.
On Friday Bit learned to write scripts,
and the computer started doing Bit's work for it.

On Saturday Bit swept the floor, carried the boxes and made tea,
all at the same time, with one small script.

On Sunday Bit rested,
and the computer said: hello, Bit.

THE END
EOF

# --- a log file for searching --------------------------------------------
levels=(INFO INFO INFO WARNING INFO ERROR INFO INFO WARNING INFO)
messages=(
    "user ala logged in"
    "backup started"
    "backup finished"
    "disk is 80% full"
    "user bartek logged in"
    "printer not responding"
    "user ala logged out"
    "email sent"
    "password will expire soon"
    "user celina logged in"
)
for hour in 08 09 10 11 12; do
    for i in "${!levels[@]}"; do
        printf '2026-03-14 %s:%02d:00 %s %s\n' "$hour" $((i * 5)) "${levels[$i]}" "${messages[$i]}"
    done
done > server.log
mkdir logs
mv server.log logs/

# --- shopping lists ------------------------------------------------------
mkdir shopping
printf 'bread\nmilk\napples\ncheese\n' > shopping/monday.txt
printf 'pasta\ntomatoes\nmilk\nchocolate\n' > shopping/tuesday.txt

# --- a messy folder to tidy up -------------------------------------------
mkdir messy
touch messy/{holiday,beach,birthday,cat}.jpg
touch messy/{dog,sunset}.png
touch messy/{song1,song2,song3}.mp3
touch messy/{homework,notes,ideas}.txt
touch messy/budget.csv

# --- a treasure hunt for practising cd and ls ---------------------------
mkdir -p treasure/forest/old_tree treasure/mountain/cave/.hidden_chest treasure/river
cat > treasure/start.txt <<'EOF'
Welcome, explorer!

Your first clue is waiting in the forest.
Go into the forest folder and look around.
EOF
cat > treasure/forest/clue.txt <<'EOF'
Well done! Clue number 2:
Something is hiding inside the old tree.
EOF
cat > treasure/forest/old_tree/clue.txt <<'EOF'
Clue number 3:
Go back up TWO levels (to the treasure folder),
then climb the mountain and enter the cave.
Tip: cd ../.. takes you up two levels.
EOF
cat > treasure/mountain/cave/clue.txt <<'EOF'
Clue number 4:
The cave looks empty... but is it?
Some folders are hidden. Their names start with a dot.
Try:  ls -a
EOF
cat > treasure/mountain/cave/.hidden_chest/treasure.txt <<'EOF'
*** YOU FOUND THE TREASURE! ***

You can now move around the file system like a real explorer.
The secret word is: PENGUIN
EOF
cat > treasure/river/clue.txt <<'EOF'
Just fish here. No clue. Try somewhere else!
EOF

echo "Done! Your playground is ready at: $PLAYGROUND"
