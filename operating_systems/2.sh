#!/bin/bash

# Ellenőrizzük, hogy két argumentumot kaptunk
if [ $# -ne 2 ]; then
  echo "Kérlek, adj meg két számot a parancssori argumentumok között!"
  exit 1
fi

# Összeadjuk a két argumentumot
sum=$(($1 + $2))

# Kiírjuk az eredményt
echo "A két szám összege: $sum"
