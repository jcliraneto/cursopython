import random

def jogar():

    print("************************************")
    print("***Bem vindo ao jogo Adivinhação!***")
    print("************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Escolha o nível: "))

    if(nivel == 1):
        total_de_tentativas = 25
    elif(nivel == 2):
        total_de_tentativas = 15
    else:
        total_de_tentativas = 10


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
            print("Você fez {} pontos!!".format(pontos))
            break
        else:
            if(chutemaior):
                print("você Errou! O seu chute foi maior que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
            elif(chutemenor):
                print("você Errou! O seu chute foi menor que o numero secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("fim do jogo! tente outra vez")

if(__name__ == "__main__"):
    jogar()
