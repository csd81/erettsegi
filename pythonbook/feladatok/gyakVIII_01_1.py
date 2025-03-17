from tkinter import *

def szamol():
    tav = int(textBox1.get())
    if tav < 3:
        ossz = 500
    elif tav < 6:
        ossz = 700
    elif tav < 11:
        ossz = 900
    elif tav < 21:
        ossz = 1400
    else:
        ossz = 2000
    textBox2.delete(0,END)
    textBox2.insert(0,str(ossz))

ablak = Tk()

ablak.option_add("*font","Arial 11")
label1 = Label(ablak,text="Távolság km-ben: ")
label2 = Label(ablak,text="Fizetés Ft-ban: ")
textBox1 = Entry(ablak)
cmdButton2 = Button(ablak,text="Meghatároz", width = 15, command=szamol)
textBox2 = Entry(ablak)
label1.pack()
textBox1.pack()
cmdButton2.pack()
label2.pack()
textBox2.pack()

ablak.mainloop()
