from dataclasses import dataclass

@dataclass
class Uzenet:
    ora: int
    perc: int
    kuldo: str
    szoveg: str

MAX_TAROLT = 10

# 1. feladat
def F1(filename):
    uzenetek = []
    with open(filename, 'r', encoding='utf-8') as f:
        uzenet_szam = int(f.readline())
        for _ in range(uzenet_szam):
            ora, perc, kuldo = f.readline().split()
            szoveg = f.readline().rstrip()
            uzenetek.append(Uzenet(int(ora), int(perc), kuldo, szoveg))
    return uzenetek

# 2. feladat
def F2(uzenetek):
    index = MAX_TAROLT - 1 if len(uzenetek) > MAX_TAROLT else -1
    print(uzenetek[index].szoveg)

# 3. feladat
def F3(uzenetek):
    min_uzenet = min(uzenetek, key=lambda x: len(x.szoveg))
    max_uzenet = max(uzenetek, key=lambda x: len(x.szoveg))

    print('A legrövidebb üzenet:')
    print(min_uzenet.ora, min_uzenet.perc, min_uzenet.kuldo, min_uzenet.szoveg)
    print('A leghosszabb üzenet:')
    print(max_uzenet.ora, max_uzenet.perc, max_uzenet.kuldo, max_uzenet.szoveg)

# 4. feladat
def F4(uzenetek):
    counts = [0] * 5
    for uz in uzenetek:
        l = len(uz.szoveg)
        if l <= 20: counts[0] += 1
        elif l <= 40: counts[1] += 1
        elif l <= 60: counts[2] += 1
        elif l <= 80: counts[3] += 1
        else: counts[4] += 1

    ranges = [' 1- 20', '21- 40', '41- 60', '61- 80', '81-100']
    for r, c in zip(ranges, counts):
        print(f'{r}: {c:4} darab')

# 5. feladat
def F5(uzenetek):
    ora = [0] * 24
    for uz in uzenetek:
        ora[uz.ora] += 1

    kozpontban = sum(x - 10 for x in ora if x > 10)
    print('A kozpontban tarolt uzenetek szama:', kozpontban)

# 6. feladat
def F6(uzenetek):
    fontos_szam = '123456789'
    fontos_uzenetek = [uz for uz in uzenetek if uz.kuldo == fontos_szam]

    if len(fontos_uzenetek) < 2:
        print('Nincs elegendo uzenet')
        return

    leghosszabb = max(
        (fontos_uzenetek[i].ora * 60 + fontos_uzenetek[i].perc - fontos_uzenetek[i-1].ora * 60 - fontos_uzenetek[i-1].perc)
        for i in range(1, len(fontos_uzenetek))
    )

    print(f'A leghosszabb idő: {leghosszabb // 60} ora {leghosszabb % 60} perc')

# 7. feladat
def F7(uzenetek):
    ora = int(input('Ora: '))
    perc = int(input('Perc: '))
    kuldo = input('Kuldo: ')
    szoveg = input('Szoveg: ')
    uzenetek.append(Uzenet(ora, perc, kuldo, szoveg))

# 8. feladat
def F8(uzenetek, output='smski.txt'):
    uzenetek.sort(key=lambda x: x.kuldo)
    with open(output, 'w', encoding='utf-8') as f:
        aktszam = ''
        for uz in uzenetek:
            if uz.kuldo != aktszam:
                f.write(uz.kuldo + '\n')
                aktszam = uz.kuldo
            f.write(f'  {uz.ora} {uz.perc} {uz.szoveg}\n')

# Main
if __name__ == '__main__':
    print('1. feladat')
    uzenetek = F1('sms.txt')
    print('2. feladat')
    F2(uzenetek)
    print('3. feladat')
    F3(uzenetek)
    print('4. feladat')
    F4(uzenetek)
    print('5. feladat')
    F5(uzenetek)
    print('6. feladat')
    F6(uzenetek)
    print('7. feladat')
    F7(uzenetek)
    print('8. feladat')
    F8(uzenetek)