from tkinter import *

def szamol():
    a = float(textBox1.get())
    b = float(textBox2.get())
    x = float(textBox3.get())
    y = float(textBox4.get())
    e = 1.2 * a * b / (x * y)
    textBox5.delete(0, END)
    if int(e) != e:
        e = int(e) + 1
    textBox5.insert(0,str(e))
    
ablak = Tk()
ablak.title("Géza mester")
ablak.option_add("*font","Arial 11")

cmdButton1 = Button(ablak,text="Számol", width = 15, command=szamol)
label1 = Label(ablak,text="Helysiég méretei:")
label2 = Label(ablak,text="Burkolólap méretei:")
label3 = Label(ablak,text="Szükséges padlólapok:")
textBox1 = Entry(ablak)
textBox2 = Entry(ablak)
textBox3 = Entry(ablak)
textBox4 = Entry(ablak)
textBox5 = Entry(ablak)
cmdButton3 = Button(ablak,text="Kilépés", width = 15)
label1.grid(row = 1, column = 1, sticky = E)
label2.grid(row = 2, column = 1, sticky = E)
label3.grid(row = 3, column = 1, sticky = E)
textBox1.grid(row = 1, column = 2, sticky = W)
textBox2.grid(row = 1, column = 3, sticky = W)
textBox3.grid(row = 2, column = 2, sticky = W)
textBox4.grid(row = 2, column = 3, sticky = W)
textBox5.grid(row = 3, column = 2, sticky = W)
cmdButton1.grid(row = 3, column = 3)

for i in range(4):
    ablak.columnconfigure(i,pad = 15)
    ablak.rowconfigure(i,pad = 10)
    
ablak.mainloop()
