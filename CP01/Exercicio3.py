#==================================================================================
#Atividade 03
#
#Conversor de Moedas: Crie um programa que exiba um menu com 3 opções de conversão:
#  Real → Dólar, Real → Euro, Real → Libra. O usuário escolhe 
# a opção, digita o valor em reais e o programa exibe o valor convertido com 2 casas decimais. 
# Se o usuário escolher uma opção inválida, exiba 
# "Opção inválida". Se digitar um valor negativo, exiba "Valor inválido".
#
#==================================================================================
print("========================MENU=========================")
print("[1] Real -> Dólar ")
print("[2] Real -> Euro ")
print("[3] Real -> Libra ")
print("=====================================================")
opção = int(input("Escolha a opção alguma opção acima -> "))
if (opção > 3) or (opção <= 0):
    print("Opção inválida! ")
    exit()

valor = float(input("Qual é o valor desejado para converção? -> "))

def dolar(dolar):
    dolar = valor / 5.15
    return dolar
def euro(euro):
    euro = valor / 5.55
    return euro
def libra(libra):
    libra = valor / 6.45
    return libra

if (opção == 1):
    print(f"{valor} Reais convertidos para Dólar é -> ${dolar(valor):.2f}")
elif (opção == 2):
    print(f"{valor} Reais convertidos para Euro é -> €{euro(valor):.2f}")
elif (opção == 3):
    print(f"{valor} Reais convertidos para Libra é -> £{libra(valor):.2f}")
else:
    print("Opção inválida")
