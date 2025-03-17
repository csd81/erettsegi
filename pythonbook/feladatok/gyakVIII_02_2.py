from tkinter import *
from random import randrange

def eredeti():
    kijelzo.delete("1.0","end")
    for i in range(len(words)-1):
        kijelzo.insert(INSERT, words[i]+"\n")
        
def feladat():
    kijelzo.delete("1.0","end")
    rendezett = words.copy()   
    rendezett.sort()
    if chk.get() == 1:
        rendezett.reverse()
    for i in range(len(words)-1):
        kijelzo.insert(INSERT, rendezett[i]+"\n")


def cbtn():
    global valt
    if valt == 0:
        feladat()
        valt = 1
        cmdButton.configure(text = "Rendezetlen")
    else:
        eredeti()
        valt = 0
        cmdButton.configure(text = "Rendez")
    
ablak = Tk()
ablak.option_add("*Font", "Arial 11")

keret = Frame(ablak)
kijelzo = Text(keret, height=5, width=20)
cmdButton = Button(ablak, text="Rendez", command=cbtn)
scrkijelzof = Scrollbar(keret)
scrkijelzof.config(command=kijelzo.yview)
kijelzo.config(yscrollcommand = scrkijelzof.set)
chk = IntVar()
chkButton = Checkbutton(ablak, \
    text="Fordítva rendez", variable = chk)
keret.pack()
kijelzo.pack(side=LEFT)
scrkijelzof.pack(side=RIGHT, fill=Y)
chkButton.pack()
cmdButton.pack()
words = ["izomtalan", "tornyai", "abbahagyjuk", "rideg", "azon", "mindenhonnan", "nem"]
eredeti()
valt = 0

ablak.mainloop()
