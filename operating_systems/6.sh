#!/bin/bash

# Kérjük be a fájl nevét
echo "Add meg a fájl nevét:"
read file

# Ellenőrizzük, hogy a fájl létezik-e
if [ -e "$file" ]; then
    # Ellenőrizzük, hogy a fájl üres-e
    if [ ! -s "$file" ]; then
        echo "A fájl üres."
    else
        echo "A fájl nem üres."
    fi
else
    echo "A fájl nem található."
fi
