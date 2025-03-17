from tkinter import *

def nevjegy():
    uzenetablak = Toplevel(ablak)
    uzenetablak.option_add("*font","Arial 11")
    uzenet = Message(uzenetablak, \
        text="Magyary Gyula\n2020.05.02.", width=300)
    cmdButton4 = Button(uzenetablak, text="OK", \
        command=uzenetablak.destroy)
    uzenet.pack()
    cmdButton4.pack()
    uzenetablak.mainloop()

def menuvaltas():
    label3.configure(text = "Átváltva: ")
    textBox1.delete(0,END)
    textBox3.delete(0,END)
    
def homerseklet():
    global m
    m = 'T'
    label1.configure(text = "Celsiusban: ")
    rButton1.configure(text = "Kelvin")
    rButton2.configure(text = "Fahrenheit")
    rButton3.configure(text = "Celsius")
    menuvaltas()
    
def nyomas():
    global m
    m = 'p'
    label1.configure(text = "Pascalban: ") 
    rButton1.configure(text = "Higanymilliméter")
    rButton2.configure(text = "Atmoszféra (fizika)")
    rButton3.configure(text = "Bar")
    menuvaltas()
    
def terfogat():
    global m
    m = 'V'
    label1.configure(text = "Köbméterben: ")
    rButton1.configure(text = "Köbdeciméter")
    rButton2.configure(text = "Köbcentiméter")
    rButton3.configure(text = "Liter")
    menuvaltas()
    
def szamol():
    be = float(textBox1.get())
    if m == 'T':
        if rb.get() == '0':
            ki = be + 273.15
            label3.configure(text = "Kelvinben: ")
        elif rb.get() == '1':
            ki = 1.8 * be +32
            label3.configure(text = "Fahrenheitben: ")
        else:
            ki = 0.8 * be
            label3.configure(text = "Reynmurban: ")
    elif m == 'p':
        if rb.get() == '0':
            ki = be / 133.322
            label3.configure(text = "Higanymilliméterben: ")
        elif rb.get() == '1':
            ki = be / 101325
            label3.configure(text = "Atmoszférában: ")
        else:
            ki = be / 100000
            label3.configure(text = "Barban: ")
    else:
        if rb.get() == '0':
            ki = be * 1000
            label3.configure(text = "Köbdeciméterben: ")
        elif rb.get() == '1':
            ki = be * 1000000
            label3.configure(text = "Köbcentiméterben: ")
        else:
            ki = be * 1000
            label3.configure(text = "Literben: ")        
    textBox3.delete(0,END)
    textBox3.insert(0,ki)
        
ablak = Tk()
ablak.title("Átváltás")
for i in range(4):
    ablak.columnconfigure(i,pad = 15)
    ablak.rowconfigure(i,pad = 10)
ablak.option_add("*font","Arial 11")
menusor = Frame(ablak)
menusor.grid(row = 1, column = 1)
menu1 = Menubutton(menusor, text="Fájl")
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label="Névjegy", command=nevjegy)
fajl.add_command(label="Kilépés", command=ablak.destroy)
menu1.config(menu = fajl)
menu2 = Menubutton(menusor, text="Mennyiségek")
menu2.pack()
feladat = Menu(menu2)
feladat.add_command(label="Hőmérséklet", command=homerseklet)
feladat.add_command(label="Térfogat", command=terfogat)
feladat.add_command(label="Nyomás", command=nyomas)
menu2.config(menu = feladat)

textBox1 = Entry(ablak)
textBox3 = Entry(ablak)
label1 = Label(ablak,text="Celsiusban:")
label3 = Label(ablak,text="Átváltva:")
cmdButton1 = Button(ablak,text="Számol", width = 15, command=szamol)
cmdButton2 = Button(ablak,text="Kilépés", width = 15, command=ablak.destroy)
rb = StringVar()
rButton1 = Radiobutton(ablak, value='0', \
    text="Kelvin", variable = rb, command = szamol)
rButton2 = Radiobutton(ablak, value='1', \
    text="Fahrenheit", variable = rb, command = szamol)
rButton3 = Radiobutton(ablak, value='2', \
    text="Reynmur", variable = rb, command = szamol)
rButton1.invoke()
label1.grid(row = 2, column = 1, sticky = W, padx = 10)
textBox1.grid(row = 3, column = 1)
rButton1.grid(row = 4, column = 1, padx = 10, sticky = W)
rButton2.grid(row = 5, column = 1, padx = 10, sticky = W)
rButton3.grid(row = 6, column = 1, padx = 10, sticky = W)
cmdButton1.grid(row = 7, column = 1)
label3.grid(row = 8, column = 1, sticky = W, padx = 10)
textBox3.grid(row = 9, column = 1)
cmdButton2.grid(row = 10, column = 1)
m = 'T'
ablak.mainloop()
