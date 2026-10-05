#!/bin/bash
# Lesson 9, exercise 1: a few facts about me and this computer
echo "My name is: $(whoami)"
echo "Today is: $(date)"
echo "This computer is called: $(hostname)"
echo "It has been switched on for: $(uptime -p)"
