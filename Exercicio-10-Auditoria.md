# Auditoria de Segurança — app_vulneravel.py

| # | Falha | OWASP 2025 | Impacto | Correção |
|---|-------|-----------|---------|----------|
| 1 | Query concatenada em `/api/usuarios/buscar` | A05 — Injection | Qualquer entrada vira comando SQL; vaza todos os registros | Usar query parametrizada (`%s`) |
| 2 | Saída não escapada em `/perfil` | A05 — Injection | Script do atacante executa no navegador da vítima (XSS) | Escapar com `markupsafe.escape` ou template Jinja2 |
| 3 | `DELETE /api/usuarios/<uid>` sem checagem de identidade | A01 — Broken Access Control | Qualquer um apaga qualquer usuário sem se autenticar | Exigir `X-API-Key` e checar nível de acesso |
| 4 | `debug=True` expõe traceback em erro de banco | A02 — Security Misconfiguration | Atacante vê estrutura interna (nome de tabela, stack trace) | `debug=False` + resposta genérica de erro |
| 5 | `SELECT *` devolve a coluna `senha` | A04 — Cryptographic Failures | Credenciais sensíveis expostas na resposta da API | Selecionar apenas colunas necessárias |
| 6 | Segredo `SENHA_MESTRA` escrito direto no código | A02 — Security Misconfiguration | Qualquer um com acesso ao código lê a senha | Mover para variável de ambiente |
| 7 | `app.run(debug=True, host="0.0.0.0")` | A02 — Security Misconfiguration | Console interativo exposto para toda a rede | `debug=False`, `host="127.0.0.1"` (ou WSGI em produção) |
| 8 | Nenhum header de segurança configurado | A02 — Security Misconfiguration | Sem proteção extra contra clickjacking/MIME sniffing | Adicionar headers via `@app.after_request` |
| 9 | Ausência total de logging de requisições e erros | A09 — Security Logging & Alerting Failures | Um ataque acontece e ninguém percebe | Registrar cada requisição e erro com o módulo `logging` |
| 10 | Ausência total de autenticação na API | A07 — Authentication Failures | Nenhuma rota sensível pede identidade | Exigir `X-API-Key` validada no banco antes de ações críticas|