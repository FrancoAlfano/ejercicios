#Ejercicio1

import argparse

def ejercicio_1():
    parser = argparse.ArgumentParser()
    operacion = parser.add_mutually_exclusive_group()

    operacion.add_argument("-s", "--suma", help="suma 2 argumentos", action="store_true")
    operacion.add_argument("-r", "--resta", help="resta 2 argumentos", action="store_true")
    operacion.add_argument("-m", "--multi", help="multiplica 2 argumentos", action="store_true")
    operacion.add_argument("-d", "--divi", help="divide 2 argumentos", action="store_true")
    
    parser.add_argument("-t", help="tipo de numero")

    parser.add_argument("arg1", help="Argumento 1")
    parser.add_argument("arg2", help="Argumento 2")

    args = parser.parse_args()

    if args.t == "int":
        arg1 = int(args.arg1)
        arg2 = int(args.arg2)
    elif args.t == "float":
        arg1 = float(args.arg1)
        arg2 = float(args.arg2)

    if args.suma:
        print(arg1+arg2)
    elif args.resta:
        print(arg1-arg2)
    elif args.multi:
        print(arg1*arg2)
    elif args.divi:
        print(arg1/arg2)


if __name__ == "__main__":
    ejercicio_1()