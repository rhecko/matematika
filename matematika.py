#!/usr/bin/python3

import sys
from random import randint
import time
#while True:

priklad=()




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



#for i in range(0,20):
#    priklad=generuj_scitanie()
#    print(str(priklad[0]) + " + " + str(priklad[1]) + " = ")





for i in range(0,50):
    #cislo1 = randint(10, 20)
    #cislo2 = randint(0, 10)

    #while cislo1 + cislo2 > 20 :
    #    cislo1 = randint(10, 20)
    #    cislo2 = randint(0, 10)

#print cislo1
#print cislo2
    d=randint(0,1)

    if d == 0:
        mystr,vysledok,uloha=generuj_odcitanie()
    else:
        mystr,vysledok,uloha=generuj_scitanie()


    odpoved = None
    while True:
        try:
            #odpoved = 0
    #        Thread(target = check).start()
            start = time.time()
            odpoved = int(input(mystr))
            now = time.time()

            print(now - start)

            if (now - start) <= 10:
                #print("trvalo ti to:" + str(now - start)
                if odpoved == vysledok:
                    print("Dobre :-) ")
                    break
                elif odpoved == 123:
                    sys.exit(0)
                else:
                    print("Zle :-(  ")
            else:
                #print(f'Neskoro: trvalo ti to: {now - start}')
                if odpoved == vysledok:
                    print("Dobre, ale neskoro ")
                    break
                elif odpoved == 123:
                    sys.exit(0)
                else:
                    print("Zle a aj neskoro :-((  ")
                    break

        except ValueError:
            break
            #print("... napis prosim odpoved. Dakujem. ")
            #continue
#        else:
#            break

    #odpoved = int(odpoved)
