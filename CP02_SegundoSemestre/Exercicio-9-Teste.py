import time
import requests

BASE = "http://127.0.0.1:5000"

for _ in range(5):
    requests.get(f"{BASE}/api/dados", headers={"X-Forwarded-For": "192.168.1.10"})
    time.sleep(1)

for i in range(60):
    if i < 40:
        requests.get(f"{BASE}/api/rota-inexistente", headers={"X-Forwarded-For": "185.220.101.1"})
    else:
        requests.get(f"{BASE}/api/dados", headers={"X-Forwarded-For": "185.220.101.1"})

analise = requests.get(f"{BASE}/api/analisar-acessos").json()

print("=== Análise de acessos ===")
for item in analise:
    print(f"{item['ip']:15s} [{item['req_por_minuto']:6.1f} req/min | 4xx {item['taxa_4xx']:.2f} | {item['rotas_distintas']} rotas] -> {item['status']}")

resposta_final = requests.get(f"{BASE}/api/dados", headers={"X-Forwarded-For": "185.220.101.1"})
print(f"Próxima requisição de 185.220.101.1 -> {resposta_final.status_code} {resposta_final.json()}")
print(f"Retry-After: {resposta_final.headers.get('Retry-After')}")
