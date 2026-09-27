import os
from datetime import datetime
import numpy as np
from flask import Flask, jsonify, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

db = MongoClient(os.environ["MONGO_URI"]).seguranca
previsoes = db.previsoes

X = np.array([
    [0, 1, 1200, 9],   [1, 1, 800, 10],   [0, 2, 1500, 14],  [12, 7, 90000, 3],
    [10, 6, 85000, 2], [0, 1, 900, 11],   [15, 8, 95000, 4], [1, 2, 1100, 15],
    [0, 1, 700, 13],   [14, 9, 92000, 1],
])
y = np.array([0, 0, 0, 1, 1, 0, 1, 0, 0, 1])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)


@app.route("/api/triagem", methods=["POST"])
def triagem():
    dados = request.get_json(silent=True)

    if not dados or "features" not in dados:
        return jsonify({"erro": "campo 'features' obrigatório"}), 400

    features = dados["features"]

    if len(features) != 4:
        return jsonify({"erro": f"esperadas 4 features, recebidas {len(features)}"}), 400

    for valor in features:
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            return jsonify({"erro": "features devem ser numéricas"}), 400

    entrada = np.array([features])
    predicao = modelo.predict(entrada)[0]
    probabilidades = modelo.predict_proba(entrada)[0]
    confianca = round(float(max(probabilidades)), 2)
    risco = "alto" if predicao == 1 else "baixo"

    previsoes.insert_one({
        "entrada": features,
        "saida": risco,
        "confianca": confianca,
        "timestamp": datetime.now()
    })

    return jsonify({"risco": risco, "confianca": confianca}), 200


@app.route("/api/modelo/metricas", methods=["GET"])
def metricas():
    previsoes_teste = modelo.predict(X_test)
    matriz = confusion_matrix(y_test, previsoes_teste)
    precisao = precision_score(y_test, previsoes_teste)
    recall = recall_score(y_test, previsoes_teste)
    f1 = f1_score(y_test, previsoes_teste)

    return jsonify({
        "precisao": round(precisao, 2),
        "recall": round(recall, 2),
        "f1": round(f1, 2),
        "matriz": matriz.tolist(),
        "aviso": "acurácia omitida de propósito: com poucas amostras de risco alto, ela mascararia falhas em detectar justamente os casos que mais importam"
    }), 200