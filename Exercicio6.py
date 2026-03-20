#==================================================================================
#Atividade 06
# Verificador de Ano Bissexto e Dia da Semana: Crie um programa que peça uma data (dia, mês e ano, separados) e verifique:
# se o ano é bissexto (divisível por 4, exceto os divisíveis por 100, exceto os divisíveis por 400)
# , se o mês é válido (1-12), se o dia é válido para aquele mês (considere meses com 28/29, 30 ou 31 dias),
# e exiba a data formatada.
# Se qualquer valor for inválido, exiba o motivo.
#
#==================================================================================
def verificador ():
    dia = int(input("Que dia é hoje? -> "))
    mes = int(input("Que mes nós estamos? -> "))
    ano = int(input("Que ano nós estamos? -> "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        bissexto = True
    else:
        bissexto = False

    dias_no_mes = [0, 31, 29 if bissexto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    valido = True
    if mes < 1 or mes > 12:
        print(f"Mês inválido! O mês {mes} não existe. Escolha entre 1 e 12.")
        valido = False

    elif dia < 1 or dia > dias_no_mes[mes]:
        print(f"Dia inválido! O mês {mes} tem apenas {dias_no_mes[mes]} dias.")
        valido = False
    if valido:
        nomes_mes = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        tipo_ano = "bissexto" if bissexto else "não bissexto"

        print("=" * 50)
        print(f"Data formatada: {dia:02d}/{mes:02d}/{ano}")
        print(f"Mês: {nomes_mes[mes]}")
        print(f"O ano {ano} é {tipo_ano}.")
        print("=" * 50)
verificador()