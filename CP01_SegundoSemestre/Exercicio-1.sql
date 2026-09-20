--# Exercício 1 — Modelagem e CRUD SQL: Crie a tabela ativos no MySQL e escreva os comandos para inserir,
-- # listar filtrando por tipo, atualizar o status e remover.
-- # Use ENUM para o campo criticidade e UNIQUE no IP.
-- # Schema esperado:
-- # ativos(id PK AUTO_INCREMENT, nome, ip UNIQUE, tipo, criticidade ENUM('baixa','media','alta'), status)
-- # Dados iniciais:-- ativos = [--    ("SRV-WEB01", "192.168.1.10", "servidor", "alta",  "ativo"),
--    ("PC-RH03",   "192.168.1.45", "estacao",  "baixa", "ativo")
--    ("SW-CORE01", "192.168.1.1",  "switch",   "media", "inativo"),
-- # Saída esperada:
-- # Listar tipo='servidor' -> SRV-WEB01 | 192.168.1.10 | alta | ativo
-- # Após UPDATE status de SW-CORE01 para 'ativo' -> "1 registro atualizado"
-- # Inserir IP duplicado (192.168.1.10) -> erro de UNIQUE tratadoUSEseguranca;
-- Criando tabela
CREATE TABLE ativos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    ip VARCHAR(150) UNIQUE NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    criticidade ENUM('baixa', 'media', 'alta') NOT NULL,
    status VARCHAR(20) DEFAULT 'ativo',
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Adicionando elementos na tabela
INSERT INTO ativos (nome, ip, tipo, criticidade, status) VALUES
('SRV-WEB01', '192.168.1.10', 'servidor', 'alta',  'ativo'),
('PC-RH03',   '192.168.1.45', 'estacao',  'baixa', 'ativo'),
('SW-CORE01', '192.168.1.1',  'switch',   'media', 'inativo');

-- Filtrar
SELECT nome, ip, criticidade, status
FROM ativos
WHERE tipo = 'servidor';

-- Atualizar status
UPDATE ativos
SET status = 'ativo'
WHERE nome = 'SW-CORE01';

-- Remover registro
DELETE FROM ativos
WHERE nome = 'SW-CORE01';

-- Testando o erro de UNIQUE
INSERT INTO ativos (nome, ip, tipo, criticidade, status)
VALUES ('PC-TESTE', '192.168.1.10', 'estacao', 'baixa', 'ativo');