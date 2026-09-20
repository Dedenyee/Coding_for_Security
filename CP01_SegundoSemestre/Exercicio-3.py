# Exercício 3 — Agregação: Top IPs: Insira uma lista de eventos no MongoDB e use um aggregation pipeline para retornar os 3 IPs com mais eventos do tipo FAIL,
# ordenados de forma decrescente.

# Dica: pipeline = [{"$match":{"tipo":"FAIL"}}, {"$group":{"_id":"$ip","total":{"$sum":1}}},
#                   {"$sort":{"total":-1}}, {"$limit":3}]

# Saída esperada:
# 185.220.101.1 -> 4
# 91.240.118.172 -> 2
# 45.33.32.156  -> 1

from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017/").seguranca
colecao = db.eventos
colecao.delete_many({}) 

eventos = [
    {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "185.220.101.1"},
    {"tipo": "OK",   "ip": "192.168.1.10"},  {"tipo": "FAIL", "ip": "91.240.118.172"},
    {"tipo": "FAIL", "ip": "185.220.101.1"}, {"tipo": "FAIL", "ip": "91.240.118.172"},
    {"tipo": "FAIL", "ip": "45.33.32.156"},  {"tipo": "FAIL", "ip": "185.220.101.1"},
]

colecao.insert_many(eventos)

pipeline = [
    {"$match": {"tipo": "FAIL"}},
    {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}},
    {"$limit": 3}
]

resultado = colecao.aggregate(pipeline)

for doc in resultado:
    print(f"{doc['_id']} -> {doc['total']}")