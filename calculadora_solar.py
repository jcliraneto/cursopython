print("*****Calculadora solar mk2*****")

escolhauser = int(input("Escolha 1 (kWp) ou 2 (kWh) para calcular: "))
kwp = escolhauser == 1
kwh = escolhauser == 2

if(kwp):
    indiceirra = int(input("Digite o indice de irradiação do local: "))
    khwfor = int(input("Digite o valor em kWh: "))
    khpcalc = khwfor/indiceirra
    print("{}kWh equivalem a {:.2f}kWp".format(khwfor, khpcalc))
    print("Programa encerrado!")
else:
    indiceirra = int(input("Digite o indice de irradiação do local: "))
    kwpfor = float(input("Digite o valor em kWp: "))
    kwhcalc = kwpfor*indiceirra
    print("{:.2f}kWp equivalem a {}kWh".format(kwpfor, kwhcalc))
    print("Programa encerrado!")