# Exercício 8 — Detecção de anomalias: Use IsolationForest para sinalizar comportamentos anômalos em
# métricas de acesso. Liste quais amostras foram marcadas como anomalia.

import numpy as np
from sklearn.ensemble import IsolationForest

# [requisicoes_min, conexoes_simultaneas]
trafego = np.array([
    [100,5],[120,6],[110,5],[105,4],[50000,500],[109,5],[111,6],[45000,450],
])

detector = IsolationForest(contamination=0.25, random_state=42)
resultados = detector.fit_predict(trafego)

for i, (amostra, r) in enumerate(zip(trafego, resultados)):
    status = "ANOMALIA" if r == -1 else "Normal"
    print(f"Amostra {i}: {list(amostra)} -> {status}")