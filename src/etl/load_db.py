import pandas as pd
import sqlite3
import os
import logging

# Configuração de Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'cadunico_limpo.csv')
DB_PATH = os.path.join(BASE_DIR, 'data', 'database', 'cadunico.db')
SCHEMA_PATH = os.path.join(BASE_DIR, 'src', 'sql', 'schema.sql')

def criar_banco():
    """Cria o banco de dados e as tabelas."""
    logger.info(f"Criando/Conectando ao banco de dados: {DB_PATH}")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Ler o arquivo de schema
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
        
    # Executar o script SQL
    cursor.executescript(schema_sql)
    conn.commit()
    conn.close()
    logger.info("Schema aplicado com sucesso.")

def carregar_dados():
    """Lê o CSV processado e insere nas tabelas SQL."""
    logger.info("Carregando dados do CSV para o Banco...")
    
    df = pd.read_csv(PROCESSED_DATA_PATH)
    
    conn = sqlite3.connect(DB_PATH)
    
    try:
        # 1. Carga da Tabela Dimensão (Famílias)
        dim_familias_cols = ['family_id', 'bairro', 'rua', 'localidade_tipo', 
                             'tipo_moradia', 'agua', 'esgoto', 'lat', 'lon']
        
        df_dim = df[dim_familias_cols].drop_duplicates(subset=['family_id'])
        df_dim.to_sql('dim_familias', conn, if_exists='append', index=False)
        logger.info(f"Tabela dim_familias carregada: {len(df_dim)} registros.")

        # 2. Carga da Tabela Fato (Indicadores)
        fact_cols = ['family_id', 'n_membros', 'renda_total', 'renda_per_capita', 
                     'faixa_renda', 'recebe_bolsa_familia', 'recebe_bpc', 
                     'tem_deficiencia', 'idade_responsavel', 'faixa_etaria_responsavel',
                     'escolaridade_responsavel']
        
        df_fact = df[fact_cols]
        df_fact.to_sql('fact_indicadores_sociais', conn, if_exists='append', index=False)
        logger.info(f"Tabela fact_indicadores_sociais carregada: {len(df_fact)} registros.")
        
        conn.commit()
        logger.info("Carga de dados concluída com sucesso.")
        
    except sqlite3.IntegrityError as e:
        logger.error(f"Erro de integridade (possível duplicação): {e}")
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH) # Recriar banco limpo para evitar duplicatas em testes
    
    criar_banco()
    carregar_dados()
