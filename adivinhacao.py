print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite seu numero: ")
chute = int(chute_str)

print("você digitou ", chute_str)

if(numero_secreto == chute_str):
    print("Você Acertou!! Malandrão heim!")
else:
    print("você errou seu burro... caralho heim")


