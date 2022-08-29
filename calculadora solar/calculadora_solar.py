import kwp
import kwh

print("                      ")
print("***Bem vindo ao calculadora solar!***")
print("                      ")


for calcular in range (1000):
    print("(1) Calcular KwP   (2) Calcular KwH")
    calcular = int(input("Escolha a opção que deseja calcular: "))

    if (calcular == 1):
                kwp.Calc()
                break

    else:
        if (calcular == 2):
                kwh.calc()
                break

        elif (calcular != 1 or calcular != 2):
            print("Você escolheu uma opção incorreta")
            continue