# Exercício 2 — CRUD com PyMongo: Conecte ao MongoDB e implemente as quatro operações sobre uma coleção vulnerabilidades.
# Insira, busque por severidade, atualize corrigida para True e delete por cve_id.

vulns = [
    {"cve_id": "CVE-2024-001", "tipo": "SQL Injection", "severidade": "Alta",  "corrigida": False},
    {"cve_id": "CVE-2024-002", "tipo": "XSS",           "severidade": "Media", "corrigida": True},
    {"cve_id": "CVE-2024-003", "tipo": "Path Traversal","severidade": "Critica","corrigida": False},
]

# Saída esperada:
# Buscar severidade='Alta'      -> CVE-2024-001: SQL Injection
# update corrigida=True em 001  -> "1 documento modificado"
# count corrigida=False         -> 1 (só a CVE-2024-003 restou aberta)
from pymongo import MongoClient

db = MongoClient("mongodb://localhost:27017/").seguranca
colecao = db.vulnerabilidades
colecao.delete_many({})

# Insert
resultado = colecao.insert_many(vulns)
print(f"{len(resultado.inserted_ids)} documentos inseridos")

# Read
resultado = colecao.find_one({"severidade": "Alta"})
print(f"{resultado['cve_id']}: {resultado['tipo']}")

# Update
resultado = colecao.update_one(
    {"cve_id": "CVE-2024-001"},          # filtro: qual documento encontrar
    {"$set": {"corrigida": True}}        # o que mudar nele
)
print(f"{resultado.modified_count} documento modificado")

# Contagem
total_abertas = colecao.count_documents({"corrigida": False})
print(f"Vulnerabilidades ainda abertas: {total_abertas}")

# Delete
resultado = colecao.delete_one({"cve_id": "CVE-2024-002"})
print(f"{resultado.deleted_count} documento removido")

