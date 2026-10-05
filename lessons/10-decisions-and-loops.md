# Lesson 10: Decisions and loops

## Goals

- Make a script choose what to do with `if`
- Compare numbers and text, and check whether files exist
- Repeat things with `for` and `while` loops
- Write a small game

## Learn

```bash
cd ~/scripts
```

### Decisions: `if`

```bash
#!/bin/bash
read -p "How old are you? " age

if [ "$age" -ge 18 ]; then
    echo "You are an adult."
else
    echo "You are not an adult yet."
fi
```

How it works:

- `if [ test ]; then` ... `fi`. `fi` is `if` backwards and marks the end.
- `else` is optional: what to do when the test is false.
- **Spaces inside `[ ]` are required!** `[ "$age" -ge 18 ]` works,
  `["$age" -ge 18]` does not.
- Put variables inside the test in double quotes. It avoids errors when they are empty.
- The lines inside are indented with spaces. Bash doesn't need this, but it makes scripts much easier to read.

### More than two choices: `elif`

```bash
#!/bin/bash
read -p "What's the temperature? " temp

if [ "$temp" -ge 25 ]; then
    echo "It's hot! Shorts today."
elif [ "$temp" -ge 15 ]; then
    echo "Nice weather. A T-shirt is fine."
elif [ "$temp" -ge 5 ]; then
    echo "Take a jacket."
else
    echo "Brrr! Hat and gloves!"
fi
```

`elif` means "else if". Bash checks each test from the top and runs the **first** one that's true.

### Tests you can use

Comparing **numbers**:

| Test | Means |
|---|---|
| `[ "$a" -eq "$b" ]` | equal |
| `[ "$a" -ne "$b" ]` | not equal |
| `[ "$a" -lt "$b" ]` | less than |
| `[ "$a" -le "$b" ]` | less than or equal |
| `[ "$a" -gt "$b" ]` | greater than |
| `[ "$a" -ge "$b" ]` | greater than or equal |

Comparing **text**:

| Test | Means |
|---|---|
| `[ "$a" = "$b" ]` | same text |
| `[ "$a" != "$b" ]` | different text |
| `[ -z "$a" ]` | empty |
| `[ -n "$a" ]` | not empty |

Checking **files**:

| Test | Means |
|---|---|
| `[ -e "$f" ]` | exists |
| `[ -f "$f" ]` | exists and is a file |
| `[ -d "$f" ]` | exists and is a folder |

Combine tests with `&&` (and) and `||` (or):

```bash
if [ "$age" -ge 13 ] && [ "$age" -le 19 ]; then
    echo "You are a teenager."
fi
```

Example with files:

```bash
#!/bin/bash
read -p "Which file? " f
if [ -f "$f" ]; then
    echo "$f has $(wc -l < "$f") lines."
elif [ -d "$f" ]; then
    echo "$f is a folder."
else
    echo "There is no $f here."
fi
```

### Checking arguments

Good scripts check they were given what they need:

```bash
#!/bin/bash
if [ $# -ne 1 ]; then
    echo "Usage: $0 NAME"
    exit 1
fi
echo "Hello, $1!"
```

`exit 1` stops the script. A number other than 0 means "something went wrong".

### Repeating: the `for` loop

A `for` loop runs the same commands once for **each** item in a list:

```bash
for animal in cat dog fish; do
    echo "I like $animal"
done
```

The variable (`animal`) gets each value in turn. `do` ... `done` mark the
commands to repeat.

Counting:

```bash
for i in {1..10}; do
    echo "$i x 7 = $(( i * 7 ))"
done
```

Every file in a folder (this is where loops become really useful):

```bash
for file in ~/playground/*.txt; do
    echo "$file has $(wc -l < "$file") lines"
done
```

(`wc -l < file` prints only the number, without the file name.)

Every line in a file:

```bash
for animal in $(cat ~/playground/animals.txt); do
    echo "Hello, $animal!"
done
```

### Repeating while something is true: `while`

