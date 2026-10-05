#!/bin/bash
# Lesson 9, exercise 6: a short report about the server log
log=~/playground/logs/server.log
echo "Lines:    $(wc -l < $log)"
echo "Errors:   $(grep -c ERROR $log)"
echo "Warnings: $(grep -c WARNING $log)"
