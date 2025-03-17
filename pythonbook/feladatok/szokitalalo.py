from tkinter import *
from random import randrange

def ujszo():
    global kitalalando, megjelenitendo, h, db
    szolista = ["DEBRECEN","BUDAPEST","EGER","SZEGED","MISKOLC"]
    vel = randrange(5)
    kitalalando = szolista[vel]
    megjelenitendo = ""
    db = 0
    h = len(kitalalando)
    for i in range(h):
        megjelenitendo += "X"
    textBox2.delete(0,END)
    textBox2.insert(0,megjelenitendo)

def betutkiertekel():
    global kitalalando, megjelenitendo, h, db
    tipp = textBox1.get()
    tipp = tipp.upper()
    elozo = megjelenitendo
    megjelenitendo=""
    for i in range(h):
        if tipp[0] == kitalalando[i]:
            megjelenitendo += tipp[0]
            db += 1
        else:
            megjelenitendo += elozo[i]
    textBox2.delete(0,END)
    textBox2.insert(0,megjelenitendo)
    textBox1.delete(0,END)
    if db == h:
        nyert()

def nyert():
    uzenetablak = Toplevel(ablak)
    uzenetablak.option_add("*font","Arial 11")
    uzenet = Message(uzenetablak, text="Ön nyert!!!", width=300)
    cmdButton4 = Button(uzenetablak, text="OK", \
        command=uzenetablak.destroy)
    uzenet.pack()
    cmdButton4.pack()
    uzenetablak.mainloop()

ablak = Tk()
ablak.option_add("*font","Arial 11")
for i in range(4):
    ablak.columnconfigure(i,pad = 15)
    ablak.rowconfigure(i,pad = 10)
label1 = Label(ablak,text="Tippelt betű: ")
label2 = Label(ablak,text="Kitalálandó szó: ")
textBox1 = Entry(ablak)
textBox2 = Entry(ablak)
cmdButton1 = Button(ablak,text="Új szó",width = 15, command=ujszo)
cmdButton2 = Button(ablak,text="Következő betű", \
    width = 15, command=betutkiertekel)
cmdButton3 = Button(ablak,text="Kilépés",width = 15, command=ablak.destroy)
label1.grid(row = 1, column = 1, sticky = E)
label2.grid(row = 2, column = 1, sticky = E)
textBox1.grid(row = 1, column = 2, sticky = W)
textBox2.grid(row = 2, column = 2, sticky = W)
cmdButton1.grid(row = 3, column = 1)
cmdButton2.grid(row = 3, column = 2)
cmdButton3.grid(row = 3, column = 3)
ablak.mainloop()
