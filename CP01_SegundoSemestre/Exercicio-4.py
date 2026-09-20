# Exercício 4 — Query parametrizada (defesa contra SQL Injection): Escreva duas funções de busca por nome de usuário: uma insegura (concatenando) e uma segura (parametrizada).
# Demonstre com a entrada ' OR '1'='1 que a insegura vaza todos os registros e a segura não retorna nada.
usuarios = [("admin","admin@x.com"), ("ana","ana@x.com"), ("bruno","bruno@x.com")]
entrada = "' OR '1'='1"

# Saída esperada:
# [INSEGURO] entrada=' OR '1'='1  -> 3 usuários (VAZAMENTO)
# [SEGURO]   entrada=' OR '1'='1  -> 0 usuários (defesa OK)

import mysql.connector
from mysql.connector import Error

conexao = mysql.connector.connect(
    host="localhost", user="root",
    password="senha", database="seguranca"
)
cur = conexao.cursor()

cur.execute("DROP TABLE IF EXISTS usuarios_sqli")
cur.execute("""
    CREATE TABLE usuarios_sqli (
        nome VARCHAR(100),
        email VARCHAR(150)
    )
""")

cur.executemany("INSERT INTO usuarios_sqli (nome, email) VALUES (%s, %s)", usuarios)
conexao.commit()

def buscar_inseguro(nome):
    query = f"SELECT * FROM usuarios_sqli WHERE nome = '{nome}'"
    print(f"[Query executada] {query}")
    cur.execute(query)
    return cur.fetchall()

def buscar_seguro(nome):
    query = "SELECT * FROM usuarios_sqli WHERE nome = %s"
    print(f"[Query executada] {query} | parâmetro: {nome!r}")
    cur.execute(query, (nome,))
    return cur.fetchall()

entrada_maliciosa = "' OR '1'='1"

resultado_inseguro = buscar_inseguro(entrada_maliciosa)
print(f"[INSEGURO] entrada={entrada_maliciosa}  -> {len(resultado_inseguro)} usuários (VAZAMENTO)")

resultado_seguro = buscar_seguro(entrada_maliciosa)
print(f"[SEGURO]   entrada={entrada_maliciosa}  -> {len(resultado_seguro)} usuários (defesa OK)")

cur.close()
conexao.close()