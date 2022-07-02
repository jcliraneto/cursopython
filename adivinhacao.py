print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite seu numero: "))
    print("você digitou ", chute)

    acertou    = chute == numero_secreto
    chutemaior = chute > numero_secreto
    chutemenor = chute < numero_secreto

    if(acertou):
        print("Você Acertou! Parabéns!!")
    else:
        if(chutemaior):
            print("você Errou! O seu chute foi maior que o numero secreto.")
        elif(chutemenor):
            print("você Errou! O seu chute foi menor que o numero secreto.")
    rodada = rodada + 1

print("Não fo dessa vez... fim do jogo!")

