from tkinter import *

def szamol():
    be = float(textBox1.get())
    if rb.get() == '0':
        ki = be + 273.15
        label3.configure(text = "Kelvinben: ")
    elif rb.get() == '1':
        ki = 1.8 * be +32
        label3.configure(text = "Fahrenheitben: ")
    else:
        ki = 0.8 * be
        label3.configure(text = "Reynmurban: ")
    textBox3.delete(0,END)
    textBox3.insert(0,ki)
        
ablak = Tk()
ablak.title("Hőmérsékletváltás")
for i in range(4):
    ablak.columnconfigure(i,pad = 15)
    ablak.rowconfigure(i,pad = 10)
ablak.option_add("*font","Arial 11")
textBox1 = Entry(ablak)
textBox3 = Entry(ablak)
label1 = Label(ablak,text="Celsius:")
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
label1.grid(row = 1, column = 1, sticky = W, padx = 10)
textBox1.grid(row = 2, column = 1)
rButton1.grid(row = 3, column = 1, padx = 10, sticky = W)
rButton2.grid(row = 4, column = 1, padx = 10, sticky = W)
rButton3.grid(row = 5, column = 1, padx = 10, sticky = W)
cmdButton1.grid(row = 6, column = 1)
label3.grid(row = 7, column = 1, sticky = W, padx = 10)
textBox3.grid(row = 8, column = 1)
cmdButton2.grid(row = 9, column = 1)

ablak.mainloop()
