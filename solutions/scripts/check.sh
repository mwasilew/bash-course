#!/bin/bash
# Lesson 10, exercise 6: tell me about a file or folder
if [ $# -ne 1 ]; then
    echo "Usage: $0 NAME"
    exit 1
fi
if [ ! -e "$1" ]; then
    echo "$1 does not exist."
elif [ -d "$1" ]; then
    echo "$1 is a folder."
elif [ -f "$1" ]; then
    echo "$1 is a file with $(wc -l < "$1") lines."
fi
