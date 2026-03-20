#==================================================================================
#Atividade 07
# Simulador de Caixa Eletrônico: Crie um programa que simule um caixa eletrônico.
#  O usuário digita um valor de saque (inteiro, múltiplo de 10) e o programa calcula a menor quantidade de cédulas necessárias.
#  Cédulas disponíveis: R$ 200, R$ 100, R$ 50, R$ 20 e R$ 10.
#  Valide se o valor é positivo, inteiro e múltiplo de 10.
#  Exiba cada cédula usada e a quantidade.
#==================================================================================
def saque ():
    saque = int(input("Digite o valor do saque (múltiplo de 10): R$ "))
    if saque <= 0:
        print("Valor inválido! O saque deve ser positivo.")
    elif saque % 10 != 0:
        print(f"Valor inválido! R$ {saque} não é múltiplo de 10.")
    else:
        dinheiro = [200, 100, 50, 20, 10]   
        restante = saque
        total_cedulas = 0
        print("=" * 30)
        print(f"=== Saque: R$ {saque} ===")
        print("=" * 30)

        for cedula in dinheiro:
            quantidade = restante // cedula   
            restante   = restante % cedula    

            if quantidade > 0:
                print(f"R$ {cedula:<4}: {quantidade} cédula(s)")
                total_cedulas += quantidade

        print("-" * 30)
        print(f"Total de cédulas: {total_cedulas}")
        print("=" * 30)
saque()