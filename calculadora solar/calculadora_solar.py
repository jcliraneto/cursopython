import kwp
import kwh

print("                      ")
print("***Bem vindo ao calculadora solar!***")
print("                      ")

print("(1) Calcular KhP   (2) Calcular KwH")
calcular = int(input("Escolha a opção que deseja calcular: "))

if (calcular == 1):
    kwp.Calc()
elif (calcular == 2):
    kwh.calc()