import os
import logging
from flask import Flask, request, jsonify
import mysql.connector
from markupsafe import escape
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

logging.basicConfig(filename="acessos.log", level=logging.INFO)


def db():
    return mysql.connector.connect(
        host=os.environ["MYSQL_HOST"],
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ["MYSQL_DATABASE"]
    )


@app.after_request
def headers_seguranca(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    logging.info(f"{request.method} {request.path} -> {resp.status_code}")
    return resp


@app.errorhandler(Exception)
def erro_generico(e):
    logging.error(f"Erro interno em {request.path}: {e}")
    return jsonify({"erro": "erro interno"}), 500


@app.route("/api/usuarios/buscar")
def buscar():
    nome = request.args.get("nome", "")
    conexao = db()
    cur = conexao.cursor(dictionary=True)
    cur.execute("SELECT id, nome, email FROM usuarios WHERE nome LIKE %s", (f"%{nome}%",))
    resultado = cur.fetchall()
    cur.close()
    conexao.close()
    return jsonify(resultado)


@app.route("/perfil")
def perfil():
    nome = request.args.get("u", "")
    return f"<h1>Bem-vindo, {escape(nome)}</h1>"


@app.route("/api/usuarios/<int:uid>", methods=["DELETE"])
def remover(uid):
    chave = request.headers.get("X-API-Key")
    if not chave:
        return jsonify({"erro": "não autenticado"}), 401

    conexao = db()
    cur = conexao.cursor(dictionary=True)
    cur.execute("SELECT nivel FROM usuarios WHERE api_key = %s", (chave,))
    solicitante = cur.fetchone()

    if solicitante is None:
        cur.close()
        conexao.close()
        return jsonify({"erro": "não autenticado"}), 401

    if solicitante["nivel"] < 5:
        cur.close()
        conexao.close()
        return jsonify({"erro": "acesso negado"}), 403

    cur.execute("DELETE FROM usuarios WHERE id = %s", (uid,))
    conexao.commit()
    cur.close()
    conexao.close()
    return jsonify({"removido": uid})


@app.route("/api/relatorio")
def relatorio():
    conexao = db()
    cur = conexao.cursor()
    try:
        cur.execute("SELECT * FROM tabela_inexistente")
        resultado = cur.fetchall()
    except mysql.connector.Error as erro:
        logging.error(f"Erro de banco em /api/relatorio: {erro}")
        return jsonify({"erro": "erro interno"}), 500
    finally:
        cur.close()
        conexao.close()
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5001)