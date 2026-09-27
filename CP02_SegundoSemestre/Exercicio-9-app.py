import os
from datetime import datetime
import numpy as np
from flask import Flask, jsonify, request, g
from sklearn.ensemble import IsolationForest
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

db = MongoClient(os.environ["MONGO_URI"]).seguranca
acessos = db.acessos
acessos.delete_many({})

BLOQUEADOS = set()


def obter_ip():
    return request.headers.get("X-Forwarded-For", request.remote_addr)


@app.before_request
def registrar_acesso():
    ip = obter_ip()

    if ip in BLOQUEADOS:
        return jsonify({"erro": "muitas requisições"}), 429, {"Retry-After": "60"}

    documento = {
        "ip": ip,
        "rota": request.path,
        "metodo": request.method,
        "timestamp": datetime.now()
    }
    resultado = acessos.insert_one(documento)
    g.acesso_id = resultado.inserted_id


@app.after_request
def completar_acesso(resp):
    if hasattr(g, "acesso_id"):
        acessos.update_one({"_id": g.acesso_id}, {"$set": {"status": resp.status_code}})
    return resp


@app.route("/api/dados")
def dados():
    return jsonify({"mensagem": "ok"}), 200


@app.route("/api/analisar-acessos")
def analisar_acessos():
    pipeline = [
        {"$group": {
            "_id": "$ip",
            "total": {"$sum": 1},
            "erros": {"$sum": {"$cond": [{"$gte": ["$status", 400]}, 1, 0]}},
            "rotas": {"$addToSet": "$rota"},
            "primeiro": {"$min": "$timestamp"},
            "ultimo": {"$max": "$timestamp"}
        }}
    ]

    grupos = list(acessos.aggregate(pipeline))

    ips = []
    features = []
    for grupo in grupos:
        duracao_min = max((grupo["ultimo"] - grupo["primeiro"]).total_seconds() / 60, 1 / 60)
        req_por_minuto = grupo["total"] / duracao_min
        taxa_4xx = grupo["erros"] / grupo["total"]
        rotas_distintas = len(grupo["rotas"])
        ips.append(grupo["_id"])
        features.append([req_por_minuto, taxa_4xx, rotas_distintas])

    features = np.array(features)
    detector = IsolationForest(contamination=0.2, random_state=42)
    resultados = detector.fit_predict(features)

    relatorio = []
    for ip, feat, r in zip(ips, features, resultados):
        status = "ANOMALIA" if r == -1 else "normal"
        if r == -1:
            BLOQUEADOS.add(ip)
        relatorio.append({
            "ip": ip,
            "req_por_minuto": round(feat[0], 2),
            "taxa_4xx": round(feat[1], 2),
            "rotas_distintas": int(feat[2]),
            "status": status
        })

    return jsonify(relatorio), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)