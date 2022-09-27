import random

def jogar():
    print("********************************")
    print("****Bem vindo ao jogo FORCA!****")
    print("********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)


    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("Você só pode errar 6 vezes!")

    while not enforcou and not acertou:

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            print("A letra {} está na palavra secreta!".format(chute))
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("A letra {} não está na palavra secreta".format(chute))
            print("Você ainda pode errar {} vezes! ".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabens, você ganhou!! a palavra era {}".format(palavra_secreta))
    else:
        print("Você perdeu!!, tente novamente")
    print("fim do jogo!")


if __name__ == "__main__":
    jogar()
