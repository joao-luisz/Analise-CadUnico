-- Schema para Análise do Cadastro Único
-- Modelagem Dimensional (Star Schema simplificado para SQLite)

-- Tabela Fato: Famílias (Centraliza as métricas principais)
CREATE TABLE IF NOT EXISTS dim_familias (
    family_id TEXT PRIMARY KEY,
    bairro TEXT,
    rua TEXT,
    localidade_tipo TEXT,
    tipo_moradia TEXT,
    agua TEXT,
    esgoto TEXT,
    lat REAL,
    lon REAL
);

-- Tabela Fato: Indicadores Sociais (Métricas numéricas e flags)
CREATE TABLE IF NOT EXISTS fact_indicadores_sociais (
    family_id TEXT,
    n_membros INTEGER,
    renda_total REAL,
    renda_per_capita REAL,
    faixa_renda TEXT,
    recebe_bolsa_familia INTEGER, -- 0 ou 1
    recebe_bpc INTEGER, -- 0 ou 1
    tem_deficiencia INTEGER, -- 0 ou 1
    idade_responsavel INTEGER,
    faixa_etaria_responsavel TEXT,
    escolaridade_responsavel TEXT,
    FOREIGN KEY (family_id) REFERENCES dim_familias(family_id)
);

-- View Analítica: Tabela Única para Power BI (Facilita a importação)
CREATE VIEW IF NOT EXISTS view_analytics_master AS
SELECT 
    f.family_id,
    f.bairro,
    f.localidade_tipo,
    f.tipo_moradia,
    i.n_membros,
    i.renda_total,
    i.renda_per_capita,
    i.faixa_renda,
    i.recebe_bolsa_familia,
    i.recebe_bpc,
    i.tem_deficiencia,
    i.idade_responsavel,
    i.faixa_etaria_responsavel,
    i.escolaridade_responsavel
FROM dim_familias f
JOIN fact_indicadores_sociais i ON f.family_id = i.family_id;
