from tkinter import *
import sys
from random import randint
import time

window=Tk()  # create window
window.geometry("440x250")

pocet_prikladov=10
evysledok_str=""
font_size=50
mystr=""
body=[]
cislo_prikladu=1

#global odpoved
#global vysledok

#priklad=()

def generuj_scitanie():

    cislo1=0
    cislo2=0
    z=0

    while z<=0:
        if ( cislo1 + cislo2 ) < 10 or (cislo1+cislo2) > 20:
            cislo1 = randint(2, 9)
            cislo2 = randint(3, 18)
        else:
            z=1

    return str(cislo1) + " + " + str(cislo2) + " = ",cislo1+cislo2,0

def generuj_odcitanie():

    cislo1=0
    cislo2=0
    z=0

    while z<=0:
        if  (cislo2-cislo1) < 2:
            cislo1 = randint(2, 17)
            cislo2 = randint(11, 20)
        else:
            z=1

    return str(cislo2) + " - " + str(cislo1) + " = ",cislo2-cislo1,1

def img_good():
    photo = PhotoImage(file="good.png")
    w.configure(image=photo)
    w.photo = photo
    w.grid(row=5, column=2)
    lpredchadzajuci.grid(row=5, column=1)


def img_bad():
    photo = PhotoImage(file="bad.png")
    w.configure(image=photo)
    w.photo = photo
    w.grid(row=5, column=2)
    lpredchadzajuci.grid(row=5, column=1)

def vykonaj(event):

    global mystr
    global vysledok
    global odpoved
    global cislo_prikladu
    global pocet_prikladov

    odpoved = int(evysledok.get())
    print("priklad: "+mystr)
    print("odpoved: "+str(odpoved))
    print("vysledok: "+str(vysledok))
    print(f'cislo prikladu: {cislo_prikladu}')
#    print(f'pocet prikladov: {pocet_prikladov}')

    if odpoved == vysledok:
        print("Dobre :-) ")
        img_good()
        evysledok.delete(0, END)
        body.append(1)

    elif odpoved == 123:
        print(str(body))
        result=0
        for i in range(0,len(body)-1):
            result = result+body[i]
        print(f'pocet bodov: {result} z max poctu {len(body)}')
        sys.exit(0)
    else:
        print("Zle :-(  ")
        img_bad()
        evysledok.delete(0, END)
        body.append(0)

    cislo_prikladu = cislo_prikladu + 1

    if cislo_prikladu > pocet_prikladov:
        print(str(body))
        result=0
        for i in range(0,len(body)):
            result = result+body[i]
        print(f'pocet bodov: {result} z max poctu {len(body)}')
        sys.exit(0)

    d=randint(0,1)

    if d == 0:
        mystr,vysledok,uloha=generuj_odcitanie()
    else:
        mystr,vysledok,uloha=generuj_scitanie()

    lpriklad.configure(text=mystr, font=("Helvetica", font_size))

mystr,vysledok,uloha=generuj_odcitanie()

lpriklad=Label(window,text=mystr, font=("Helvetica", font_size))
lpriklad.grid(row=3, column=1)

evysledok=StringVar()
evysledok=Entry(window, textvariable=evysledok_str, font=("Helvetica", font_size), width=2 )
evysledok.grid(row=3, column=2)

lpredchadzajuci=Label(window,text="Predosly:", font=("Helvetica", font_size))

photo = PhotoImage(file="good.png")
w = Label(window, image=photo)

window.bind('<Return>', vykonaj)
window.mainloop()  # display window
