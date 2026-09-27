import os
from flask import Flask, render_template_string
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

app = Flask(__name__)

db = MongoClient(os.environ["MONGO_URI"]).seguranca
colecao = db.incidentes_dashboard
colecao.delete_many({})

p1 = "<script>alert('xss1')</script>"
p2 = 'x" onerror="alert(\'xss2\')'

colecao.insert_many([
    {"titulo": p1, "ativo": "SRV-WEB01"},
    {"titulo": "Alerta de teste", "ativo": p2},
])

TEMPLATE_SEGURO = """
<table border="1">
{% for incidente in incidentes %}
    <tr>
        <td>{{ incidente.titulo }}</td>
        <td><img src="/icone.png" alt="{{ incidente.ativo }}"></td>
    </tr>
{% endfor %}
</table>
"""

TEMPLATE_INSEGURO = """
<table border="1">
{% for incidente in incidentes %}
    <tr>
        <td>{{ incidente.titulo | safe }}</td>
        <td><img src="/icone.png" alt="{{ incidente.ativo | safe }}"></td>
    </tr>
{% endfor %}
</table>
"""


@app.after_request
def headers_seguranca(resp):
    resp.headers["Content-Security-Policy"] = "default-src 'self'"
    return resp


@app.route("/dashboard")
def dashboard():
    incidentes = list(colecao.find({}, {"_id": 0}))
    return render_template_string(TEMPLATE_SEGURO, incidentes=incidentes)


@app.route("/dashboard-inseguro")
def dashboard_inseguro():
    incidentes = list(colecao.find({}, {"_id": 0}))
    return render_template_string(TEMPLATE_INSEGURO, incidentes=incidentes)


if __name__ == "__main__":
    app.run(debug=True, port=5000)