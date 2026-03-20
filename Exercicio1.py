#==================================================================================
#CP - 01 
#Atividade 01 ----- Vinícius de Souza Christovam 
#
# Verificador de Idade: Crie um programa que peça a idade do usuário e exiba se ele é criança (0-11), 
# adolescente (12-17), adulto (18-59) ou idoso (60+). Se a idade for negativa ou maior que 120, exiba 
# "Idade inválida".
#
#==================================================================================
def idade ():
    idade = int(input("Qual é sua idade? "))
    if (idade <= 0) or (idade >= 120):
        print("Idade inválida! ")
    elif (idade >= 12) or (idade <= 17):
        print(f"Você é um adolescênte de {idade} anos ")
    elif (idade >= 18) or (idade <= 59):
        print(f"Você é um adulto de {idade} anos ")
    elif (idade >= 60) or (idade <= 120):
        print(f"Você é um idoso de {idade} anos ")
    elif (idade >= 1 ) or (idade <= 11):
        print(f"Você é uma criança de {idade} anos" )
idade ()