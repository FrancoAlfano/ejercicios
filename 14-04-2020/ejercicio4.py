#Ejercicio 4

import os

while True:
    pid = os.fork()
    if pid == 0:
        print(pid)
    else:
        continue