#!/bin/bash
# Lesson 10, exercise 5: dice game against the computer, 5 rounds
me=0
computer=0
for round in {1..5}; do
    read -p "Round $round - press Enter to roll..."
    my_roll=$(( RANDOM % 6 + 1 ))
    computer_roll=$(( RANDOM % 6 + 1 ))
    echo "You rolled $my_roll, the computer rolled $computer_roll."
    if [ "$my_roll" -gt "$computer_roll" ]; then
        echo "You win this round!"
        me=$(( me + 1 ))
    elif [ "$my_roll" -lt "$computer_roll" ]; then
        echo "The computer wins this round."
        computer=$(( computer + 1 ))
    else
        echo "A draw."
    fi
done
echo "Final score: you $me, computer $computer"
