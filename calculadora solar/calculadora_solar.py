import kwp
import kwh

print("                      ")
print("***Bem vindo ao calculadora solar!***")
print("                      ")


print("(1) Calcular KhP   (2) Calcular KwH")
calcular = int(input("Escolha a opção que deseja calcular: "))

if (calcular == 1):
        kwp.Calc()

else:
    if (calcular == 2):
        kwh.calc()

    elif (calcular != 1 or calcular != 2):
        print("Você selecionou uma opção errada!")