import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("***Bem vindo, escolha seu jogo!***")
    print("*********************************")

    print("(1) Forca  (2) Adivinhação")

    jogo = int(input("Escolha seu jogo: "))

    if (jogo == 1):
        print("Iniciando FORCA")
        forca.jogar()
    elif (jogo == 2):
        print("Iniciando ADIVINHAÇÃO")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()