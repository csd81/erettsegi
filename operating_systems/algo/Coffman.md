### **Coffman algoritmus: Holtpont ellenőrzése és biztonságos sorozat keresése**

A **Coffman algoritmus** segítségével ellenőrizhetjük, hogy a rendszer holtpont-mentes-e, vagyis van-e biztonságos sorozat, amelyben a folyamatok végrehajtásához szükséges erőforrásokat biztosítani tudjuk. A lépéseken végighaladva a következő eredményeket kapjuk.

#### **Adott információk**:

- **Erőforrás osztályok**: A, B, C
- **Rendelkezésre álló erőforrások**: 10 (összesen)
  
| Folyamat | Foglalás (F) | Kérés (Max - Foglalás) |
|----------|--------------|------------------------|
| P1       | (1, 4, 0)    | (8, 0, 5)              |
| P2       | (5, 1, 3)    | (2, 0, 2)              |
| P3       | (1, 0, 3)    | (0, 2, 0)              |
| P4       | (2, 4, 1)    | (4, 0, 0)              |

### **1. lépés: Kiindulási táblázat**

A következő táblázatot hoztuk létre a foglalt és maximális igények alapján:

| Folyamat | Foglal (F) | Max | Még (Max - Foglal) | Szabad (összesen) |
|----------|------------|-----|--------------------|-------------------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 3                 |
| P2       | (5, 1, 3)  | (4, 1, 2) | (2, 0, 2) |                   |
| P3       | (1, 0, 3)  | (7, 2, 0) | (6, 2, 0) |                   |
| P4       | (2, 4, 1)  | (4, 0, 0) | (2, 0, 0) |                   |

### **2. lépés: P4 folyamat kiválasztása**

Az erőforrások rendelkezésre állása alapján a **P4** folyamat erőforrásigénye teljesíthető:

- P4 igényelt erőforrásai: (A: 4, B: 0, C: 0) 
- Szabad erőforrások: (A: 5, B: 1, C: 0)

P4 elindul, és az általa foglalt erőforrásokat frissítjük:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 3      |
| P2       | (5, 1, 3)  | (4, 1, 2) | (2, 0, 2) |        |
| P3       | (1, 0, 3)  | (7, 2, 0) | (6, 2, 0) |        |
| P4       | (6, 4, 1)  | (4, 0, 0) | (2, 0, 0) | 1      |

### **3. lépés: P4 erőforrásainak visszaadása**

P4 befejeződött és visszaadja az erőforrásokat:

- Szabad erőforrások frissítése:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 5      |
| P2       | (5, 1, 3)  | (4, 1, 2) | (2, 0, 2) |        |
| P3       | (1, 0, 3)  | (7, 2, 0) | (6, 2, 0) |        |
| P4       | -          | -   | -   | 7      |

### **4. lépés: P3 folyamat kiválasztása**

A **P3** igénye (A: 0, B: 2, C: 0) most teljesíthető a szabad erőforrásokkal (A: 5, B: 1, C: 0). Elindítjuk:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 5      |
| P2       | (5, 1, 3)  | (4, 1, 2) | (2, 0, 2) |        |
| P3       | (7, 2, 3)  | (7, 2, 0) | (0, 0, 0) | 3      |
| P4       | -          | -   | -   |        |

### **5. lépés: P3 erőforrásainak visszaadása**

P3 befejeződött és visszaadja az erőforrásokat:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 8      |
| P2       | (5, 1, 3)  | (4, 1, 2) | (2, 0, 2) |        |
| P3       | -          | -   | -   | 7      |
| P4       | -          | -   | -   |        |

### **6. lépés: P2 folyamat kiválasztása**

A **P2** igénye (A: 2, B: 0, C: 2) most teljesíthető a szabad erőforrásokkal (A: 8, B: 4, C: 5). Elindítjuk:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 7      |
| P2       | (7, 1, 5)  | (4, 1, 2) | (0, 0, 0) | 4      |
| P3       | -          | -   | -   |        |
| P4       | -          | -   | -   |        |

### **7. lépés: P2 erőforrásainak visszaadása**

P2 befejeződött és visszaadja az erőforrásokat:

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (1, 4, 0)  | (9, 4, 7) | (8, 0, 5) | 10     |
| P2       | -          | -   | -   |        |
| P3       | -          | -   | -   |        |
| P4       | -          | -   | -   |        |

### **8. lépés: P1 folyamat kiválasztása**

A **P1** igénye (A: 0, B: 0, C: 5) most teljesíthető a szabad erőforrásokkal (A: 10, B: 4, C: 5). Elindítjuk.

| Folyamat | Foglal (F) | Max | Még | Szabad |
|----------|------------|-----|-----|--------|
| P1       | (9, 4, 5)  | (9, 4, 7) | (0, 0, 2) | 10     |
| P2       | -          | -   | -   |        |
| P3       | -          | -   | -   |        |
| P4       | -          | -   | -   |        |

### **Biztonságos sorozat**:

Miután minden folyamat igénye teljesíthető volt, a biztonságos sorozat a következő:

 
\text{P4} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P2} \quad 🡪 \quad \text{P1}
 

### **Összegzés**:

A rendszer **biztonságos**, és a folyamatok végrehajtási sorrendje a következő:

 
P4 \quad 🡪 \quad P3 \quad 🡪 \quad P2 \quad 🡪 \quad P1
 