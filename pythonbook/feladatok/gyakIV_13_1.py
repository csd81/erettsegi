def hetnapja(honap,nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok",
"pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    return napnev[napsorszam]

print(hetnapja(1,8))
