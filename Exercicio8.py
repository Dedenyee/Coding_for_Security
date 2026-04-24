# Exercício 8 — Inventário de Ativos com CRUD: Crie um programa que gerencie um inventário de ativos de rede usando uma lista de dicionários. 
# Cada ativo tem: nome, tipo (servidor/estação/switch/roteador), IP e status (ativo/inativo). 
# O programa deve ter menu com: [1] Cadastrar ativo, [2] Listar ativos, [3] Buscar por IP, [4] Alterar status, [5] Remover ativo, [6] Sair. 
# Trate com exceções entradas inválidas (ex: IP duplicado, ativo não encontrado). Use for para buscas e listagens.
# Sequência de teste:
# [1] Cadastrar: nome="SRV-DB01", tipo="servidor", ip="192.168.1.20" → "Cadastrado!"
# [1] Cadastrar: ip="192.168.1.10" → "Erro: IP já cadastrado!"
# [3] Buscar: ip="192.168.1.45"  → exibe dados do PC-RH03
# [3] Buscar: ip="8.8.8.8"       → "Ativo não encontrado"
# [4] Alterar: ip="192.168.1.1", novo status="ativo" → "Status atualizado!"
# [5] Remover: ip="192.168.1.45" → "Ativo removido!"
# [2] Listar → exibe todos os ativos formatados

# Dados iniciais:
ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
    {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
    {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
]
while True:
    print("="*50 + " Inventário de Ativos " + "="*50)
    print(" [1] Cadastrar ativo ")
    print(" [2] Listar ativos ")
    print(" [3] Buscar por IP ")
    print(" [4] Alterar status ")
    print(" [5] Remover ativo ")
    print(" [6] Sair ")
    print("="*122)
    opcao = int(input("Escolha uma opção -- "))
    



    def adicionar():
        if opcao == 1:
            print("Você escolheu cadastrar ativo! ")
            nome = str(input("NOME = "))
            tipo = str(input("TIPO = "))
            ip = (input("IP = "))
            for ativo in ativos:
                if ativo["ip"] == ip:
                    print("Erro: IP já cadastrado!")
                    return #Sai da fiunção quando encontra 2 ip's iguais.
                if ativo["nome"] == nome:
                    print("Erro: Nome já cadastrado!")
                    return
            print("Cadastrado! ")
            ativos.append({"nome": nome, "tipo": tipo, "ip": ip, "status": "ativo"})
    adicionar()

    def listar_ativos():
        if opcao == 2:
            print("Você escolheu listar ativos! ")
            print(f"Existem ({len(ativos)}) ativos")
            contagem = 0
            for ativo in ativos:
                contagem += 1
                print("="*50)
                print(f"Esse é o ({contagem}) ativo!")
                print(f"NOME = {ativo['nome']}")
                print(f"TIPO = {ativo['tipo']}")
                print(f"IP = {ativo['ip']}")
                print(f"STATUS = {ativo['status']}")
    listar_ativos()

    def Buscar_ip():
        if opcao == 3:
            print("Você escolheu buscar ativos! ")
            busca = input("Digite o ip do ativo - ")
            contagem = 0
            for ativo in ativos:
                if ativo["ip"] == busca:
                    contagem += 1
                    print("Ativo encontrado!")
                    print("="*50)
                    print(f"Nome: {ativo['nome']}")
                    print(f"Tipo: {ativo['tipo']}")
                    print(f"IP: {ativo['ip']}")
                    print(f"Status: {ativo['status']}")
            if contagem == 0:
                print("Ativo não encontrado!")
    Buscar_ip()
                
    def Alterar_Status():
        if opcao == 4:
            print("Você escolheu alterar status! ")
            busca = input("Digite o ip do ativo - ")
            contagem = 0
            for ativo in ativos:
                if ativo["ip"] == busca:
                    contagem += 1
                    print("Arquivo encontrado! ")
                    print("="*50)
                    print(f"O status do ativo é ({ativo['status']})")
                    novo_status = input("Digite o novo status (ativo/inativo) - ")
                    if novo_status not in ["ativo", "inativo"]:
                        print("Status inválido! Digite 'ativo' ou 'inativo'")
                    else:
                        ativo["status"] = novo_status
                        print(f"Status alterado com sucesso!\nNovo Status: ({ativo['status']})")
            if contagem == 0:
                print("Ativo não encontrado!")
    Alterar_Status()

    def Remover_Ativo():
        if opcao == 5:
            print("Você escolheu remover o ativo!")
            busca = input("Digite o ip do ativo - ")
            contagem = 0
            for i in range(len(ativos)):
                if ativos[i]["ip"] == busca:
                    contagem += 1
                    ativos.pop(i)
                    print(f"Ativo '{busca}' removido com sucesso!")
                    break
            if contagem == 0:
                print("Ativo não encontrado!")
    Remover_Ativo()

    if opcao == 6:
            print("Encerrando...")
            break
