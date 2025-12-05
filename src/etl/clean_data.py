import pandas as pd
import numpy as np
import logging
import os
from datetime import datetime

# Configuração de Logging Profissional
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Configurações de Caminhos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_PATH = os.path.join(BASE_DIR, 'data', 'raw', 'uruburetama_cadunico_synthetic.csv')
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed', 'cadunico_limpo.csv')

def carregar_dados(caminho):
    """Carrega os dados brutos do CSV."""
    logger.info(f"Iniciando carregamento de dados de: {caminho}")
    try:
        df = pd.read_csv(caminho)
        logger.info(f"Dados carregados com sucesso. Dimensões: {df.shape}")
        return df
    except Exception as e:
        logger.error(f"Erro ao carregar dados: {e}")
        raise

def limpar_dados(df):
    """Aplica regras de limpeza e padronização nos dados."""
    logger.info("Iniciando processo de limpeza e transformação...")
    
    df_clean = df.copy()

    # 1. Padronização de Nomes de Colunas (Snake Case)
    df_clean.columns = [col.lower().strip().replace(' ', '_') for col in df_clean.columns]
    
    # 2. Tratamento de Valores Nulos e Tipos de Dados
    # Renda: Garantir que é numérico
    cols_numericas = ['renda_total', 'renda_per_capita', 'n_membros', 'idade_responsavel']
    for col in cols_numericas:
        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # Preencher nulos em renda com 0 (assunção de negócio: sem renda declarada)
    df_clean['renda_total'] = df_clean['renda_total'].fillna(0)
    df_clean['renda_per_capita'] = df_clean['renda_per_capita'].fillna(0)

    # 3. Padronização de Texto (Uppercase para evitar duplicatas por case)
    cols_texto = ['bairro', 'rua', 'localidade_tipo', 'escolaridade_responsavel', 'tipo_moradia']
    for col in cols_texto:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].astype(str).str.upper().str.strip()

    # 4. Criação de Novas Features (Engenharia de Atributos)
    
    # Faixa de Renda (Classificação Social)
    # Critérios baseados no CadÚnico real (valores aproximados para exemplo)
    def classificar_renda(renda_per_capita):
        if renda_per_capita <= 105:
            return 'EXTREMA POBREZA'
        elif renda_per_capita <= 210:
            return 'POBREZA'
        elif renda_per_capita <= 706: # 1/2 Salário Mínimo (aprox 2024)
            return 'BAIXA RENDA'
        else:
            return 'ACIMA 1/2 SM'
            
    df_clean['faixa_renda'] = df_clean['renda_per_capita'].apply(classificar_renda)

    # Faixa Etária do Responsável
    bins = [0, 18, 30, 60, 120]
    labels = ['JOVEM (0-18)', 'ADULTO JOVEM (19-30)', 'ADULTO (31-60)', 'IDOSO (60+)']
    df_clean['faixa_etaria_responsavel'] = pd.cut(df_clean['idade_responsavel'], bins=bins, labels=labels, right=False)

    # 5. Validação de Dados
    # Remover duplicatas completas se houver
    duplicatas = df_clean.duplicated().sum()
    if duplicatas > 0:
        logger.warning(f"Removendo {duplicatas} linhas duplicadas.")
        df_clean = df_clean.drop_duplicates()

    logger.info("Limpeza concluída.")
    return df_clean

def salvar_dados(df, caminho):
    """Salva os dados processados em CSV."""
    logger.info(f"Salvando dados processados em: {caminho}")
    try:
        df.to_csv(caminho, index=False, encoding='utf-8')
        logger.info("Dados salvos com sucesso.")
    except Exception as e:
        logger.error(f"Erro ao salvar dados: {e}")
        raise

def main():
    start_time = datetime.now()
    logger.info(">>> INICIANDO PIPELINE ETL <<<")
    
    try:
        # Extração
        df_raw = carregar_dados(RAW_DATA_PATH)
        
        # Transformação
        df_processed = limpar_dados(df_raw)
        
        # Carregamento (Load para arquivo)
        salvar_dados(df_processed, PROCESSED_DATA_PATH)
        
        # Estatísticas Finais
        logger.info(f"Total de registros processados: {len(df_processed)}")
        logger.info(f"Média de Renda Per Capita: R$ {df_processed['renda_per_capita'].mean():.2f}")
        
    except Exception as e:
        logger.critical("Falha crítica no pipeline ETL.")
        raise e
    finally:
        duration = datetime.now() - start_time
        logger.info(f">>> PIPELINE FINALIZADO EM {duration} <<<")

if __name__ == "__main__":
    main()
