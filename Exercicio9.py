#==================================================================================
#Atividade 09
# Jogo de Pedra, Papel, Tesoura, Lagarto, Spock: Crie o jogo expandido (da série The Big Bang Theory).
#  O usuário escolhe por número (1-5) e o computador escolhe aleatoriamente.
#  As regras são: Tesoura corta Papel, Papel cobre Pedra, Pedra esmaga Lagarto, Lagarto envenena Spock, Spock derrete Tesoura,
#  Tesoura decapita Lagarto, Lagarto come Papel, Papel refuta Spock, Spock vaporiza Pedra,
#  Pedra quebra Tesoura. Exiba as escolhas, quem ganhou e o motivo (ex: "Spock vaporiza Pedra").
#  Use o módulo random para a escolha do computador — importe com import random e use random.randint(1, 5) para gerar um número aleatório entre 1 e 5.
#
#==================================================================================
def predrapapel():
    import random
    opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura", 4: "Lagarto", 5: "Spock"}

    vence = {
        1: {3: "quebra",    4: "esmaga"},
        2: {1: "cobre",     5: "refuta"},
        3: {2: "corta",     4: "decapita"},
        4: {2: "come",      5: "envenena"},
        5: {1: "vaporiza",  3: "derrete"},
    }

    print("1-Pedra | 2-Papel | 3-Tesoura | 4-Lagarto | 5-Spock")
    jogador    = int(input("Sua escolha: "))
    computador = random.randint(1, 5)

    print(f" Você: {opcoes[jogador]}")
    print(f" Computador: {opcoes[computador]}")
    print("-" * 35)

    if jogador == computador:
        print("Empate!")
    elif computador in vence[jogador]:
        acao = vence[jogador][computador]
        print(f"{opcoes[jogador]} {acao} {opcoes[computador]} — Você venceu! ")
    else:
        acao = vence[computador][jogador]
        print(f"{opcoes[computador]} {acao} {opcoes[jogador]} — Computador venceu! ")
predrapapel()