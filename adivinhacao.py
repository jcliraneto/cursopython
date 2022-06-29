print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite seu numero: ")
print("você digitou ", chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Você Acertou!")
else:
    print("você Errou!")

print("Fim do jogo!")

