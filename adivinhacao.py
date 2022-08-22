import random


print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3
print(numero_secreto)

for rodada in range (1, total_de_tentativas + 1):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite um número entre 1 e 100: "))
    print("você digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100 ")
        continue

    acertou = chute == numero_secreto
    chutemaior = chute > numero_secreto
    chutemenor = chute < numero_secreto

    if(acertou):
        print("Você Acertou! Parabéns!!")
        break
    else:
        if(chutemaior):
            print("você Errou! O seu chute foi maior que o numero secreto.")
        elif(chutemenor):
            print("você Errou! O seu chute foi menor que o numero secreto.")

print("fim do jogo!")

