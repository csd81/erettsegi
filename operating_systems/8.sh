#!/bin/bash

# Kérjük be a két számot a felhasználótól
echo "Add meg az első számot:"
read num1
echo "Add meg a második számot:"
read num2

# Összeadjuk a két számot
sum=$((num1 + num2))

# Kiírjuk az eredményt a fájlba
echo "A két szám összege: $sum" > eredmeny.txt

# Értesítjük a felhasználót
echo "Az eredmény elmentve az eredmeny.txt fájlba."
