# Exercício 10 (Desafio) — Mini-pipeline SIEM: log -> MongoDB -> ML: Leia o auth.log, normalize cada linha
# em um documento, insira no MongoDB, agregue a contagem de FAILs por IP, rotule como suspeito (>=5 falhas)
# e treine um classificador para prever o rótulo de um IP novo.

from pymongo import MongoClient
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def parsear_linha(linha):
    partes = linha.strip().split()
    data, hora, tipo = partes[0], partes[1], partes[2]
    usuario = partes[3].split("=")[1]
    ip = partes[4].split("=")[1]
    return {
        "timestamp": f"{data} {hora}",
        "tipo": tipo,
        "usuario": usuario,
        "ip": ip
    }

eventos = []
with open("auth.log", "r") as arquivo:
    for linha in arquivo:
        eventos.append(parsear_linha(linha))

db = MongoClient("mongodb://localhost:27017/").seguranca
colecao = db.auth_log
colecao.delete_many({})
colecao.insert_many(eventos)
print(f"Eventos inseridos no MongoDB: {colecao.count_documents({})}")

pipeline = [
    {"$match": {"tipo": "FAIL"}},
    {"$group": {"_id": "$ip", "total": {"$sum": 1}}},
    {"$sort": {"total": -1}}
]
contagem_por_ip = list(colecao.aggregate(pipeline))
for item in contagem_por_ip:
    print(f"{item['_id']} -> {item['total']} FAILs")

X = []
y = []
for item in contagem_por_ip:
    qtd_fails = item["total"]
    suspeito = 1 if qtd_fails >= 5 else 0
    X.append([qtd_fails])
    y.append(suspeito)

X = np.array(X)
y = np.array(y)
print(f"Dataset de treino: {X.tolist()} rótulos {y.tolist()}")

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X, y)

ip_novo = [[8]]
predicao = modelo.predict(ip_novo)[0]
resultado = "Suspeito (1)" if predicao == 1 else "Normal (0)"
print(f"Previsão para IP com 8 falhas -> {resultado}")