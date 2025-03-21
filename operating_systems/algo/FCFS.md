### **Legrégebben várakozó (First Come First Served, FCFS) ütemezés**

A **First Come First Served (FCFS)** ütemezés az egyik legegyszerűbb algoritmus, ahol a folyamatokat a **beérkezési sorrend** szerint ütemezik, vagyis az elsőként érkező folyamatot hajtják végre először.

### **Adott adatok**:

- **Folyamatok**: P = (1, 2, 3, 4, 5)
- **Futási idők**: C = (1, 2, 6, 5, 3)
- **Érkezési idők**: T = (2, 4, 5, 0, 8)

### **1. lépés: Kiindulási táblázat**

Először is, készítünk egy táblázatot a **Folyamatok**, **Érkezés** és **CPU-idő** alapján:

| Folyamat | Érkezik (T) | CPU-idő (C) |
|----------|-------------|-------------|
| P1       | 2           | 1           |
| P2       | 4           | 2           |
| P3       | 5           | 6           |
| P4       | 0           | 5           |
| P5       | 8           | 3           |

### **2. lépés: Az algoritmus működése**

A FCFS algoritmus alapján az a folyamat lesz leghamarabb kiszolgálva, amelyik **legkorábban érkezett** meg a futásra kész állapotba. Az ütemezés sorrendjét az érkezési idő alapján határozzuk meg.

#### **Érkezési sorrend**:

1. **P4** érkezik először (T=0), így ő kerül elsőként végrehajtásra.
2. A következő a **P1** (T=2), mivel ő érkezett a második legkorábban.
3. Ezután **P2** következik (T=4).
4. **P3** jön következőként (T=5).
5. Végül **P5** érkezik (T=8), és ő lesz az utolsó.

### **3. lépés: Ütemezési sorrend**

A FCFS algoritmusban a folyamatokat érkezési sorrendben hajtjuk végre. Ezért a folyamatok ütemezése a következőképpen alakul:

\[
\text{P4} \quad 🡪 \quad \text{P1} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P5}
\]

### **4. lépés: Befejezési idő**

Most számoljuk ki minden folyamat befejezési idejét:

| Folyamat | Érkezik (T) | CPU-idő (C) | Kezdési idő | Befejezési idő |
|----------|-------------|-------------|-------------|----------------|
| P4       | 0           | 5           | 0           | 5              |
| P1       | 2           | 1           | 5           | 6              |
| P2       | 4           | 2           | 6           | 8              |
| P3       | 5           | 6           | 8           | 14             |
| P5       | 8           | 3           | 14          | 17             |

#### **Összegzés**:

- **P4** kezdődik 0-nál és befejeződik 5-nél.
- **P1** kezdődik 5-nél és befejeződik 6-nál.
- **P2** kezdődik 6-nál és befejeződik 8-nál.
- **P3** kezdődik 8-nál és befejeződik 14-nél.
- **P5** kezdődik 14-nél és befejeződik 17-nél.

### **Várakozási idő számítása**:

A várakozási idő a következő képlettel számolható:

\[
\text{Várakozási idő} = \text{Befejezési idő} - \text{Érkezési idő} - \text{CPU-idő}
\]

| Folyamat | Érkezik (T) | CPU-idő (C) | Befejezési idő | Várakozási idő |
|----------|-------------|-------------|----------------|----------------|
| P4       | 0           | 5           | 5              | 0              |
| P1       | 2           | 1           | 6              | 3              |
| P2       | 4           | 2           | 8              | 2              |
| P3       | 5           | 6           | 14             | 3              |
| P5       | 8           | 3           | 17             | 6              |

#### **Átlagos várakozási idő**:

\[
\text{Átlagos várakozási idő} = \frac{0 + 3 + 2 + 3 + 6}{5} = 2.8
\]

### **Összegzés**:

- A **FCFS** algoritmus működése alapján a **folyamatok ütemezése**:  
  \[
  \text{P4} \quad 🡪 \quad \text{P1} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P5}
  \]
- Az **átlagos várakozási idő**: 2.8 ms.

Ha további kérdéseid vannak vagy más példákat szeretnél látni, nyugodtan szólj! 😊