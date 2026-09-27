def recomendar(perfil):
    if perfil["precisa_acid"]:
        banco = "MySQL"
        cap = "CP"
        justificativa = "autenticar errado é pior que ficar fora do ar"
        risco_owasp = "A07"
    elif perfil["escala_horizontal"] and perfil["tolera_atraso_de_consistencia"]:
        banco = "MongoDB"
        cap = "AP"
        justificativa = "perder 1s de log < parar de aceitar log"
        risco_owasp = "A09"
    else:
        banco = "MongoDB"
        cap = "CP"
        justificativa = "auditoria divergente não vale como prova"
        risco_owasp = "A08"

    if perfil["dado_sensivel"] and risco_owasp != "A07":
        risco_owasp = "A04"

    return {
        "banco": banco,
        "cap": cap,
        "justificativa": justificativa,
        "risco_owasp": risco_owasp
    }


perfis = {
    "credenciais_do_SOC":      {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
    "telemetria_de_sensores":  {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":False},
    "trilha_de_auditoria":     {"schema_fixo":False, "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":False, "dado_sensivel":True},
    "carrinho_de_licencas":    {"schema_fixo":True,  "precisa_acid":True,  "escala_horizontal":False, "tolera_atraso_de_consistencia":False, "dado_sensivel":False},
    "cache_de_sessoes":        {"schema_fixo":True,  "precisa_acid":False, "escala_horizontal":True,  "tolera_atraso_de_consistencia":True,  "dado_sensivel":True},
}

for nome, perfil in perfis.items():
    resultado = recomendar(perfil)
    print(f"{nome:25s} -> {resultado['banco']:8s} | {resultado['cap']} | \"{resultado['justificativa']}\" | {resultado['risco_owasp']}")