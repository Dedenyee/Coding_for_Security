import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

db = MongoClient(os.environ["MONGO_URI"]).seguranca
colecao = db.eventos
colecao.drop()

agora = datetime.now()

eventos = []
for i in range(200):
    hora_aleatoria = random.randint(0, 23)
    minuto_aleatorio = random.randint(0, 59)
    timestamp = agora - timedelta(hours=(23 - hora_aleatoria), minutes=(59 - minuto_aleatorio))
    eventos.append({
        "tipo": "FAIL",
        "timestamp": timestamp
    })

colecao.insert_many(eventos)

colecao.create_index("timestamp", expireAfterSeconds=604800)

pipeline = [
    {"$match": {"tipo": "FAIL"}},
    {"$group": {"_id": {"$hour": "$timestamp"}, "total": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
]

resultado = list(colecao.aggregate(pipeline))

print("=== Falhas por hora (últimas 24h) ===")
pico_hora = None
pico_total = 0
for item in resultado:
    hora = item["_id"]
    total = item["total"]
    barra = "█" * total
    print(f"{hora:02d}h | {barra} {total}")
    if total > pico_total:
        pico_total = total
        pico_hora = hora

print(f"Hora de pico: {pico_hora:02d}h ({pico_total} falhas)")
print("Índice TTL ativo: eventos com mais de 7 dias serão removidos automaticamente.")