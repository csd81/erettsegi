#!/bin/bash

# Kérjük be a fájl nevét és a célmappát
echo "Add meg a fájl nevét (teljes elérési úttal):"
read file
echo "Add meg a célmappát (teljes elérési úttal):"
read destination

# Ellenőrizzük, hogy a fájl létezik-e
if [ -f "$file" ]; then
    # Ellenőrizzük, hogy a célmappa létezik-e
    if [ -d "$destination" ]; then
        # Másolás a megadott mappába
        cp "$file" "$destination"
        echo "A fájl sikeresen másolva lett a $destination mappába."
    else
        echo "A megadott célmappa nem létezik!"
    fi
else
    echo "A megadott fájl nem létezik!"
fi
