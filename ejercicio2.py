#Ejercicio 2

import os

def ejercicio2():
    print("Ingrese archivo origen:")
    origen = input()
    print("Ingrese archivo destino:")
    destino = input()

    ori = os.open(origen, os.O_RDONLY)
    des = os.open(destino, os.O_RDWR)

    FIN = False
    while FIN == False:
        leido = os.read(ori, 1024)
        os.write(des, leido)
        if len(leido) < 1024:
            FIN = True

    os.close(ori)
    os.close(des)    



if __name__ == "__main__":
    ejercicio2()