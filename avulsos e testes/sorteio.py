import random

jogadores = []

escolha = 0

print("*****SorteioPY******")
print("Inicie escrevendo o nome do primeiro jogador!")
while escolha == 0 or escolha.lower() == "j":
    player = input("Diga o nome do jogador: ")
    jogadores.append(player)
    print("{} foi adicionado a lista".format(player))
    print(jogadores)
    escolha = input("Deseja adicionar mais um jogador ou iniciar o sorteio?(J/S): ")
    continue


if escolha.lower() == "s":
   escolhido = random.choice(jogadores)
   print("*********INICIANDO SORTEIO!********")
   print("{} foi escolhido!".format(escolhido.upper()))
   print("*****Fim de SorteioPy, BOM JOGO!******")

elif escolha != "s" or escolha != "j":
    print("Valor inválido.. programa encerrado!")

