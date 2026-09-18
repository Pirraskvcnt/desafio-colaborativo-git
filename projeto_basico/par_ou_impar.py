print("== PAR OU ÍMPAR ==")
while True:
    numero = int(input("Digite um número: "))


    if numero % 2 == 0:
     print("O número é par!")
    else:
     print("O número é ímpar!")

     print("O sucessor desse número é", numero + 1)
     print("O antecessor desse número é", numero - 1)

    continuar = input("\nDeseja continuar? (s/n): ")

    if continuar.lower() == "n":
        print("Programa encerrado!")
        break