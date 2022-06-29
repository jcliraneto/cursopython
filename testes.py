print("***Comparador de idades mk1***")
sua_idadestr = input("Digite sua idade: ")
comp_idadestr = input("Digite a idade da outra pessoa: ")

sua_idade = int(sua_idadestr)
comp_idade = int(comp_idadestr)

if(sua_idade > comp_idade):
    print("Você é o mais velho")
else:
    print("você é mais novo")

