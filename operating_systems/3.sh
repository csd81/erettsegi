#!/bin/bash

# Kérjük be a felhasználótól a fájlnevet
echo "Add meg a fájl nevét:"
read filename

# Ellenőrizzük, hogy a fájl létezik-e a dokumentumok mappában
if [ -e ~/dokumentumok/$filename ]; then
    echo "A fájl létezik."
else
    echo "A fájl nem létezik."
fi
