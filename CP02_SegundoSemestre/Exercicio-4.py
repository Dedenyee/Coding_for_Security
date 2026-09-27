import os
from datetime import datetime
import mysql.connector
from mysql.connector import Error
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

cur.execute("DROP TABLE IF EXISTS usuarios_niveis")
cur.execute("""
    CREATE TABLE usuarios_niveis (
        id INT PRIMARY KEY,
        nome VARCHAR(100),
        email VARCHAR(150),
        nivel_acesso INT
    )
""")

usuarios = [(1, "ana", "ana@x.com", 5), (2, "bruno", "bruno@x.com", 2), (3, "caio", "caio@x.com", 1)]
cur.executemany("INSERT INTO usuarios_niveis (id, nome, email, nivel_acesso) VALUES (%s, %s, %s, %s)", usuarios)
conexao.commit()

db = MongoClient(os.environ["MONGO_URI"]).seguranca
auditoria = db.auditoria


def registrar_auditoria(quem, alvo, nivel_anterior, nivel_novo, resultado):
    auditoria.insert_one({
        "quem": quem,
        "alvo": alvo,
        "nivel_anterior": nivel_anterior,
        "nivel_novo": nivel_novo,
        "resultado": resultado,
        "timestamp": datetime.now()
    })


def buscar_usuario(id_usuario):
    cur.execute("SELECT * FROM usuarios_niveis WHERE id = %s", (id_usuario,))
    return cur.fetchone()


def alterar_nivel(admin_id, alvo_id, novo_nivel):
    admin = buscar_usuario(admin_id)
    alvo = buscar_usuario(alvo_id)

    if admin_id == alvo_id:
        registrar_auditoria(admin_id, alvo_id, None, novo_nivel, "RECUSADO")
        print(f"RECUSADO (auto-promoção).")
        return

    if admin is None or admin["nivel_acesso"] < 5:
        registrar_auditoria(admin_id, alvo_id, None, novo_nivel, "RECUSADO")
        print(f"RECUSADO (admin sem privilégio).")
        return

    if alvo is None:
        registrar_auditoria(admin_id, alvo_id, None, novo_nivel, "RECUSADO")
        print(f"RECUSADO (alvo inexistente).")
        return

    try:
        nivel_anterior = alvo["nivel_acesso"]
        cur.execute("UPDATE usuarios_niveis SET nivel_acesso = %s WHERE id = %s", (novo_nivel, alvo_id))
        conexao.commit()
        registrar_auditoria(admin_id, alvo_id, nivel_anterior, novo_nivel, "OK")
        print(f"OK. commit.")
    except Error:
        conexao.rollback()
        registrar_auditoria(admin_id, alvo_id, None, novo_nivel, "RECUSADO")
        print("RECUSADO (erro no banco). rollback.")


alterar_nivel(1, 2, 4)
alterar_nivel(2, 3, 5)
alterar_nivel(1, 1, 9)
alterar_nivel(1, 99, 3)

total_auditoria = auditoria.count_documents({})
total_recusado = auditoria.count_documents({"resultado": "RECUSADO"})
print(f"Trilha de auditoria ao final: {total_auditoria} documentos")
print(f"db.auditoria.count_documents({{'resultado':'RECUSADO'}}) -> {total_recusado}")

cur.close()
conexao.close()