import os
import mysql.connector
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_db():
    return mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
    )


def preparar_tabelas():
    conexao = get_db()
    cur = conexao.cursor()
    cur.execute("DROP TABLE IF EXISTS incidentes")
    cur.execute("DROP TABLE IF EXISTS analistas")
    cur.execute("""
        CREATE TABLE analistas (
            id INT PRIMARY KEY,
            nome VARCHAR(100),
            api_key VARCHAR(50) UNIQUE,
            nivel INT
        )
    """)
    cur.execute("""
        CREATE TABLE incidentes (
            id INT PRIMARY KEY,
            dono_id INT,
            titulo VARCHAR(150),
            severidade VARCHAR(20),
            FOREIGN KEY (dono_id) REFERENCES analistas(id)
        )
    """)
    analistas = [(1, "ana", "key-ana-001", 5), (2, "bruno", "key-bruno-002", 2)]
    incidentes = [(1, 1, "Brute force SSH", "critica"), (2, 2, "Phishing no RH", "media")]
    cur.executemany("INSERT INTO analistas (id, nome, api_key, nivel) VALUES (%s, %s, %s, %s)", analistas)
    cur.executemany("INSERT INTO incidentes (id, dono_id, titulo, severidade) VALUES (%s, %s, %s, %s)", incidentes)
    conexao.commit()
    cur.close()
    conexao.close()


def autenticar():
    chave = request.headers.get("X-API-Key")
    if not chave:
        return None
    conexao = get_db()
    cur = conexao.cursor(dictionary=True)
    cur.execute("SELECT * FROM analistas WHERE api_key = %s", (chave,))
    analista = cur.fetchone()
    cur.close()
    conexao.close()
    return analista


@app.route("/api/incidentes", methods=["GET"])
def listar_incidentes():
    analista = autenticar()
    if analista is None:
        return jsonify({"erro": "não autenticado"}), 401

    conexao = get_db()
    cur = conexao.cursor(dictionary=True)
    cur.execute("SELECT * FROM incidentes WHERE dono_id = %s", (analista["id"],))
    resultado = cur.fetchall()
    cur.close()
    conexao.close()
    return jsonify(resultado), 200


@app.route("/api/incidentes/<int:id>", methods=["GET"])
def obter_incidente(id):
    analista = autenticar()
    if analista is None:
        return jsonify({"erro": "não autenticado"}), 401

    conexao = get_db()
    cur = conexao.cursor(dictionary=True)
    cur.execute("SELECT * FROM incidentes WHERE id = %s", (id,))
    incidente = cur.fetchone()
    cur.close()
    conexao.close()

    if incidente is None:
        return jsonify({"erro": "não encontrado"}), 404

    if incidente["dono_id"] != analista["id"]:
        return jsonify({"erro": "acesso negado"}), 403

    return jsonify(incidente), 200


@app.route("/api/incidentes/<int:id>", methods=["DELETE"])
def remover_incidente(id):
    analista = autenticar()
    if analista is None:
        return jsonify({"erro": "não autenticado"}), 401

    if analista["nivel"] < 5:
        return jsonify({"erro": "acesso negado"}), 403

    conexao = get_db()
    cur = conexao.cursor()
    cur.execute("SELECT id FROM incidentes WHERE id = %s", (id,))
    if cur.fetchone() is None:
        cur.close()
        conexao.close()
        return jsonify({"erro": "não encontrado"}), 404

    cur.execute("DELETE FROM incidentes WHERE id = %s", (id,))
    conexao.commit()
    cur.close()
    conexao.close()
    return jsonify({"mensagem": "removido"}), 200


if __name__ == "__main__":
    preparar_tabelas()
    app.run(debug=True, port=5000)