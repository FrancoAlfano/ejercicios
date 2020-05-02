#Ejercicio 1

import os
import sys

def ejercicio_1():
    archivo = sys.argv[1]
    fd = os.open(archivo, os.O_RDWR | os.O_CREAT)
    fd_r, fd_w = os.pipe()
    pid = os.fork()
    
    FIN = False
    while FIN == False:
        leido = os.read(fd, 1024)
        os.write(fd_w, leido)

        if pid == 0: #child
            hijo_lee = os.read(fd_r, 100)
            print("soy hijo: ", os.getpid(), " y mi padre es: ", os.getppid())
            print(hijo_lee)

        if len(leido) < 1024:
            FIN = True



if __name__ == "__main__":
    ejercicio_1()