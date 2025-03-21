### **Biztonságos sorozat keresés (Bankár algoritmus)**

A **Bankár algoritmus** célja, hogy meghatározza, van-e biztonságos sorozat egy rendszerben, vagyis olyan folyamatok sorrendjét, amelyek végrehajthatók a rendelkezésre álló erőforrások alapján. A következő lépéseken keresztül megnézhetjük, hogy a rendszer biztonságos-e, és ha igen, meghatározhatjuk a biztonságos sorozatot.

#### **Adott információk**:

- **Rendelkezésre álló erőforrások**: 10 (1 erőforrás osztály)
- **Folyamatok foglalása (F)**: 
  - P1: 3
  - P2: 2
  - P3: 2
- **Folyamatok maximális igénye (M)**:
  - P1: 9
  - P2: 4
  - P3: 7
- **Szabad erőforrások (Szabad)**: 3

#### **1. lépés: Kiindulási táblázat elkészítése**

Először is, készítünk egy táblázatot a **Foglal**, **Max**, **Még** és **Szabad** oszlopokkal:

| Folyamat | Foglal | Max | Még (Max - Foglal) |
|----------|--------|-----|--------------------|
| P1       | 3      | 9   | 6                  |
| P2       | 2      | 4   | 2                  |
| P3       | 2      | 7   | 5                  |
| **Szabad** |        |     | 3                  |

#### **2. lépés: A P2 folyamat kiválasztása**

Mivel a **Szabad** erőforrások (A: 3) elegendőek a **P2** erőforrás igényének (A: 2), a **P2** folyamatot válasszuk.

Frissítjük a táblázatot:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | 3      | 9   | 6   |        |
| P2       | 4      | 4   | 0   |        |
| P3       | 2      | 7   | 5   |        |
| Szabad   |        |     |     | 1      |

#### **3. lépés: A P2 folyamat végrehajtása és erőforrások visszaadása**

Miután **P2** befejeződött, visszaadja az általa foglalt erőforrásokat. Így a **Szabad** erőforrások száma növekszik:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | 3      | 9   | 6   |        |
| P2       | -      | -   | -   |        |
| P3       | 2      | 7   | 5   |        |
| Szabad   |        |     |     | 5      |

#### **4. lépés: A P3 folyamat kiválasztása**

A **Szabad** erőforrások (A: 5) elegendőek a **P3** igényének (A: 2), tehát most a **P3** folyamatot válasszuk.

Frissítjük a táblázatot:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | 3      | 9   | 6   |        |
| P2       | -      | -   | -   |        |
| P3       | 7      | 7   | 0   |        |
| Szabad   |        |     |     | 0      |

#### **5. lépés: A P3 folyamat végrehajtása és erőforrások visszaadása**

Miután **P3** befejeződött, visszaadja az általa foglalt erőforrásokat, így a **Szabad** erőforrások száma ismét nő:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | 3      | 9   | 6   |        |
| P2       | -      | -   | -   |        |
| P3       | -      | -   | -   |        |
| Szabad   |        |     |     | 7      |

#### **6. lépés: A P1 folyamat kiválasztása**

Mivel a **Szabad** erőforrások (A: 7) elegendőek a **P1** igényének (A: 6), a **P1** folyamatot válasszuk.

Frissítjük a táblázatot:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | 9      | 9   | 0   |        |
| P2       | -      | -   | -   |        |
| P3       | -      | -   | -   |        |
| Szabad   |        |     |     | 1      |

#### **7. lépés: A P1 folyamat végrehajtása és erőforrások visszaadása**

Miután **P1** befejeződött, visszaadja az általa foglalt erőforrást, így a **Szabad** erőforrások ismét növekednek:

| Folyamat | Foglal | Max | Még | Szabad |
|----------|--------|-----|-----|--------|
| P1       | -      | -   | -   |        |
| P2       | -      | -   | -   |        |
| P3       | -      | -   | -   |        |
| Szabad   |        |     |     | 10     |

### **Biztonságos sorozat**:

Mivel minden folyamat végrehajtható és sikerült a szükséges erőforrásokat biztosítani, a **biztonságos sorozat**:

\[
\text{P2} \quad 🡪 \quad \text{P3} \quad 🡪 \quad \text{P1}
\]

### **Összegzés**:
A rendszer **biztonságos**, és a folyamatok biztonságos végrehajtási sorrendje: **P2 → P3 → P1**. Minden folyamat sikeresen lefutott a rendelkezésre álló erőforrásokkal anélkül, hogy holtpontba került volna a rendszer.

Ha kérdésed van, vagy további részletekre van szükséged, szívesen segítek! 😊