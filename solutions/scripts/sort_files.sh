#!/bin/bash
# Lesson 10, exercise 4: tidy the messy folder automatically
cd ~/playground/messy || exit 1
mkdir -p photos music documents
for file in *; do
    # skip the folders we just made
    if [ -d "$file" ]; then
        continue
    fi
    case "$file" in
        *.jpg|*.png) mv "$file" photos/ ;;
        *.mp3)       mv "$file" music/ ;;
        *.txt|*.csv) mv "$file" documents/ ;;
        *)           echo "Don't know where to put $file" ;;
    esac
done
ls -R
