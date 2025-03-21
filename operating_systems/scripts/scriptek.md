### **Összefoglaló: OS. Gyakorlati 4**

---

#### **Bash Script Futtatása, Változók, Kiíratás, Argumentumok, Elágazások**

1. **Bash script futtatása:**
   - **Shell script**-et egyszerű szöveges fájlként hozunk létre, és **`chmod`** segítségével futtathatóvá tesszük.
   - **Létrehozás és futtatás lépései**:
     1. `nano helloworld.sh`
     2. `#!/bin/bash` (kötelező első sor)
     3. `echo "Hello World"`
     4. `chmod u+x helloworld.sh`
     5. `./helloworld.sh` (relatív vagy abszolút útvonal)

2. **Változók:**
   - A változók típustalanok, bármit tárolhatnak, szöveget és számot egyaránt.
   - **Értékadás**: 
     ```bash
     numbers=10
     salary=$numbers
     text=hello
     longtext="A fizetesem $salary alma"
     ```

3. **Kiíratás:**
   - **`echo`** parancs a változók tartalmának kiíratására.
   - Példák:
     ```bash
     echo "$salary"   # Kiíratja: 10
     echo "$longtext" # Kiíratja: A fizetesem 10 alma
     echo '$longtext' # Kiíratja: A fizetesem $salary alma
     ```

4. **Változónév elkülönítés:**
   - **`${}`** a változónév elválasztására:
     ```bash
     echo "${hello}world" # Hellóworld
     ```

---

#### **Parancssori Argumentumok**

- A parancssori argumentumok az `$1`, `$2` stb. változókban tárolódnak.
- **Példák**:
  ```bash
  ./elso.sh arg1 arg2
  ```

  ```bash
  # Argumentumok használata a szkriptekben:
  # 1. Kiíratás
  echo "$1 $2!"
  
  # 2. Fájlba írás:
  echo "$1" > "$2"
  
  # 3. Fájl másolása:
  cp "$1" "$2"
  ```

---

#### **Szöveg Bekérése**

- **`read`** parancs segítségével szöveget kérhetünk be a felhasználótól:
  ```bash
  read name
  ```

- **Példa (login.sh)**: Jelszó bekérés:
  ```bash
  #!/bin/bash
  echo "Kerem, adja meg a nevet:"
  read name
  echo "Kerem, adja meg a jelszavat:"
  read -s password
  echo "Kedves ${name}, most már belephet!"
  ```

---

#### **Elágazás (if)**

- Az **`if`** utasítással elágazásokat végezhetünk.
  - **Egyszerű if**:
    ```bash
    if test -e ~/dokumentumok/sorok.txt
    then
        echo "Van ilyen fájl"
    else
        echo "Nincs ilyen fájl"
    fi
    ```

  - **Többszörös elágazás (if-else if)**:
    ```bash
    if [ "$a" -gt "$b" ]; then
        echo "Az első szám a nagyobb."
    elif [ "$a" -eq "$b" ]; then
        echo "A két szám egyenlő."
    else
        echo "A második szám a nagyobb."
    fi
    ```

  - **`test` utasítás**: fájlok, könyvtárak létezésének, vagy a fájlok méretének ellenőrzésére:
    ```bash
    test -e ~/dokumentumok/sorok.txt
    ```

---

#### **Egész Számok Összehasonlítása**

- **Összehasonlító operátorok**:
  ```bash
  -eq  # egyenlő
  -ne  # nem egyenlő
  -gt  # nagyobb
  -ge  # nagyobb vagy egyenlő
  -lt  # kisebb
  -le  # kisebb vagy egyenlő
  ```

  - **Példa:**
    ```bash
    if [ "$a" -gt "$b" ]; then
        echo "$a nagyobb, mint $b"
    fi
    ```

---

#### **Szövegek (String) Összehasonlítása**

- **`==`**: Egyenlőség ellenőrzése.
- **`!=`**: Nem egyenlőség ellenőrzése.
  - **Példa:**
    ```bash
    if [ "$a" != "$b" ]; then
        echo "$a nem egyenlő $b-val"
    fi
    ```

- **Mintaillesztés (`[[ $a == z* ]]`)**: Ha `$a` "z"-vel kezdődik.
  ```bash
  if [[ $a == z* ]]; then
      echo "$a kezdődik z-vel"
  fi
  ```

---

#### **Többszörös Elágazás (case)**

- **`case`**: Több lehetséges mintát ellenőrizhetünk egy változóval:
  ```bash
  case $number in
    1)
        echo "Elso szamot valasztotta."
        ;;
    2)
        echo "Masodik szamot valasztotta."
        ;;
    *)
        echo "Hibas szamot valasztott."
        ;;
  esac
  ```

---

#### **`expr` és Aritmetikai Műveletek**

- **`expr`** parancs az aritmetikai kifejezések értékelésére:
  ```bash
  sum=$(expr 5 + 3)
  difference=$(expr 10 - 4)
  product=$(expr 4 \* 6)
  quotient=$(expr 24 / 4)
  remainder=$(expr 27 % 5)
  ```

- **`$(( ... ))`**: C-szintaxisban az aritmetikai műveletek végrehajtása:
  ```bash
  sum=$((5 + 3))
  difference=$((10 - 4))
  ```

- **Példa:**
  ```bash
  #!/bin/bash
  a=5
  b=3
  c=$(expr $a + $b)
  echo "Az eredmény: $c"
  ```

---

Ez a **gyakorlati összefoglaló** segít a legfontosabb Bash parancsok és szkript írási alapelvek megértésében és alkalmazásában. Ha kérdésed van, vagy szeretnél további részleteket, kérlek jelezd! 😊