```bash
#!/bin/bash
count=10
while [ "$count" -gt 0 ]; do
    echo "$count..."
    sleep 1
    count=$(( count - 1 ))
done
echo "Lift off! 🚀"
```

⚠️ If the test never becomes false, the loop runs **forever**. Press `Ctrl` + `C` to stop it.

### Choosing from a menu: `case`

When one variable can have many values, `case` is neater than lots of `elif`s:

```bash
#!/bin/bash
read -p "Pick a fruit (apple/banana/cherry): " fruit
case "$fruit" in
    apple)  echo "Apples are red or green." ;;
    banana) echo "Bananas are yellow." ;;
    cherry) echo "Cherries are small and red." ;;
    *)      echo "I don't know that fruit." ;;
esac
```

`*)` catches everything else. `esac` is `case` backwards.

### Putting it together: a guessing game

Save this as `guess.sh`, make it runnable, and play:

```bash
#!/bin/bash
# Guess the number game
secret=$(( RANDOM % 100 + 1 ))
tries=0

echo "I'm thinking of a number between 1 and 100."

while true; do
    read -p "Your guess: " guess
    tries=$(( tries + 1 ))

    if [ "$guess" -lt "$secret" ]; then
        echo "Too small!"
    elif [ "$guess" -gt "$secret" ]; then
        echo "Too big!"
    else
        echo "Correct! You needed $tries tries."
        break
    fi
done
```

`while true` loops forever, and `break` jumps out of the loop.

## Try it

1. Write a script that asks for a number and says whether it is even or odd.
   (Hint: a number is even if `$(( n % 2 ))` is `0`.)
2. Print the numbers 1 to 20 with a `for` loop.
3. Run the countdown script. Change it to count down from 5.
4. Play the guessing game. What's the smallest number of tries that **always** works?

## Exercises

1. **`password.sh`**: asks for a password. If it's `open sesame`, print `Welcome!`, otherwise print `Go away!`.
   Then improve it: give the user 3 tries.
2. **`times.sh`**: takes a number as an argument and prints its multiplication table from 1 to 10.
   If no argument is given, print a usage message and exit.
3. **`fizzbuzz.sh`**: print the numbers 1 to 30, but print `Fizz` instead of numbers divisible by 3,
   `Buzz` instead of numbers divisible by 5, and `FizzBuzz` for numbers divisible by both.
4. **`sort_files.sh`**: tidies `~/playground/messy` automatically (like Lesson 3, but with a loop):
   for each file, look at its ending and move it into `photos`, `music` or `documents`.
   Hints: `case "$file" in *.jpg|*.png) ... ;;`. Reset the playground first.
5. **`dice_game.sh`**: you and the computer each roll a die (1–6). Say who wins, or if it's a draw.
   Then make it play 5 rounds and keep the score.
6. **`check.sh`**: takes a file name as an argument and says whether it exists, whether it is a file or a
   folder, and, if it's a file, how many lines it has.
7. Improve the guessing game: if the user types something that is not a number, say so instead of
   showing an error. (Hint: `[[ "$guess" =~ ^[0-9]+$ ]]` is true when `guess` contains only digits.)

## Quiz

1. How does an `if` block end? How does a `for` loop end?
2. Why is `[$x -eq 5]` wrong?
3. Which test checks that two pieces of **text** are the same?
4. What's the difference between a `for` loop and a `while` loop?
5. How do you stop a loop that runs forever?

## Recap

```bash
if [ test ]; then        for x in a b c; do        while [ test ]; do
    ...                      ...                       ...
elif [ test ]; then      done                      done
    ...
else                     case "$x" in
    ...                      a) ... ;;
fi                           *) ... ;;
                         esac
```

| Thing | Meaning |
|---|---|
| `-eq -ne -lt -le -gt -ge` | number comparisons |
| `=` `!=` `-z` `-n` | text comparisons |
| `-e -f -d` | exists / is a file / is a folder |
| `&&`, `\|\|` | and, or |
| `break` | jump out of a loop |
| `exit 1` | stop the script with an error |
