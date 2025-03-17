from tkinter import * 
from random import randrange 

def indulj():
    global foto1, item1, ablak, vege, vel
    if vege == 0:
        vel = randrange(3)
        fajlnev =  str(vel) + ".png"
        foto1 = PhotoImage(file=fajlnev)
        item1 = vaszon1.create_image(155,155, image=foto1) #155 kép középponja
        ablak.after(100,indulj) #100 ms szünet után hívja az indulj-t
    
def listabeallit():
    global lista, foto2, item2, kivalasztott
    kiv = lista.curselection() #kiválasztott listaelem indexei
    kivalasztott = kiv[0] #az első kiválasztot index
    fajlnev =  str(kivalasztott) + ".png"
    foto2 = PhotoImage(file=fajlnev)
    item2 = vaszon2.create_image(155,155, image=foto2)
    
def valaszt(evt):
    listabeallit()

def bezar():
    global uzenetablak, vege
    uzenetablak.destroy()
    vege = 0
    
def allj():
    global vege, vel, kivalasztott, uzenetablak
    vege = 1
    if vel < kivalasztott and vel >= 0:
        szoveg = "Ön nyert!!!"
    elif vel == 2 and kivalasztott == 0:
        szoveg = "Ön nyert!!!"
    elif vel == kivalasztott:
        szoveg = "Döntetlen!!!"
    else:
        szoveg = "A gép nyert!!!"   
    uzenetablak = Toplevel(ablak) #üzenetablak létrehozása
    uzenetablak.option_add("*font","Arial 11")
    uzenet = Message(uzenetablak, text=szoveg, width=300)
    cmdButton3 = Button(uzenetablak, text="OK", command=bezar)
    uzenet.pack()
    cmdButton3.pack()
    uzenetablak.mainloop()
    
ablak = Tk()
ablak.title("Kő, papír, olló")
ablak.option_add("*font","Arial 11") #ablakban alapértelmezett betűk
for i in range(3):
    ablak.columnconfigure(i,pad = 15) #oszlopok közötti hely
    ablak.rowconfigure(i,pad = 10) #sorok közötti hely
cmdButton1 = Button(ablak, text="Indulj!", width=15, command=indulj)
cmdButton2 = Button(ablak, text="Állj!", width=15, command=allj)
lista = Listbox(ablak, height=3) #3 karaktersor magasságú
lista.bind("<<ListboxSelect>>", valaszt) #listamezőre kattintva ez történik
lista.insert(END, "kő", "papír", "olló") #listamező elemei (az eddigiek után)
lista.select_set(0) #listamezőben alapértelmezetten kiválasztott a 0. sor
vaszon1 = Canvas(ablak, width=310, height=310, bg="white") 
vaszon2 = Canvas(ablak, width=310, height=310, bg="white")
cmdButton1.grid(row = 1, column = 1)
cmdButton2.grid(row = 1, column = 2)
lista.grid(row = 2, column = 2)
vaszon1.grid(row = 3, column = 1)
vaszon2.grid(row = 3, column = 2)
listabeallit()
vege = 0
ablak.mainloop()
