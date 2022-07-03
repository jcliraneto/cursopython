print("*****Calculadora solar mk2*****")

escolhauser = int(input("Escolha 1 (kWp) ou 2 (kWh) para calcular: "))
kwp = escolhauser == 1
kwh = escolhauser == 2

while(escolhauser != 1 and escolhauser !=2):
    print("Escolha apenas as opçoes 1 (kWp) ou 2 (kWh)")
    escolhauser = int(input("Escolha 1 (kWp) ou 2 (kWh) para calcular: "))

    if(kwp):
        print("Você escolheu calcular o valor em kWp!")
        indiceirra = int(input("Digite o indice de irradiação do local: "))
        khwfor = int(input("Digite o valor em kWh: "))
        khpcalc = khwfor/indiceirra
        print("{}kWh equivalem a {:.2f}kWp".format(khwfor, khpcalc))
        print("Programa encerrado!")

    elif(kwh):
        print("Você escolheu calcular o valor em kWh!")
        indiceirra = int(input("Digite o indice de irradiação do local: "))
        kwpfor = float(input("Digite o valor em kWp: "))
        kwhcalc = kwpfor*indiceirra
        print("{:.2f}kWp equivalem a {}kWh".format(kwpfor, kwhcalc))
        print("Programa encerrado!")