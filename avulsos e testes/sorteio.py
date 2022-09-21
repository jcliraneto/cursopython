import random

jogadores = []

escolha = input("Deseja adicionar um jogador ou iniciar sorteio?(J/S): ")


while escolha.lower() == "j":
    player = input("Diga o nome do jogador: ")
    jogadores.append(player)
    print("{} foi adicionado a lista".format(player))
    print(jogadores)
    escolha = input("Deseja adicionar mais um jogador ou iniciar o sorteio?(J/S): ")
    continue

if escolha.lower() == "s":
   escolhido = random.choice(jogadores)
   print("{} foi escolhido!".format(escolhido))
   print("Fim de SorteioPy")
elif escolha != "s" or escolha != "j":
    print("Valor inválido.. programa encerrado!")

