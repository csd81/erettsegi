### Bevezetés a számítógépes hálózatokhoz

A számítógépes hálózatok az információs társadalom alapvető infrastruktúráját képezik. Segítségükkel az eszközök közötti kommunikáció, adatok megosztása és távoli elérés biztosítható. A modern hálózatok fejlődése az elmúlt évtizedekben forradalmasította az üzleti életet, az oktatást, a tudományos kutatást és a hétköznapi felhasználást.

---

## **Alapfogalmak tisztázása**

### **Hálózat definíciója**
A számítógépes hálózat olyan összekapcsolt eszközök rendszere, amely lehetővé teszi az adatok és erőforrások megosztását. A hálózatokat különböző eszközök (pl. számítógépek, szerverek, nyomtatók) és kommunikációs csatornák (pl. vezetékes vagy vezeték nélküli kapcsolatok) alkotják.

### **Hálózati típusok: LAN, WAN, Internet**
- **LAN (Local Area Network, helyi hálózat)**: Egy épületen vagy kisebb területen belüli hálózat, például irodákban vagy iskolákban. Jellemzően nagy sebességű kapcsolatokat használ (pl. Ethernet).
- **WAN (Wide Area Network, kiterjedt hálózat)**: Nagy földrajzi területet lefedő hálózat, amely több LAN-t köt össze. Az internet is egy globális WAN.
- **Internet**: A világ legnagyobb számítógépes hálózata, amely TCP/IP protokollkészletet használ az eszközök összekapcsolására és kommunikációjára.

### **Protokollok**
A protokollok olyan szabályrendszerek, amelyek meghatározzák az adatok továbbításának módját a hálózaton belül. Fontosabb protokollok:
- **TCP/IP (Transmission Control Protocol / Internet Protocol)**: Az internet és számos belső hálózat alapvető protokollkészlete.
- **HTTP/HTTPS (HyperText Transfer Protocol / Secure HTTP)**: A weboldalak betöltésére szolgál.
- **FTP (File Transfer Protocol)**: Fájlok átvitelére használatos.
- **DNS (Domain Name System)**: A domainneveket IP-címekké alakítja.

### **Sávszélesség és átviteli sebesség**
A sávszélesség azt jelenti, hogy egy adott hálózat milyen mennyiségű adatot képes továbbítani adott idő alatt. Mértékegysége a bit/s (bit per másodperc), például Mbps (megabit per másodperc) vagy Gbps (gigabit per másodperc). A nagyobb sávszélesség gyorsabb adatátvitelt eredményez.

---

## **A számítógépes hálózatok fejlődése és szerepe**
A számítógépes hálózatok az 1960-as években jelentek meg az ARPANET kialakulásával, amely az internet elődjének tekinthető. Az évtizedek során a hálózatok gyors fejlődésen mentek keresztül:
1. **Kezdeti hálózatok (1960-1980)**: Az első számítógépes hálózatokat kutatási célokra fejlesztették ki.
2. **Hálózatok elterjedése (1980-1990)**: A LAN-ok elérhetővé váltak az üzleti és egyetemi szférában.
3. **Internethálózat (1990-2000)**: A világháló (World Wide Web) és az e-mail széles körben elterjedt.
4. **Modern hálózatok (2000-napjainkig)**: A vezeték nélküli hálózatok, a felhőalapú szolgáltatások és az 5G technológia fejlődése.

Napjainkban a hálózatok elengedhetetlenek az üzleti életben, az egészségügyben, az oktatásban és a szórakoztatásban.

---

## **Hálózati eszközök és funkcióik**

A hálózatok hatékony működéséhez különféle eszközök szükségesek. Ezek biztosítják az adatforgalmat és az eszközök közötti kapcsolatot.

- **Router (Forgalomirányító)**: Az eszközök közötti adatirányítást végzi, és különböző hálózatok összekapcsolását teszi lehetővé.
- **Switch (Kapcsoló)**: Az egy hálózaton belüli eszközök közötti adatkapcsolatot irányítja, hatékonyabb és gyorsabb, mint a hub.
- **Hub**: Egy egyszerűbb eszköz, amely minden beérkező adatot továbbít minden csatlakoztatott eszköz felé (kevésbé hatékony, mint a switch).
- **Szerverek**: Központi számítógépek, amelyek szolgáltatásokat nyújtanak (pl. fájlszerver, webkiszolgáló).

---

## **Labor: Hálózati infrastruktúra és Packet Tracer használata**

### **Cisco IOS alapvető parancsai**
A Cisco eszközök konfigurálásához a **Cisco IOS** operációs rendszert használják, amely parancssori felületen keresztül kezelhető. Fontosabb parancsok:
- **show ip interface brief** – Megmutatja az interfészek állapotát.
- **ping [IP-cím]** – Ellenőrzi az eszközök közötti kapcsolatot.
- **enable** – Adminisztrátori módba lépés.
- **configure terminal** – Konfigurációs mód megnyitása.
- **interface [interfész neve]** – Hálózati interfész konfigurálása.

### **Egyszerű kétgépes hálózat összeállítása Packet Tracerben**
A **Cisco Packet Tracer** egy hálózatszimulációs eszköz, amely lehetővé teszi hálózatok tervezését és tesztelését. Egy alapvető kétgépes hálózat beállítása a következő lépésekből áll:

1. **Két PC hozzáadása a Packet Tracerben.**
2. **Egy egyenes UTP kábel használata a közvetlen összeköttetéshez.**
3. **IP-címek beállítása a PC-k számára (pl. PC1: 192.168.1.1, PC2: 192.168.1.2).**
4. **Ping teszt végrehajtása a hálózati kapcsolat ellenőrzésére.**

**Parancs a kapcsolat ellenőrzésére**:
```sh
ping 192.168.1.2
```
Ha a konfiguráció helyes, a PC1 sikeresen eléri a PC2-t.

---

## **Összegzés**
A számítógépes hálózatok lehetővé teszik az eszközök közötti kommunikációt, erőforrások megosztását és az internet elérését. Az alapfogalmak tisztázása és a hálózati eszközök ismerete nélkülözhetetlen a modern IT környezetben. A laboratóriumi gyakorlatok során a hálózati infrastruktúra és a Cisco Packet Tracer használata révén a gyakorlati ismeretek is elsajátíthatók.