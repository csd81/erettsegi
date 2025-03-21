#!/bin/bash

# Kérjük be a könyvtár nevét
echo "Add meg a könyvtár nevét:"
read directory

# Ellenőrizzük, hogy a megadott könyvtár létezik-e
if [ -d "$directory" ]; then
    echo "A könyvtár tartalma:"
    # Listázzuk a könyvtárban található fájlokat és alkönyvtárakat
    ls "$directory"
else
    echo "A megadott könyvtár nem létezik!"
fi
