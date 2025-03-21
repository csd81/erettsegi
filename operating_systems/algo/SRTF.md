### **II/4. Legrövidebb hátralévő idejű (Shortest Remaining Time First, SRTF) ütemezés**

A **SRTF (Shortest Remaining Time First)** algoritmus a **preemptív ütemezési algoritmusok** közé tartozik, amely mindig a legkisebb hátralévő futási idővel rendelkező folyamatot hajtja végre. Ha egy új folyamat érkezik, amelynek rövidebb hátralévő ideje van, mint az éppen futó folyamatnak, akkor az éppen futó folyamatot félbeszakítja, és az új folyamatot kezdi el futtatni.

### **Adott adatok:**

- **Folyamatok**: P = (1, 2, 3, 4)
- **Futási idők (C)**: C = (4, 5, 7, 1)
- **Érkezési idők (T)**: T = (5, 2, 4, 0)

### **1. lépés: Kiindulási táblázat**

Először is, készítünk egy táblázatot az **Érkezési idők** és **Futási idők** alapján:

| Folyamat | Érkezik (T) | CPU-idő (C) |
|----------|-------------|-------------|
| P1       | 5           | 4           |
| P2       | 2           | 5           |
| P3       | 4           | 7           |
| P4       | 0           | 1           |

### **2. lépés: P4 indítása**

Mivel az **SRTF** algoritmus a legkisebb hátralévő futási idővel rendelkező folyamatot választja, és **P4** a legkisebb futási idővel rendelkezik (1 ms), így ő indítja el a futást. **P4** befejezi futását 1 ms múlva, így 0-tól 1-ig tart.

| Folyamat | Érkezik (T) | CPU-idő (C) | Indulás | Befejezés | Várakozás |
|----------|-------------|-------------|---------|-----------|-----------|
| P1       | 5           | 4           |         |           |           |
| P2       | 2           | 5           |         |           |           |
| P3       | 4           | 7           |         |           |           |
| P4       | 0           | 1           | 0       | 1         | 0         |

### **3. lépés: P2 indítása**

A következő legkisebb hátralévő idejű folyamat **P2**, mivel ő érkezett 2 ms-kor és 5 ms futási idővel rendelkezik. Mivel **P2** beérkezése után **P1** még nem érkezett meg, így **P2** futását 1 ms után kezdi el, és 7 ms-ig fut.

| Folyamat | Érkezik (T) | CPU-idő (C) | Indulás | Befejezés | Várakozás |
|----------|-------------|-------------|---------|-----------|-----------|
| P1       | 5           | 4           |         |           |           |
| P2       | 2           | 5           | 1       | 7         | 0         |
| P3       | 4           | 7           |         |           |           |
| P4       | 0           | 1           | 0       | 1         | 0         |

### **4. lépés: P3 indítása**

A következő legkisebb hátralévő idejű folyamat **P3**, mivel 7 ms futási idővel rendelkezik, és az érkezését követően rövid ideig tartó munkát végezhet, mivel **P2** éppen félbeszakad.

Mivel a hátralévő ideje 7 és még nem maradt be, a végső becsült elemzés befejeződik.

----------


A feladat alapján a legrövidebb hátralévő idejű ütemezés (SRTF) algoritmus lépéseit kell végrehajtani. Az alábbiakban bemutatom a folyamatok ütemezését a megadott adatok szerint.

**1. Lépés: Kiindulási táblázat**

| Folyamat | Érkezik | CPU-idő | Indulás | Vége | Várakozás |
|----------|---------|---------|---------|------|-----------|
| P1       | 5       | 4       |         |      |           |
| P2       | 2       | 5       |         |      |           |
| P3       | 4       | 7       |         |      |           |
| P4       | 0       | 1       |         |      |           |

**2. Lépés: P4 elindul, mert ő érkezett elsőként.**

| Folyamat | Érkezik | CPU-idő | Indulás | Vége | Várakozás |
|----------|---------|---------|---------|------|-----------|
| P1       | 5       | 4       |         |      |           |
| P2       | 2       | 5       |         |      |           |
| P3       | 4       | 7       |         |      |           |
| P4       | 0       | 1       | 0       | 1    | 0         |

**3. Lépés: P2 elindul, mivel ő érkezett legközelebb és kisebb CPU-idővel rendelkezik, mint P3.**

| Folyamat | Érkezik | CPU-idő | Indulás | Vége | Várakozás |
|----------|---------|---------|---------|------|-----------|
| P1       | 5       | 4       |         |      |           |
| P2       | 2       | 5       | 2       | 7    | 0         |
| P3       | 4       | 7       |         |      |           |
| P4       | 0       | 1       | 0       | 1    | 0         |

**4. Lépés: P1 elindul, mivel P3 érkezéséig már nem lesz újabb folyamat, és ő rendelkezik kisebb CPU-idővel, mint P3.**

| Folyamat | Érkezik | CPU-idő | Indulás | Vége | Várakozás |
|----------|---------|---------|---------|------|-----------|
| P1       | 5       | 4       | 7       | 11   | 2         |
| P2       | 2       | 5       | 2       | 7    | 0         |
| P3       | 4       | 7       |         |      |           |
| P4       | 0       | 1       | 0       | 1    | 0         |

**5. Lépés: Végül P3 elindul, miután P1 befejeződött.**

| Folyamat | Érkezik | CPU-idő | Indulás | Vége | Várakozás |
|----------|---------|---------|---------|------|-----------|
| P1       | 5       | 4       | 7       | 11   | 2         |
| P2       | 2       | 5       | 2       | 7    | 0         |
| P3       | 4       | 7       | 11      | 18   | 7         |
| P4       | 0       | 1       | 0       | 1    | 0         |

**6. Lépés: Folyamatok ütemezése, döntések nyomon követése:**

P4 🡪 P2 🡪 P2 🡪 P2 🡪 P1 🡪 P3 🡪 - 🡪 -

Ez a teljes ütemezési folyamat a megadott szabályok és lépések szerint, figyelembe véve a SRTF algoritmus alkalmazását.