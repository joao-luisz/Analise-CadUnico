# Guia de Implementação: Dashboard Power BI - Cadastro Único Uruburetama

Este guia descreve passo-a-passo como conectar os dados e construir o dashboard no Power BI Desktop.

## 1. Conexão com os Dados

### Opção A: Conectar ao Banco de Dados SQLite (Recomendado)
1. Abra o Power BI Desktop.
2. Clique em **Obter Dados** -> **Mais...**
3. Pesquise por **ODBC** e selecione.
4. Na string de conexão, se você não tiver um DSN configurado, pode tentar usar a string direta se tiver o driver instalado, ou mais fácil:
   **Alternativa Simples**: Use o script Python integrado do Power BI.
   - Vá em **Obter Dados** -> **Outros** -> **Script Python**.
   - Cole o seguinte código:
     ```python
     import pandas as pd
     import sqlite3
     # Ajuste o caminho para o SEU caminho absoluto
     db_path = r'C:\Users\azjoa\OneDrive\Área de Trabalho\Nova pasta\data\database\cadunico.db'
     conn = sqlite3.connect(db_path)
     df = pd.read_sql_query("SELECT * FROM view_analytics_master", conn)
     conn.close()
     ```
   - Clique em OK e selecione a tabela `df`.

### Opção B: Conectar ao CSV Processado
1. Clique em **Obter Dados** -> **Texto/CSV**.
2. Selecione o arquivo: `data/processed/cadunico_limpo.csv`.
3. Clique em **Transformar Dados**.
4. Verifique os tipos de dados (Renda como número decimal, Idade como número inteiro).
5. Clique em **Fechar e Aplicar**.

---

## 2. Modelagem de Dados (DAX)

Crie uma nova tabela chamada `_Medidas` para organizar suas fórmulas.

### Medidas Principais

**1. Total de Famílias**
```dax
Total Familias = COUNTROWS('view_analytics_master')
```

**2. Famílias em Extrema Pobreza**
```dax
Familias Extrema Pobreza = 
CALCULATE(
    [Total Familias], 
    'view_analytics_master'[faixa_renda] = "EXTREMA POBREZA"
)
```

**3. % Cobertura Bolsa Família**
```dax
% Cobertura BF = 
DIVIDE(
    CALCULATE([Total Familias], 'view_analytics_master'[recebe_bolsa_familia] = 1),
    [Total Familias],
    0
)
```

**4. Renda Média**
```dax
Renda Media = AVERAGE('view_analytics_master'[renda_per_capita])
```

---

## 3. Design do Dashboard (Sugestão de Layout)

### Página 1: Visão Geral (Overview)
- **Cabeçalho**: Logo da Prefeitura (fictício) + Título "Monitoramento Cadastro Único".
- **Cartões (KPIs)** no topo:
  - Total de Famílias
  - % Cobertura Bolsa Família
  - Famílias em Extrema Pobreza
  - Renda Média Per Capita
- **Gráfico de Mapa**:
  - Localização das famílias (Latitude/Longitude).
  - Tamanho da bolha: `n_membros`.
  - Cor da bolha: `faixa_renda`.
- **Gráfico de Barras**: "Famílias por Bairro".
- **Gráfico de Rosca**: "Distribuição por Faixa de Renda".

### Página 2: Vulnerabilidade Social
- **Matriz**: Linhas = `Bairro`, Colunas = `Tipo de Esgoto`, Valores = `Total Familias`.
- **Gráfico de Colunas Empilhadas**: "Escolaridade do Responsável por Faixa de Renda".
- **Segmentação de Dados (Filtros)**:
  - Zona (Urbana/Rural)
  - Recebe BPC (Sim/Não)
  - Tem Deficiência (Sim/Não)

---

## 4. Dicas de Design (Estilo Google/Enterprise)
- **Cores**: Use um tema sóbrio. Azul escuro (#1A73E8) para destaque, cinza claro para fundo.
- **Fontes**: Segoe UI ou Roboto.
- **Espaçamento**: Mantenha margens consistentes entre os gráficos.
- **Interatividade**: Ative o "Drill-down" nos gráficos de bairro.
