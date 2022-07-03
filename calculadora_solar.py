print("*****Calculadora solar mk1*****")

calcular = (input("Digite a unidade que deseja calcular. (KWH ou KWP): "))

if (calcular = KWH):

    KWH = int(input("Digite a quantidade de kWh: "))
    indicesolar = int(input("Digite o indice de irradiação solar: "))
    KWP = float(KWH / indicesolar)

    print("{}kWh corresponde a {:.3}kWp".format(KWH, KWP))
    print("Fim do programa!")