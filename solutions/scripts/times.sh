#!/bin/bash
# Lesson 10, exercise 2: multiplication table
if [ $# -ne 1 ]; then
    echo "Usage: $0 NUMBER"
    exit 1
fi
for i in {1..10}; do
    echo "$i x $1 = $(( i * $1 ))"
done
