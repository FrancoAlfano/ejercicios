#Ejercicio 2

import argparse
import os

def ejercicio_2():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="incrementa verbosidad", action="store_true")

    parser.add_argument("-n", "--base", help="la base")
    parser.add_argument("-m", "--exponente", help="el exponente")
    
    args = parser.parse_args()
    
    n = os.fork() 
  
    # n greater than 0  means parent process 
    if n > 0: 
        print("ID del padre: ", os.getpid())
        if args.verbose:
            print("Argumentos ingresados, leidos por padre: {}".format(args))
  
    # n equals to 0 means child process 
    else: 
        print("ID del hijo: ", os.getpid())
        respuesta = int(args.base)**int(args.exponente)

        print("El resultado calculado por el hijo: ", respuesta, " siendo el padre: ", os.getppid())


if __name__ == "__main__":
    ejercicio_2()