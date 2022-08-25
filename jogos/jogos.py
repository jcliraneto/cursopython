import forca
import adivinhacao


print("*********************************")
print("***Bem vindo, escolha seu jogo!***")
print("*********************************")

print("(1) Forca  (2) Adivinhação")

jogo = int(input("Escolha seu jogo: "))

if (jogo == 1):
    print("Iniciando FORCA")
elif (jogo == 2):
    print("Iniciando ADIVINHAÇÃO")
