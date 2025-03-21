#!/bin/bash

# Kérjük be a számot a felhasználótól
echo "Add meg a számot:"
read num

# Ellenőrizzük, hogy a szám pozitív, negatív vagy nulla
if [ "$num" -gt 0 ]; then
    echo "A szám pozitív."
elif [ "$num" -lt 0 ]; then
    echo "A szám negatív."
else
    echo "A szám nulla."
fi
