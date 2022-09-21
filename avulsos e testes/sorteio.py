import random

jogadores = []


print("*****SorteioPY******")
print("Inicie escrevendo o nome do primeiro jogador!")

escolha = input("Diga o nome do jogador: ")

while escolha.lower() != "sorteio":
    jogadores.append(escolha)
    print("{} foi adicionado a lista".format(escolha))
    print(jogadores)
    escolha = input("Digite o nome do proximo jogador ou digite SORTEIO para iniciar: ")
    continue


if escolha.lower() == "sorteio":
   escolhido = random.choice(jogadores)
   print("*********INICIANDO SORTEIO!********")
   print("A primeira pessoa a jogar será.... {}!".format(escolhido.upper()))
   print("*****Fim de SorteioPy, BOM JOGO!******")
