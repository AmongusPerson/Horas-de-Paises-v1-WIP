from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time
pg = Tk()
pg.geometry("500x500")
pg.title("Horas de Paises")

lb1 = Label(pg, text="Zona Horaria EEUU")
lb1.place(relx=0.5, rely=0.05, anchor=CENTER)

lb2 = Label(pg, text=".")
lb2.place(relx=0.5, rely=0.25, anchor=CENTER)

def fn1():
    vr1 = pytz.timezone("US/Central")
    vr2 = datetime.now(vr1)
    vr3 = vr2.strftime("%I %p:%M:%S")
    lb2["text"] = vr3
 
bt1 = Button(pg, text="Ejecutar", bg="#e76f51", fg="white", command=fn1)
bt1.place(relx=0.5, rely=0.15, anchor=CENTER)

pg.mainloop()