#!/bin/bash
# Final project A: a diary kept in ~/diary.txt
# Usage: ./diary.sh add | show | last | search WORD

diary=~/diary.txt
touch "$diary"

case "$1" in
    add)
        read -p "What happened today? " entry
        echo "$(date '+%F %H:%M') | $entry" >> "$diary"
        echo "Saved!"
        ;;
    show)
        less "$diary"
        ;;
    last)
        tail -n 5 "$diary"
        ;;
    search)
        if [ -z "$2" ]; then
            echo "Usage: $0 search WORD"
            exit 1
        fi
        grep -i "$2" "$diary"
        ;;
    *)
        echo "Usage: $0 add | show | last | search WORD"
        exit 1
        ;;
esac
