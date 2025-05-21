moedaReal = 100.00

print("Valor a ser convertido:",moedaReal)
print("taxa do Dolar: 5.20")
print("taxa do Euro: 6.15")

moedaParaConversao = int(input("Escolha 1 para dolar e 2 para Euro:"))

if(moedaParaConversao == 1):
    print("Valor convertido para Dolar:", moedaReal * 5.20)
else:
    print("Valor convertido para Euro:", moedaReal * 6.15)


print("------------------------------------------------------------------")

nomeDoProduto = "camiseta"
precoDoProduto = 50.00
descontoDoProduto = 0.2

descontoNoProduto = int(input("Vai ter desconto: 1 - Sim | 2 - Nao\n"))

if(descontoNoProduto == 1):
    print("Valor com desconto:", precoDoProduto - (descontoDoProduto * precoDoProduto))
else:
    print("Valor sem desconto:", precoDoProduto)

print("------------------------------------------------------------------")

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

mediaDasNotas = (nota1 + nota2 + nota3) / 3

if(mediaDasNotas >= 6):
    print("Parabens passou de ano, media final:"f"{mediaDasNotas:.2f}")
else:
    print("Ficou de Recuperacao com a media final de:"f"{mediaDasNotas:.2f}")


print("------------------------------------------------------------------")


distanciaPercorrida = 300
combustivelGasto = 25.00

consumoMedio = distanciaPercorrida / combustivelGasto

print(" Foram gastos em media:",f"{consumoMedio:.2f}","\n","distancia percorrida:",distanciaPercorrida,"\n","combustivel gasto:",combustivelGasto)

