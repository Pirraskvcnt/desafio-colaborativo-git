print("== PAR OU ÍMPAR ==")
while True:
    nome = input("Informe o seu nome: ")
    numero = int(input("Digite um número: "))
    suce = numero + 1
    ante = numero - 1

    if numero % 2 == 0:
     print(f"Olá, {nome}. O número escolhido é par!")
     print(f"O sucessor desse número é {suce}")
     print(f"O antecessor desse número é {ante}")
    else:
     print(f"Olá, {nome}. O número escolhido é ímpar!")
     print(f"O sucessor desse número é {suce}")
     print(f"O antecessor desse número é {ante}")

    continuar = input("\nDeseja continuar? (s/n): ")

    if continuar.lower() == "n":
        print("Programa encerrado!")
        break