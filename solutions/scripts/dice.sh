#!/bin/bash
# Lesson 9, exercise 5: roll a die
roll=$(( RANDOM % 6 + 1 ))
echo "You rolled: $roll"
