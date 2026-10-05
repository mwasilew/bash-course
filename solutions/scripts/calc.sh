#!/bin/bash
# Lesson 9, exercise 3: a tiny calculator
# Usage: ./calc.sh 17 5
a=$1
b=$2
echo "$a + $b = $(( a + b ))"
echo "$a - $b = $(( a - b ))"
echo "$a * $b = $(( a * b ))"
echo "$a / $b = $(( a / b ))"
echo "$a % $b = $(( a % b ))  (the remainder)"
