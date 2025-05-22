idadeInserida = 15

if(0 >= idadeInserida <= 12):
    print("crianca")
elif(idadeInserida <= 17):
    print("adolecente")
elif(idadeInserida <= 59):
    print("adulto")
else:
    print("idoso")

pesoEmKg = float(input("Digite seu peso aqui em KG:\n"))
alturaEmMetros = float(input("Digite sua altura em Metros:\n"))

resultadoImc = pesoEmKg / (alturaEmMetros * alturaEmMetros)
print(resultadoImc)

if(resultadoImc < 18.5):
    print("Abaixo do peso")
elif(resultadoImc < 25):
    print("Peso normal")
elif(resultadoImc < 30):
    print("Sobrepeso")
else:
    print("Obeso")

print("---------------------------------------------------------------")

temperaturaOrigem = float(input("Digite a temperatura atual: "))
unidadeOrigem = int(input("Em qual unidade esta:\n 1 - Celsius 2 - Fahrenheit 3 - Kelvin"))
unidadeDestino = int(input("Qual unidade deseja colocar:\n 1 - Celsius 2 - Fahrenheit 3 - Kelvin"))

match unidadeOrigem:
    case 1:
        if(unidadeDestino == 1):
            print(temperaturaOrigem)
        elif(unidadeDestino == 2):
            print(temperaturaOrigem * 1.8 + 32)
        else:
            print(temperaturaOrigem + 273.15)
    case 2:
        if(unidadeDestino == 1):
            print((temperaturaOrigem - 32) / 1.8)
        elif(unidadeDestino == 2):
            print(temperaturaOrigem)
        else:
            print(273.15 + (5/9)*(temperaturaOrigem - 32))
    case 3:
        if(unidadeDestino == 1):
            print(temperaturaOrigem - 273.15)
        elif(unidadeDestino == 2):
            print((temperaturaOrigem - 273.15) * (9/5) + 32)
        else:
            print(temperaturaOrigem)
        

anoBisexto = int(input("Digite um ano que voce ache que e bissexto:\n"))

if(anoBisexto % 4 == 0 and anoBisexto % 100 != 0 ):
    print("Ano bissexto")
else:
    print("Nao e bissexto o ano")