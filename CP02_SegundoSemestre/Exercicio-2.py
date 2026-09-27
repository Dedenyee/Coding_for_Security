import os
import mysql.connector
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

conexao = mysql.connector.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"]
)
cur = conexao.cursor(dictionary=True)

cur.execute("DROP TABLE IF EXISTS alertas")
cur.execute("DROP TABLE IF EXISTS ativos")

cur.execute("""
    CREATE TABLE ativos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        ip VARCHAR(45) UNIQUE,
        criticidade ENUM('baixa', 'media', 'alta')
    )
""")

cur.execute("""
    CREATE TABLE alertas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ativo_id INT,
        tipo VARCHAR(50),
        severidade VARCHAR(20),
        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ativo_id) REFERENCES ativos(id)
    )
""")

ativos = [(1, "SRV-WEB01", "192.168.1.10", "alta"), (2, "PC-RH03", "192.168.1.45", "baixa")]
cur.executemany("INSERT INTO ativos (id, nome, ip, criticidade) VALUES (%s, %s, %s, %s)", ativos)

alertas = [(1, 1, "BRUTE_FORCE", "critica"), (2, 1, "PORT_SCAN", "alta"), (3, 2, "XSS", "media")]
cur.executemany("INSERT INTO alertas (id, ativo_id, tipo, severidade) VALUES (%s, %s, %s, %s)", alertas)
conexao.commit()

cur.execute("""
    SELECT alertas.tipo, alertas.severidade,
           ativos.nome, ativos.ip, ativos.criticidade
    FROM alertas
    JOIN ativos ON alertas.ativo_id = ativos.id
""")
linhas = cur.fetchall()

db = MongoClient(os.environ["MONGO_URI"]).seguranca
colecao = db.alertas
colecao.delete_many({})

documentos = []
for linha in linhas:
    documentos.append({
        "tipo": linha["tipo"],
        "severidade": linha["severidade"],
        "ativo": {
            "nome": linha["nome"],
            "ip": linha["ip"],
            "criticidade": linha["criticidade"]
        }
    })

colecao.insert_many(documentos)

total_mysql = len(linhas)
total_mongo = colecao.count_documents({})
status = "MIGRAÇÃO ÍNTEGRA" if total_mysql == total_mongo else "DIVERGÊNCIA"
print(f"MySQL: {total_mysql} alertas | MongoDB: {total_mongo} documentos -> {status}")

resultado_sem_join = colecao.find({"ativo.criticidade": "alta"})
print(f"Consulta sem JOIN: db.alertas.find({{'ativo.criticidade': 'alta'}}) -> {len(list(resultado_sem_join))} documentos")

cur.close()
conexao.close()