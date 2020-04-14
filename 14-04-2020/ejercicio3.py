#Ejercicio 3

import argparse
import os

def ejercicio_2():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="incrementa verbosidad", action="store_true")
    parser.add_argument("-c", "--childs", help="la cantidad de hijos que desee")
    x = 0
    
    args = parser.parse_args()
   
    if x < int(args.childs):
        n = os.fork()
        if n == 0:
            print("Yo soy: ", os.getppid()," Mi padre es: ", os.getpid())
        x += 1



if __name__ == "__main__":
    ejercicio_2()