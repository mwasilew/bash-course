#!/bin/bash
# Lesson 10, exercise 7: guessing game that checks the input is a number
secret=$(( RANDOM % 100 + 1 ))
tries=0

echo "I'm thinking of a number between 1 and 100."

while true; do
    read -p "Your guess: " guess
    if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
        echo "That's not a number!"
        continue
    fi
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
