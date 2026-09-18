nome = input("Informe o seu nome: ")
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"Olá, {nome}. O número escolhido é par!")
else:
    print(f"Olá, {nome}. O número escolhido é ímpar!")