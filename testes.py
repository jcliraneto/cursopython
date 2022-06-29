print("***Comparador de idades mk1***")
sua_idadestr = input("Digite sua idade: ")
comp_idadestr = input("Digite a idade da outra pessoa: ")
sua_idade = int(sua_idadestr)
comp_idade = int(comp_idadestr)
idadesiguais = sua_idade == comp_idade
maisnovo = sua_idade < comp_idade
maisvelho = sua_idade > comp_idade
dif_idaden = comp_idade - sua_idade
dif_idadev = sua_idade - comp_idade

if(idadesiguais):
    print("Vocês tem a mesma idade!")
else:
    if(maisnovo):
        print("Você é", dif_idaden, "anos mais novo que a outra pessoa")
    elif (maisvelho):
        print("Você é", dif_idadev, "anos mais velho que a outra pessoa")

print("Fim do programa!")


