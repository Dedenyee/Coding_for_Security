# Exercício 3 — Gerenciador de Lista de IPs: Crie um programa com menu interativo (usando while True) que gerencie uma lista de endereços IP. 
# O menu deve ter as opções: [1] Adicionar IP, [2] Remover IP, [3] Listar todos, [4] Buscar IP, [5] Sair. 
# Não permita IPs duplicados na lista. Na busca, informe se o IP foi encontrado e em qual posição. 
# Use break para sair do loop quando o usuário escolher a opção 5.
# Lista inicial para teste:
# ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

# Sequência de teste:
# [1] Adicionar: "192.168.1.10" → "IP adicionado!"
# [1] Adicionar: "10.0.0.5"    → "IP já existe na lista!"
# [4] Buscar: "172.16.0.3"     → "IP encontrado na posição 3"
# [4] Buscar: "8.8.8.8"        → "IP não encontrado"
# [2] Remover: "10.0.0.5"      → "IP removido!"
# [3] Listar                   → exibe todos os IPs numerados
# [5] Sair                     → "Encerrando..."
from time import sleep
def main():
    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]
    while True:
        print("="*50)
        print("[1] Adicionar IP     ")
        print("[2] Remover IP   ")
        print("[3] Listar todos IPs   ")
        print("[4] Buscar IP   ")
        print("[5] Sair     ")
        print("="*50)

        opcao = input("Escolha uma opção -- ")

        print(f"\n A opção escolhida foi [{opcao}]")

        if opcao == "1":
            print("Você escolheu [1] - Adicionar IP")
            adicionar = input("Digite o IP - ")
            if adicionar in ips:
                print("O IP já existe na lista! ")
                continue
            ips.append(adicionar)
            print(f"O IP adicionado foi {adicionar}")
            print("\nAguarde 5 Segundos para voltar ao menu.")
            sleep(5)

        elif opcao == "2":
            print("Você escolheu [2] - Remover IP")
            remover = input("Digite o IP - ")
            ips.remove(remover)
            print(f"O IP removido foi [{remover}]")
            print("\nAguarde 5 Segundos para voltar ao menu.")
            sleep(5)
        
        elif opcao == "3":
            print("Você escolheu [3] - Listar todos IPs")
            print(f"Existem ({len(ips)}) IPs cadastrados")
            contagem = 0
            for ip in ips:
                contagem += 1
                print(f"IP - {contagem:02d} - {ip}")
            print("\nAguarde 5 Segundos para voltar ao menu.")
            sleep(5)

        elif opcao == "4":
            print("Você escolheu [4] - Buscar IP IPs")
            buscar = input("Digite o IP no qual será buscado - ")
            if buscar in ips:
                print("IP foi encontrado! ")
            else:
                print("Não foi possível encontra o IP! ")
            print("\nAguarde 5 Segundos para voltar ao menu.")
            sleep(5)    

        elif opcao == "5":
            print("Você escolheu [5] - Sair")
            break
main()
