import random


def jogar():
    mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    print("Você só pode errar 6 vezes!")

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:

            marca_chute_correto(chute, letras_acertadas, palavra_secreta)

        else:
            erros += 1
            print("A letra {} não está na palavra secreta".format(chute))
            print("Você ainda pode errar {} vezes! ".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Parabens, você ganhou!! a palavra era {}".format(palavra_secreta))
    else:
        print("Você perdeu!!, tente novamente")
    print("fim do jogo!")


def mensagem_de_abertura():
    print("********************************")
    print("****Bem vindo ao jogo FORCA!****")
    print("********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    print("A letra {} está na palavra secreta!".format(chute))
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


if __name__ == "__main__":
    jogar()
