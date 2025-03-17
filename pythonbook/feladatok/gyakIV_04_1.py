ado = float(input("Mennyi az adó? "))
h = float(input("Mennyi a hossz? "))
sz = float(input("Mennyi a szélesség? "))
if h <= 25 or sz <= 15:
    ado = 0.8 * ado
print ("A kedvezményes adó: ", ado)
