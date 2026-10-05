#!/bin/bash
# Lesson 10, exercise 1: a password check with 3 tries
for try in 1 2 3; do
    read -p "Password: " password
    if [ "$password" = "open sesame" ]; then
        echo "Welcome!"
        exit 0
    fi
    echo "Wrong! ($try of 3)"
done
echo "Go away!"
exit 1
