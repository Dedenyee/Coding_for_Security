#==================================================================================
#Atividade 05
#
# Calculadora de Desconto Progressivo: Crie um programa para uma loja que aplica descontos baseados no valor da compra:
#  até R$ 100 não tem desconto, de R$ 100.01 a R$ 300 tem 10% de desconto, de R$ 300.01 a R$ 500 tem 15%, acima de R$ 500 tem 20%.
#  Além disso, se o cliente for VIP (pergunte sim ou não), ganha 5% extra em qualquer faixa.
#  Exiba o valor original, o desconto aplicado, o desconto VIP (se houver) e o valor final.
#
#==================================================================================
def desconto():
    vip = input("Bem vindo a nossa loja! O senhor é cliente Vip? (sim/nao): ")
    if (vip) in ("sim", "ss", "s", "lógico", "com certeza", "y", "yes"):
        continuar = True
    elif (vip) in ("não", "n", "nop", "not", "nem", "no", "nao"):
        continuar = False
    else:
        print("Resposta inválida paisão! ")
        continuar = None

    if continuar == True:
        valor1 = float(input("Ok senhor vip, qual foi o valor da compra? -> "))
        if valor1 <= 100.00:
            print("Infelizmente não tem como aplicar desconto na compra.")
            porcentagem = valor1
        elif valor1 >= 100.01 and valor1 <= 300.00:
            print("Você tem direito a 15% de desconto.")
            porcentagem = valor1 - (15 * valor1 / 100)
        elif valor1 >= 300.01 and valor1 <= 500.00:
            print("Você tem direito a 20% de desconto.")
            porcentagem = valor1 - (20 * valor1 / 100)
        elif valor1 >= 500.01:
            print("Você tem direito a 25% de desconto.")
            porcentagem = valor1 - (25 * valor1 / 100)
        final1 = valor1 - porcentagem
        print("================================================================================== ")
        print("=" * 70)
        print(f"Valor original        -> R$ {valor1:.2f}")
        print(f"Valor com desconto    -> R$ {porcentagem:.2f}")
        print(f"Você economizou       -> R$ {final1:.2f}")
        print("=" * 70)
        print("================================================================================== ")

    elif continuar == False:
        valor2 = float(input("Senhor me diga qual foi o valor da compra -> "))
        if valor2 <= 100.00:
            print("Infelizmente não tem como aplicar desconto na compra.")
            porcentagem2 = valor2
        elif valor2 >= 100.01 and valor2 <= 300.00:
            print("Você tem direito a 10% de desconto.")
            porcentagem2 = valor2 - (10 * valor2 / 100)
        elif valor2 >= 300.01 and valor2 <= 500.00:
            print("Você tem direito a 15% de desconto.")
            porcentagem2 = valor2 - (15 * valor2 / 100)
        elif valor2 >= 500.01:
            print("Você tem direito a 20% de desconto.")
            porcentagem2 = valor2 - (20 * valor2 / 100)
    final2 = valor2 - porcentagem2
    print("================================================================================== ")
    print("=" * 70)
    print(f"Valor original        -> R$ {valor2:.2f}")
    print(f"Valor com desconto    -> R$ {porcentagem2:.2f}")
    print(f"Você economizou       -> R$ {final2:.2f}")
    print("=" * 70)
    print("================================================================================== ")
desconto()