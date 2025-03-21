#!/bin/bash

# Kérjük be a számot a felhasználótól
echo "Add meg a számot:"
read num

# Ellenőrizzük, hogy a szám páros vagy páratlan
if [ $((num % 2)) -eq 0 ]; then
    echo "A szám páros."
else
    echo "A szám páratlan."
fi
