#!/bin/bash
# Lesson 9, exercise 4: copy the shopping lists into a folder named with today's date
today=$(date +%F)
cp -r ~/playground/shopping ~/playground/shopping_$today
echo "Backup saved to ~/playground/shopping_$today"
