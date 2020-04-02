#Ejercicio 3
import os
import re

def ejercicio3():
    e_mail = r"[a-zA-Z]\w+([\.-]\w+)*@\w+([\.-]\w+)*\.*"
    saldo = r"\d*$"

    
    with open("archivo.csv") as f:
        for linea in f:
            match_saldo = re.search(saldo, linea)
            if match_saldo != None:
                if (int(match_saldo.group()))>1200:
                    print(re.search(e_mail, linea).group())

if __name__ == "__main__":
    ejercicio3()