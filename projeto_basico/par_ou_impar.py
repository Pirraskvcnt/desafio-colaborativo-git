print("== PAR OU ÍMPAR ==")

resultados = []

while True:
    nome = input("Informe o seu nome: ")
    numero = int(input("Digite um número: "))

    suce = numero + 1
    ante = numero - 1
    dobro = numero * 2

    if numero % 2 == 0:
        tipo = "par"
    else:
        tipo = "ímpar"

    print(f"\nOlá, {nome}. O número escolhido é {tipo}!")
    print(f"O sucessor desse número é {suce}")
    print(f"O antecessor desse número é {ante}")
    print(f"O dobro desse número é {dobro}")

    resultados.append({
        "nome": nome,
        "numero": numero,
        "tipo": tipo,
        "sucessor": suce,
        "antecessor": ante,
        "dobro": dobro
    })

    continuar = input("\nDeseja continuar? (s/n): ")

    if continuar.lower() == "n":
        print("RESUMO DOS RESULTADOS")

        for resultado in resultados:
            print(f"\nNome: {resultado['nome']}")
            print(f"Número: {resultado['numero']} ({resultado['tipo']})")
            print(f"Sucessor: {resultado['sucessor']}")
            print(f"Antecessor: {resultado['antecessor']}")
            print(f"Dobro: {resultado['dobro']}")

        print("Obrigado por utilizar o programa!")
        print("Espero que tenha gostado. Até a próxima!")


        break