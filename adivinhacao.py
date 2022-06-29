print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite seu numero: ")
print("você digitou ", chute_str)
chute = int(chute_str)
acertou = numero_secreto == chute
chutemaior = chute > numero_secreto
chutemenor = chute < numero_secreto

if(acertou):
    print("Você Acertou!")
else:
    if(chutemaior):
        print("você Errou! O seu chute foi maior que o numero secreto.")
    elif(chutemenor):
        print("você Errou! O seu chute foi menor que o numero secreto.")

print("Fim do jogo!")

