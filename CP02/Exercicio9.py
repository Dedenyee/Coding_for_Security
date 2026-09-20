# Exercício 9 — Analisador de Logs de Segurança: Crie um programa que analise uma lista de logs (strings), 
# extraindo informações com manipulação de   strings e armazenando em dicionários. 
# Para cada log: extraia o nível (INFO/WARNING/ERROR), o IP de origem e a mensagem. 
# Conte os eventos por nível, identifique o IP com mais erros e gere um relatório. 
# Use for, dicionários e try/except para tratar logs malformados.

# Saída esperada:
# === Relatório de Logs ===
# INFO:    3 eventos
# WARNING: 3 eventos
# ERROR:   4 eventos
# Logs malformados: 1
#
# IP com mais erros: 185.220.101.1 (3 erros)
#
# Detalhamento de erros:
#   185.220.101.1 → 3 erros
#   10.0.0.5      → 1 erro
logs = [
    "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
    "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
    "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
    "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
    "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
    "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
    "log malformado sem formato correto",
    "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
    "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
    "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
    "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
]

avisos = {"ERROR": 0, "WARNING": 0, "INFO": 0}
malformados = 0
erros_porIP = {}

print("="*20 + " Relatório de Logs " + "="*20)

for log in logs:
    try:
        palavra = ""

        #EXtração do nível (WAARNING, ERROR, INFO)
        contador = 0
        lendo_nivel = False
        nivel = ""

        for letra in log:
            if letra == "[":
                contador += 1
                if contador == 2:
                    lendo_nivel = True
                    nivel = ""
                    continue

            elif letra == "]" and lendo_nivel:
                break

            elif lendo_nivel:
                nivel += letra

        #Extração do IP
        ip = "" 
        lendo_ip = False

        for i in range(len(log)):
            if (i + 3 < len(log) and
                log[i] == "I" and log[i+1] == "P" and log[i+2] == ":" and log[i+3] == " "):
                
                lendo_ip = True
                continue

            if lendo_ip:
                ip += log[i]

        #Validação
        if nivel == "" or ip == "":
            raise ValueError()

        #Contagem
        avisos[nivel] += 1

        if nivel == "ERROR":
            if ip in erros_porIP:
                erros_porIP[ip] += 1
            else:
                erros_porIP[ip] = 1

    except:
        malformados += 1


#Resultados
ip_mais_erros = max(erros_porIP, key=erros_porIP.get)

print(f"INFO:    {avisos['INFO']} eventos")
print(f"WARNING: {avisos['WARNING']} eventos")
print(f"ERROR:   {avisos['ERROR']} eventos")
print(f"Logs malformados: {malformados}\n")

print(f"IP com mais erros: {ip_mais_erros} ({erros_porIP[ip_mais_erros]} erros)\n")

print("Detalhamento de erros:")
for ip, qtd in erros_porIP.items():
    print(f"  {ip} → {qtd} erros")
