print("***Comparador de idades mk1***")
sua_idadestr = input("Digite sua idade: ")
comp_idadestr = input("Digite a idade da outra pessoa: ")

sua_idade = int(sua_idadestr)
comp_idade = int(comp_idadestr)
idadesiguais = sua_idade == comp_idade
maisnovo = sua_idade < comp_idade
maisvelho = sua_idade > comp_idade

if(idadesiguais):
    print("Vocês tem a mesma idade!")
else:
    if(maisnovo):
        print("Você é mais novo que a outra pessoa")
    elif (maisvelho):
        print("Você é mais velho que a outra pessoa")

