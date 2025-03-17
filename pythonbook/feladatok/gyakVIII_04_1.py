from tkinter import *
import winsound

def kor(x, y, hely):
    global mezomeret, korr
    x1, y1 = x*mezomeret+2*korr, y*mezomeret+2*korr
    x2, y2 = (x+1)*mezomeret, (y+1)*mezomeret
    hely.create_rectangle(korr,korr, mezomeret+korr, \
        mezomeret+korr, width=2, fill="dark grey", outline="dark blue")
    hely.create_oval(x1,y1,x2,y2,width=2,fill="red",outline="black")

def iksz(x, y, hely):
    global mezomeret, korr
    x1, y1 = x*mezomeret+2.5*korr, y*mezomeret+2.5*korr
    x2, y2 = (x+1)*mezomeret-0.5*korr, (y+1)*mezomeret-0.5*korr
    hely.create_rectangle(korr,korr,mezomeret+korr, \
        mezomeret+korr, width=2, fill="dark grey", outline="dark blue")
    hely.create_line(x1,y1,x2,y2,width=4,fill="green")
    hely.create_line(x2,y1,x1,y2,width=4,fill="green")

def uj():
    global mezomeret, palyameret, korr, jatekos, palyatar, vege
    palyatar = {}
    vege = 0
    for i in range(mezoszam):
        for j in range(mezoszam):
            palyatar[(i,j)] = 0
    jatekos = 1
    for x in range(0, palyameret, mezomeret):
        for y in range(0, palyameret, mezomeret):
            x1, y1, x2, y2 = x+korr, y+korr, \
                x+mezomeret+korr, y+mezomeret+korr
            canPalya.create_rectangle(x1,y1,x2,y2, \
                width=2, fill="dark grey", outline="dark blue")     
    canNyert.create_rectangle(korr,korr,mezomeret+korr, \
            mezomeret+korr, width=2, fill="dark grey", outline="dark blue")
    kor(0,0,canKovetkezo)
    
def palyankattint(event): #bal egérgombbal kattintás eseménye
    global mezomeret, korr, jatekos, \
           palyatar, vege
    if vege == 0:
        x = int((event.x-korr)/mezomeret)
        y = int((event.y-korr)/mezomeret)
        if palyatar[(x,y)] == 0:
            palyatar[(x,y)] = jatekos
            if jatekos == 1:
                kor(x,y,canPalya)
            else:
                iksz(x,y,canPalya)
            if kiertekel(x,y) == 0:
                
                if jatekos == 1:
                    jatekos = 2
                    iksz(0, 0, canKovetkezo)
                else:
                    jatekos = 1
                    kor(0, 0, canKovetkezo)
            else:
                # rendszerhang lejátszás, ASYNC = hang miatt nem áll meg a program
                winsound.PlaySound("SystemAsterisk", winsound.SND_ASYNC)
                if jatekos == 1:
                    kor(0,0,canNyert)
                else:
                    iksz(0,0,canNyert)
                vege = 1
         
def kiertekel(x, y):
    global jatekos, palyatar, mezoszam
    db, xj = 0, x
    while db < 5 and xj < mezoszam and palyatar[(xj,y)]==jatekos:
        db, xj = db + 1, xj + 1
    xb = x - 1
    while db < 5 and xb >=0 and palyatar[(xb,y)]==jatekos:
        db, xb = db + 1, xb - 1
    if db != 5:
        db = 0
    yj = y
    while db < 5 and yj < mezoszam and palyatar[(x,yj)]==jatekos:
        db, yj = db + 1, yj + 1
    yb = y - 1
    while db < 5 and yb >=0 and palyatar[(x,yb)]==jatekos:
        db, yb = db + 1, yb - 1
    if db != 5:
        db = 0
    xj,yj = x,y
    while db < 5 and yj < mezoszam and xj < mezoszam and \
          palyatar[(xj,yj)]==jatekos:
        db, xj, yj = db + 1, xj + 1, yj + 1
    xb, yb = x - 1, y - 1
    while db < 5 and yb >=0 and xb >= 0 and \
          palyatar[(xb,yb)]==jatekos:
        db, xb, yb = db + 1, xb - 1, yb - 1
    if db != 5:
        db = 0
    xj,yj = x,y
    while db < 5 and yj < mezoszam and xj >=0 and \
          palyatar[(xj,yj)]==jatekos:
        db, xj, yj = db + 1, xj - 1, yj + 1
    xb, yb = x + 1, y - 1
    while db < 5 and yb <= mezoszam and xb >= 0 and \
          palyatar[(xb,yb)]==jatekos:
        db, xb, yb = db + 1, xb + 1, yb - 1     
    if db == 5:
        return 1
    else:
        return 0

mezoszam, mezomeret = 20, 30 
palyameret = mezoszam * mezomeret
korr = 4 # a mező korvonalának legyen helye
ablak = Tk()
ablak.title("Amóba")
ablak.option_add("*Font", "Arial 11")
lblNyert = Label(ablak, text="Nyertes:")
lblKovetkezo = Label(ablak, text="Következő játékos: ")
canNyert = Canvas(ablak, bg="dark grey", \
    height=mezomeret+korr, width=mezomeret+korr)
canKovetkezo = Canvas(ablak, bg="dark grey", \
    height=mezomeret+korr, width=mezomeret+korr)
cmdButton = Button(ablak, text="Új játék", command=uj, width=15)
canPalya = Canvas(ablak, bg="dark grey", \
    height=palyameret+korr, width=palyameret+korr)
canPalya.grid(row=1, column=1,rowspan=3, padx=15,pady=15)
lblKovetkezo.grid(row=1, column=2)
canKovetkezo.grid(row=1, column=3, padx=15)
lblNyert.grid(row=2, column=2, sticky=E)
canNyert.grid(row=2, column=3, padx=15)
cmdButton.grid(row=3, column=2, padx=15, columnspan=2)
canPalya.bind("<Button-1>", palyankattint) #bal egérgombra érzékeny rajzterület
uj()
ablak.mainloop()
