-- Análise de Dados - Cadastro Único Uruburetama

-- 1. Distribuição de Famílias por Bairro
-- Pergunta: Quais bairros têm a maior concentração de famílias cadastradas?
SELECT 
    bairro,
    COUNT(family_id) as total_familias,
    ROUND(AVG(renda_per_capita), 2) as renda_media_per_capita
FROM view_analytics_master
GROUP BY bairro
ORDER BY total_familias DESC;

-- 2. Perfil de Renda e Pobreza
-- Pergunta: Qual a porcentagem de famílias em cada faixa de renda?
SELECT 
    faixa_renda,
    COUNT(family_id) as total_familias,
    ROUND(COUNT(family_id) * 100.0 / (SELECT COUNT(*) FROM view_analytics_master), 2) as porcentagem
FROM view_analytics_master
GROUP BY faixa_renda
ORDER BY total_familias DESC;

-- 3. Cobertura do Bolsa Família
-- Pergunta: Qual a taxa de cobertura do Bolsa Família por Bairro?
SELECT 
    bairro,
    COUNT(family_id) as total_familias,
    SUM(recebe_bolsa_familia) as beneficiarios_bf,
    ROUND(SUM(recebe_bolsa_familia) * 100.0 / COUNT(family_id), 2) as taxa_cobertura
FROM view_analytics_master
GROUP BY bairro
HAVING total_familias > 10 -- Filtrar bairros com poucas famílias para relevância estatística
ORDER BY taxa_cobertura DESC;

-- 4. Análise de Vulnerabilidade (Saneamento)
-- Pergunta: Famílias sem acesso a esgoto adequado por tipo de localidade (Urbana/Rural)
SELECT 
    localidade_tipo,
    esgoto,
    COUNT(family_id) as total_familias
FROM view_analytics_master
WHERE esgoto IN ('Vala a céu aberto', 'Fossa rudimentar')
GROUP BY localidade_tipo, esgoto
ORDER BY localidade_tipo, total_familias DESC;

-- 5. Idosos em Situação de Vulnerabilidade
-- Pergunta: Quantos idosos (60+) responsáveis familiares vivem em extrema pobreza?
SELECT 
    COUNT(family_id) as idosos_extrema_pobreza
FROM view_analytics_master
WHERE faixa_etaria_responsavel = 'IDOSO (60+)' 
AND faixa_renda = 'EXTREMA POBREZA';
