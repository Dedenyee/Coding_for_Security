# Exercício 6 — Índice e desempenho: Crie uma coleção com 1000 eventos gerados em laço, crie um índice no
# campo ip e demonstre uma consulta por IP. Explique por que o índice importa quando a coleção cresce.

# Dica: gere eventos com um for e insert_many; use create_index("ip").
# Consulte um IP específico e conte quantos eventos retornaram.

# Saída esperada (exemplo):
# 1000 eventos inseridos.
# Índice criado em 'ip'.
# Eventos do IP 185.220.101.1: 250
# Comentário: sem índice a busca seria O(n) (varre tudo); com índice ~O(log n).

import random
from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017/").seguranca
colecao = db.eventos_indexados
colecao.drop()

ips_possiveis = ["185.220.101.1", "91.240.118.172", "45.33.32.156", "192.168.1.10", "10.0.0.5"]

eventos = []
for i in range(1000):
    eventos.append({
        "tipo": random.choice(["FAIL", "OK"]),
        "ip": random.choice(ips_possiveis)
    })

colecao.insert_many(eventos)
print(f"{colecao.count_documents({})} eventos inseridos.")

colecao.create_index("ip")
print("Índice criado em 'ip'.")

ip_alvo = "185.220.101.1"
total = colecao.count_documents({"ip": ip_alvo})
print(f"Eventos do IP {ip_alvo}: {total}")
