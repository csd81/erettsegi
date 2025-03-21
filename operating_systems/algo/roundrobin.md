### **Round Robin (RR) ütemezés lépésről lépésre**

A **Round Robin (RR)** ütemezés egy körbeforgó ütemezési algoritmus, ahol minden folyamat egy **időszelet** (time quantum) idejéig fut, majd ha nem fejezi be, akkor a következő folyamat következik. Az időszelet itt **3 ms**.

A következő táblázatot az adatok alapján hoztuk létre:

| Folyamat | Érkezési idő (T) | CPU-idő (C) |
|----------|------------------|-------------|
| P1       | 1                | 3           |
| P2       | 3                | 6           |
| P3       | 0                | 2           |
| P4       | 5                | 5           |

#### **1. lépés: Kiindulási táblázat**
A folyamatok az időszeletekhez rendelhetőek.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       |       |      |     |
| P2       | 3       | 6       |       |      |     |
| P3       | 0       | 2       |       |      |     |
| P4       | 5       | 5       |       |      |     |

#### **2. lépés: P3 indulása**
A **P3** folyamat érkezik először. Mivel a CPU-idője (2 ms) kisebb, mint az időszelet (3 ms), így teljesíthető. **P3** befejeződik 2 ms után.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       |       |      |     |
| P2       | 3       | 6       |       |      |     |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       |       |      |     |

#### **3. lépés: P1 indulása**
A **P1** folyamat következik. Mivel a CPU-idője (3 ms) megegyezik az időszelettel (3 ms), ezért 3 ms után befejeződik.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       | 2     | 5    | 1   |
| P2       | 3       | 6       |       |      |     |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       |       |      |     |

#### **4. lépés: P2 indulása**
A **P2** folyamat érkezik a 3. időpontban, de 5-ig kell várnia. Mivel a CPU-idője (6 ms) nagyobb, mint az időszelet (3 ms), a **P2** 3 ms-ot fut, majd félbeszakad.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       | 2     | 5    | 1   |
| P2       | 3       | 6       | 5     | 8    | 2   |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       |       |      |     |

#### **5. lépés: P4 indulása**
A **P4** folyamat érkezik 5-én. Mivel a CPU-idője (5 ms) nagyobb, mint az időszelet (3 ms), ezért 3 ms-ot fut, majd félbeszakad.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       | 2     | 5    | 1   |
| P2       | 3       | 6       | 5     | 8    | 2   |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       | 8     | 11   | 3   |

#### **6. lépés: P2 folytatása**
A **P2** folyamat most folytatódik, mivel a fennmaradó CPU-idője (3 ms) teljesíthető. 3 ms után befejeződik.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       | 2     | 5    | 1   |
| P2       | 3       | 6       | 5     | 8    | 2   |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       | 8     | 11   | 3   |

#### **7. lépés: P4 folytatása**
A **P4** folyamat folytatódik a fennmaradó 2 ms-os CPU-idővel, és befejeződik 16-ra.

| Folyamat | Érkezik | CPU-idő | Indul | Vége | Vár |
|----------|---------|---------|-------|------|-----|
| P1       | 1       | 3       | 2     | 5    | 1   |
| P2       | 3       | 6       | 5     | 8    | 2   |
| P3       | 0       | 2       | 0     | 2    | 0   |
| P4       | 5       | 5       | 8     | 11   | 3   |

### **Ütemezés:**

A végleges ütemezés (a folyamatok futásának sorrendje):

\[
\text{P3} \quad 🡪 \quad \text{P1} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P4} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P4}
\]

### **Összegzés**:
- Az **FCFS (First Come First Served)** ütemezésnél minden folyamat az érkezési sorrendben kapja meg a CPU-t.
- A **Round Robin (RR)** ütemezés körbeforgó módon osztja el az időt az egyes folyamatok között az időszelet segítségével.
  
Ha bármilyen kérdésed van a lépésekkel kapcsolatban, szívesen segítek! 😊