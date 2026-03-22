#==================================================================================
#Atividade 04
#Classificador de Triângulos: Crie um programa que peça 3 valores representando os lados de 
# um triângulo. Primeiro, verifique se os valores formam um triângulo válido 
# (a soma de dois lados deve ser maior que o terceiro — teste as 3 combinações).
# Se for válido, classifique como equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes).
#  Se não for válido, exiba "Não forma triângulo".
#
#==================================================================================
validação = int(input("Diga o primeiro valor -> "))
validação2 = int(input("Diga o segundo valor -> "))
validação3 = int(input("Diga o terceiro valor -> "))
def triangulo():
    if (validação + validação2 <= validação3):
        print("Triângulo inválido! ")
    elif (validação2 == validação2 == validação3):
        print("Este é um triângulo equilátero. ")
    elif (validação == validação2) or (validação == validação3) or (validação3 == validação2):
        print("Este é um triângulo isósceles. ")
    else:
        print("Este é um triângulo escaleno. ")
triangulo()
