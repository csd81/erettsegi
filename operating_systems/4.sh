#!/bin/bash

# Kérjük be a két számot a felhasználótól
echo "Add meg az első számot:"
read num1
echo "Add meg a második számot:"
read num2

# Ellenőrizzük, hogy melyik szám a nagyobb, vagy ha egyenlőek
if [ "$num1" -gt "$num2" ]; then
    echo "Az első szám ($num1) nagyobb, mint a második szám ($num2)."
elif [ "$num1" -lt "$num2" ]; then
    echo "A második szám ($num2) nagyobb, mint az első szám ($num1)."
else
    echo "A két szám egyenlő ($num1 == $num2)."
fi
