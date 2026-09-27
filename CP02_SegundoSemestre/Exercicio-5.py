import os
import mysql.connector
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

COLUNAS = {"data": "criado_em", "sev": "severidade", "ip": "ip_origem"}
ORDEM = {"asc": "ASC", "desc": "DESC"}


def get_db():
    return mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
    )


def preparar_tabela():
    conexao = get_db()
    cur = conexao.cursor()
    cur.execute("DROP TABLE IF EXISTS eventos")
    cur.execute("""
        CREATE TABLE eventos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            tipo VARCHAR(50),
            ip_origem VARCHAR(45),
            severidade ENUM('baixa', 'media', 'alta', 'critica'),
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    dados = [
        ("PORT_SCAN", "192.168.1.50", "alta"),
        ("BRUTE_FORCE", "185.220.101.1", "critica"),
        ("XSS", "45.33.32.156", "alta"),
        ("FAIL_LOGIN", "91.240.118.172", "media"),
        ("PORT_SCAN", "10.0.0.5", "baixa"),
        ("BRUTE_FORCE", "185.220.101.2", "critica"),
    ]
    cur.executemany(
        "INSERT INTO eventos (tipo, ip_origem, severidade) VALUES (%s, %s, %s)", dados
    )
    conexao.commit()
    cur.close()
    conexao.close()


@app.route("/api/eventos", methods=["GET"])
def listar_eventos():
    coluna_pedida = request.args.get("ordenar_por", "data")
    ordem_pedida = request.args.get("ordem", "asc")
    tamanho_texto = request.args.get("tamanho", "10")

    if coluna_pedida not in COLUNAS:
        return jsonify({"erro": "campo de ordenação inválido"}), 400

    if ordem_pedida not in ORDEM:
        return jsonify({"erro": "ordem inválida"}), 400

    if not tamanho_texto.isdigit():
        return jsonify({"erro": "tamanho deve ser inteiro"}), 400

    tamanho = int(tamanho_texto)
    if tamanho > 100:
        tamanho = 100

    coluna_sql = COLUNAS[coluna_pedida]
    ordem_sql = ORDEM[ordem_pedida]

    conexao = get_db()
    cur = conexao.cursor(dictionary=True)
    query = f"SELECT * FROM eventos ORDER BY {coluna_sql} {ordem_sql} LIMIT %s"
    cur.execute(query, (tamanho,))
    resultado = cur.fetchall()
    cur.close()
    conexao.close()

    return jsonify(resultado), 200


if __name__ == "__main__":
    preparar_tabela()
    app.run(debug=True, port=5000)