# Exercício 7 — Classificador de tráfego: Treine um RandomForestClassifier para distinguir tráfego normal de malicioso.
# Divida treino/teste (test_size=0.3, random_state=42), reporte a acurácia e classifique um caso novo.

# Saída esperada:
# Acurácia no teste: (imprime o valor, ex. 1.00)
# Caso novo [58000,4444,16.0] -> Malicioso (1)

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Features: [bytes, porta, duracao]
X = np.array([
    [500,80,0.1],[1200,80,0.5],[64,22,0.02],[64000,4444,10.0],[45000,8080,15.0],
    [60000,31337,20.0],[800,443,0.3],[300,53,0.05],[55000,9999,18.0],[200,25,0.2],
])
y = np.array([0,0,0,1,1,1,0,0,1,0])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
print(f"Acurácia no teste: {accuracy_score(y_test, previsoes):.2f}")

caso_novo = [[58000, 4444, 16.0]]
predicao = modelo.predict(caso_novo)[0]
resultado = "Malicioso (1)" if predicao == 1 else "Normal (0)"
print(f"Caso novo {caso_novo[0]} -> {resultado}")