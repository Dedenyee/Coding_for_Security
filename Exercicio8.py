#==================================================================================
#Atividade 08
#Calculadora de Estacionamento: Crie um programa para calcular o valor do estacionamento.
#  A tarifa funciona assim: primeira hora custa R$ 10.00, horas adicionais custam R$ 5.00 cada (não tem meia hora — qualquer fração conta como hora cheia),
#  entre 22h e 6h cobra adicional noturno de 50% sobre o total,
#  e carros com placa terminando em número par ganham 10% de desconto às segundas-feiras.
#  O programa deve pedir: hora de entrada, hora de saída (formato 24h, apenas horas inteiras), 
# último número da placa e dia da semana. Exiba o detalhamento completo.
#==================================================================================
def estacionamento():
    entrada  = int(input("Hora de entrada (0-23) -> "))
    saida    = int(input("Hora de saída   (0-23) -> "))
    placa    = int(input("Último número da placa -> "))
    dia      = input("Dia da semana -> ").strip().lower()


    if not (0 <= entrada <= 23) or not (0 <= saida <= 23):
        print("Hora inválida! Use o formato 24h (0-23). ")
    elif not (0 <= placa <= 9):
        print("Dígito da placa inválido! Digite apenas o último número (0-9). ")
    else:

        if saida == entrada:
            horas = 1                     
        elif saida > entrada:
            horas = saida - entrada
        else:
            horas = (24 - entrada) + saida   

        if horas <= 1:
            tarifa_base = 10.00
        else:
            tarifa_base = 10.00 + (horas - 1) * 5.00

        total = tarifa_base
        adicional_noturno = 0
        desconto_segunda  = 0

        horas_percorridas = [(entrada + h) % 24 for h in range(horas)]
        periodo_noturno   = any(h >= 22 or h < 6 for h in horas_percorridas)
        if periodo_noturno:
            adicional_noturno = total * 0.50
            total += adicional_noturno
        if dia == "segunda" and placa % 2 == 0:
            desconto_segunda = total * 0.10
            total -= desconto_segunda
        nomes_dia = {
            "segunda": "Segunda-feira", "terca": "Terça-feira",
            "quarta": "Quarta-feira",   "quinta": "Quinta-feira",
            "sexta": "Sexta-feira",     "sabado": "Sábado",
            "domingo": "Domingo"
        }
        nome_dia = nomes_dia.get(dia, dia.capitalize())

        print("=" * 40)
        print("      === Estacionamento ===")
        print("=" * 40)
        print(f"Dia ->          {nome_dia}")
        print(f"Entrada ->      {entrada:02d}h  |  Saída: {saida:02d}h")
        print(f"Permanência ->  {horas} hora(s)")
        print(f"Placa final ->  {placa} ({'par' if placa % 2 == 0 else 'ímpar'})")
        print("-" * 40)
        print(f"Tarifa base ->             R$ {tarifa_base:6.2f}")

        if adicional_noturno > 0:
            print(f"Adicional noturno (50%) -> R$ {adicional_noturno:6.2f}")
        if desconto_segunda > 0:
            print(f"Desconto segunda (10%) -> -R$ {desconto_segunda:6.2f}")

        print("=" * 40)
        print(f"TOTAL:                   R$ {total:6.2f}")
        print("=" * 40)
estacionamento()