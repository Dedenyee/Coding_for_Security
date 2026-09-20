# Exercício 5 — Transação com rollback: Simule uma transferência entre duas "contas" no MySQL (debita de uma, credita em outra).
# Se a segunda operação falhar (ex: conta inexistente), faça rollback e prove que o saldo da primeira conta não mudou.

# Tabela: contas(id, titular, saldo)
contas = [(1, "Alice", 1000), (2, "Bob", 500)]

# Cenário de teste:
# Transferir 200 de Alice para Bob      -> commit, saldos: Alice=800, Bob=700
# Transferir 100 de Alice para conta 99 -> rollback, saldos INALTERADOS: Alice=800

# Saída esperada:
# Transferência 1 OK. Alice=800, Bob=700
# Transferência 2 FALHOU (conta destino inexistente). Rollback. Alice=800

import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host="localhost", user="root",
        password="senha", database="seguranca"
    )
    cur = conexao.cursor()

    cur.execute("DROP TABLE IF EXISTS contas")
    cur.execute("""
        CREATE TABLE contas (
            id INT PRIMARY KEY,
            titular VARCHAR(100),
            saldo DECIMAL(10, 2)
        )
    """)

    contas = [(1, "Alice", 1000), (2, "Bob", 500)]
    cur.executemany("INSERT INTO contas (id, titular, saldo) VALUES (%s, %s, %s)", contas)
    conexao.commit()

    def transferir(id_origem, id_destino, valor):
        try:
            cur.execute("SELECT id FROM contas WHERE id = %s", (id_destino,))
            if cur.fetchone() is None:
                raise ValueError(f"Conta destino {id_destino} não existe")

            cur.execute("UPDATE contas SET saldo = saldo - %s WHERE id = %s", (valor, id_origem))
            cur.execute("UPDATE contas SET saldo = saldo + %s WHERE id = %s", (valor, id_destino))
            conexao.commit()
            return True
        except (Error, ValueError) as e:
            conexao.rollback()
            print(f"Transferência FALHOU ({e}). Rollback.")
            return False

    def mostrar_saldo(id_conta):
        cur.execute("SELECT titular, saldo FROM contas WHERE id = %s", (id_conta,))
        titular, saldo = cur.fetchone()
        return titular, saldo

    # Transferência 1: Alice -> Bob, 200
    if transferir(1, 2, 200):
        _, saldo_alice = mostrar_saldo(1)
        _, saldo_bob = mostrar_saldo(2)
        print(f"Transferência 1 OK. Alice={saldo_alice}, Bob={saldo_bob}")

    # Transferência 2: Alice -> conta 99 (não existe)
    if not transferir(1, 99, 100):
        _, saldo_alice = mostrar_saldo(1)
        print(f"Transferência 2 FALHOU (conta destino inexistente). Rollback. Alice={saldo_alice}")

except Error as e:
    print(f"Erro de conexão: {e}")
finally:
    if 'conexao' in locals() and conexao.is_connected():
        cur.close()
        conexao.close()
