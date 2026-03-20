#==================================================================================
#Atividade 02
#
#Calculadora de IMC: Crie um programa que peça peso (kg) e altura (m), calcule o IMC (peso / altura²)
# e exiba a classificação: abaixo do peso (< 18.5), peso normal (18.5 - 24.9), sobrepeso (25.0 - 29.9), 
# obesidade (≥ 30.0). Exiba o resultado com 1 casa decimal.
#==================================================================================
peso = float(input("Qual é seu peso? "))
altura = float(input ("Qual é sua altura? "))
IMC = peso / altura**2
def IMC():
    float(IMC)
    if (IMC < 18.5):
        print(f"Seu IMC é {IMC:.1f}, você está abaixo do peso ideal. ")
    elif(IMC <= 24.9):
        print(f"Seu IMC é {IMC:.1f}, você está no peso ideal. ")
    else:
        print(f"Seu IMC é {IMC:.1f}, você está em uma situação de sobrepeso. ")
IMC()