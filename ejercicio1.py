#Ejercicio 1
import sys 

def ejercicio1():
    leido = sys.stdin.read()
    lista = leido.split(" ")
    lista_reversa = [i[::-1] for i in lista]
    string_reverso = " ".join(lista_reversa)

    print(string_reverso)
    
if __name__ == "__main__":
    ejercicio1()
