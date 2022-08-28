
def calc():

    print("                      ")
    print("**********************")
    print("*****Calcular KwH*****")
    print("**********************")
    print("                      ")

    kwp = float(input("informe o KwP desejado: "))
    indicesolar = int(input("Informe o indice de irradiação do local de instalação: "))

    kwh = int(kwp * indicesolar)
    print("                      ")
    print("{:.2f} KwP equivale a {} KwH".format(kwp,kwh))