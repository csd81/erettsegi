### **II/3. Prioritásos ütemezés (Priority Scheduling)**

A **Prioritásos ütemezés (Priority Scheduling)** egy olyan ütemezési algoritmus, amely figyelembe veszi a folyamatok prioritását. A legnagyobb prioritású folyamatokat hajtja végre először, és a rendszer végrehajtja őket azelőtt, hogy a kisebb prioritásúak kerüljenek sorra.

A prioritásos ütemezésnél:
- **Alacsonyabb prioritás** = **Nagyobb prioritás** (a kisebb számú prioritás jelenti a magasabb fontosságot).

### **Adott adatok:**

- **Folyamatok**: P = (1, 2, 3, 4, 5)
- **Futási idők (C)**: C = (3, 6, 2, 1, 3)
- **Prioritások (Prioritas)**: Prioritas = (5, 4, 2, 3, 1)
- **Minden folyamat T=0 időpontban kerül futásra kész állapotba.**

### **1. lépés: Kiindulási táblázat**

Először is, készítünk egy táblázatot a **Folyamatok**, **CPU-idő**, és **Prioritás** alapján:

| Folyamat | CPU-idő (C) | Prioritás (Prioritas) |
|----------|-------------|-----------------------|
| P1       | 3           | 5                     |
| P2       | 6           | 4                     |
| P3       | 2           | 2                     |
| P4       | 1           | 3                     |
| P5       | 3           | 1                     |

### **2. lépés: Prioritási sorrend**

Mivel minden folyamat T=0 időpontban futásra kész állapotba kerül, az ütemezésnél a **prioritás értéke** a mérvadó. Minél kisebb a prioritás száma, annál magasabb a folyamat prioritása, tehát azt előbb hajtjuk végre.

Prioritási sorrend:
1. **P5** (Prioritás = 1)
2. **P3** (Prioritás = 2)
3. **P4** (Prioritás = 3)
4. **P2** (Prioritás = 4)
5. **P1** (Prioritás = 5)

### **3. lépés: Ütemezési sorrend**

A prioritásos algoritmus alapján a folyamatokat a következő sorrendben hajtjuk végre:

\[
\text{P5} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P4} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P1}
\]

### **4. lépés: Befejezési idő számítása**

A befejezési idő meghatározásához összesítjük a futási időket az ütemezési sorrend alapján.

| Folyamat | CPU-idő (C) | Kezdési idő | Befejezési idő |
|----------|-------------|-------------|----------------|
| P5       | 3           | 0           | 3              |
| P3       | 2           | 3           | 5              |
| P4       | 1           | 5           | 6              |
| P2       | 6           | 6           | 12             |
| P1       | 3           | 12          | 15             |

### **5. lépés: Várakozási idő számítása**

A várakozási időt a következő képlettel számoljuk:

\[
\text{Várakozási idő} = \text{Befejezési idő} - \text{Érkezési idő} - \text{CPU-idő}
\]

| Folyamat | Érkezési idő (T) | CPU-idő (C) | Befejezési idő | Várakozási idő |
|----------|------------------|-------------|----------------|----------------|
| P5       | 0                | 3           | 3              | 0              |
| P3       | 0                | 2           | 5              | 3              |
| P4       | 0                | 1           | 6              | 5              |
| P2       | 0                | 6           | 12             | 6              |
| P1       | 0                | 3           | 15             | 12             |

### **6. lépés: Átlagos várakozási idő**

Az átlagos várakozási időt az alábbi képlettel számoljuk ki:

\[
\text{Átlagos várakozási idő} = \frac{0 + 3 + 5 + 6 + 12}{5} = 5.2
\]

### **Összegzés**:

- Az ütemezési sorrend:  
  \[
  \text{P5} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P4} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P1}
  \]
- Az **átlagos várakozási idő**: 5.2 ms.

Ez az ütemezés a prioritásos algoritmus alapján történik, ahol a legkisebb prioritású folyamatokat hajtják végre először.

Ha kérdéseid vannak, vagy további részletekre van szükséged, szívesen segítek! 😊