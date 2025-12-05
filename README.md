# Projeto de Análise de Dados: Cadastro Único de Uruburetama

![Status do Projeto](https://img.shields.io/badge/Status-Concluído-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)

## 📋 Visão Geral do Projeto

Este projeto consiste em uma análise completa "end-to-end" dos dados do Cadastro Único (CadÚnico) do município de Uruburetama. O objetivo é simular um ambiente corporativo real, transformando dados brutos em inteligência de negócios para apoiar a tomada de decisão em políticas públicas.

O projeto segue uma arquitetura de dados moderna, com pipeline de ETL em Python, modelagem dimensional (Star Schema) em SQL e visualização interativa no Power BI.

### 🎯 Objetivos de Negócio
1.  **Mapeamento de Vulnerabilidade**: Identificar bairros e zonas com maior concentração de famílias em extrema pobreza.
2.  **Eficiência de Programas Sociais**: Analisar a cobertura do Bolsa Família e BPC.
3.  **Perfil Demográfico**: Entender a composição familiar e escolaridade dos responsáveis.

---

## 🏗️ Arquitetura do Projeto

A estrutura do projeto foi organizada seguindo as melhores práticas de engenharia de software e dados:

```
uruburetama-analytics/
├── data/
│   ├── raw/                # Dados brutos (CSV original)
│   ├── processed/          # Dados limpos e padronizados (CSV)
│   └── database/           # Banco de Dados SQLite (Data Warehouse)
├── src/
│   ├── etl/                # Scripts Python para Extração e Transformação
│   │   ├── clean_data.py   # Limpeza e engenharia de atributos
│   │   └── load_db.py      # Carga no banco de dados
│   └── sql/                # Scripts SQL
│       ├── schema.sql      # Definição das tabelas (DDL)
│       └── analysis_queries.sql # Consultas de negócio
├── docs/
│   ├── powerbi_guide.md    # Guia passo-a-passo para o Dashboard
│   └── data_dictionary.md  # Dicionário de dados
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação principal
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- Power BI Desktop (para visualização)

### Passo 1: Configuração do Ambiente
1. Clone este repositório ou baixe a pasta.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Passo 2: Execução do Pipeline ETL
Execute os scripts na ordem para processar os dados e popular o banco:

1. **Limpeza de Dados**:
   ```bash
   python src/etl/clean_data.py
   ```
   *Saída: Gera `data/processed/cadunico_limpo.csv`*

2. **Carga no Banco de Dados**:
   ```bash
   python src/etl/load_db.py
   ```
   *Saída: Gera `data/database/cadunico.db`*

### Passo 3: Análise e Visualização
- **SQL**: Utilize o arquivo `src/sql/analysis_queries.sql` para rodar consultas diretamente no banco de dados (use um cliente SQLite como DBeaver ou DB Browser).
- **Power BI**: Siga o guia em `docs/powerbi_guide.md` para conectar o Power BI ao banco de dados e criar o dashboard.

---

## 📊 Resultados e Insights (Exemplos)

> *Nota: Os dados são sintéticos e utilizados apenas para fins de demonstração.*

- **Cobertura do Bolsa Família**: A análise revelou que bairros rurais possuem uma taxa de cobertura 15% superior à zona urbana.
- **Saneamento**: Identificou-se que 30% das famílias na zona rural ainda utilizam fossa rudimentar, indicando prioridade para obras de saneamento.

---

## 🛠️ Tecnologias Utilizadas

- **Python (Pandas/Numpy)**: Para manipulação e limpeza de dados de alta performance.
- **SQLite**: Banco de dados relacional leve e serverless para armazenamento estruturado.
- **SQL**: Linguagem padrão para consultas analíticas.
- **Power BI**: Ferramenta líder de mercado para Business Intelligence.

---

## 👤 Autor

Projeto desenvolvido como parte de portfólio profissional de Análise de Dados.
