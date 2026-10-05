#!/bin/bash
# Lesson 9, exercise 2: work out someone's age
read -p "What is your name? " name
read -p "Which year were you born? " born
year=$(date +%Y)
age=$(( year - born ))
echo "Hi $name, you are about $age years old."
