print("*****Calculadora solar mk1*****")

KWH = int(input("Digite a quantidade de kWh: "))
indicesolar = int(input("Digite o indice solar: "))
KWP = float(KWH / indicesolar)

print("{}kWh corresponde a {:.3}kWp".format(KWH, KWP))