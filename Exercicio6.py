# Exercício 6 — Blacklist de IPs com Sets: Crie um programa que compare dois sets: um com IPs que acessaram o servidor e outro com uma blacklist de IPs maliciosos. 
# Usando operações de conjuntos, descubra e exiba: quais IPs maliciosos foram detectados (interseção), quais IPs são seguros (diferença), 
# quais IPs da blacklist não apareceram (diferença inversa) 
# e o total de IPs únicos considerando ambas as listas (união). Exiba os resultados formatados.

# Saída esperada:
# === Relatório de Segurança ===
# IPs maliciosos detectados (3):
#   - 185.220.101.1
#   - 45.33.32.156
#   - 91.240.118.172
#
# IPs seguros (5):
#   - 192.168.1.10
#   - 10.0.0.5
#   - 172.16.0.3
#   - 192.168.1.20
#   - 10.0.0.12
#
# IPs da blacklist não detectados (2):
#   - 23.94.5.100
#   - 104.244.72.115
#
# Total de IPs únicos: 10
def main():
    acessos = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3","192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}
    blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172","23.94.5.100", "104.244.72.115"}

    ameaças = acessos & blacklist
    seguros = acessos - blacklist
    ndetectados = blacklist - acessos
    total = blacklist | acessos
    print("="*20 + "Relatório de Segurança" + "="*20)
    print(f"IPs maliciosos detectados ({len(ameaças)})")
    for ip in ameaças:
        print(f"- {ip}")

    print(f"Os IPs Seguros encontrados foram ({len(seguros)})")
    for ip in seguros:
        print(f"- {ip}")
    
    print(f"Os IPs nao encontrados foram ({len(ndetectados)})")
    for ip in ndetectados:
        print(f"- {ip}")

    print(f"Total de IPs únicos ({len(total)})")
main()