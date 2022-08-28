
def Calc():

    print("                      ")
    print("**********************")
    print("*****Calcular KwP*****")
    print("**********************")
    print("                      ")

    kwh = int(input("informe o KwH desejado: "))
    indicesolar = int(input("Informe o indice de irradiação do local de instalação: "))

    kwp = float(kwh/indicesolar)
    print("                      ")
    print("{} KwH equivale a {:.2f} KwP".format(kwh,kwp))