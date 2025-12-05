# Dicionário de Dados - Cadastro Único

Este documento descreve as variáveis presentes no conjunto de dados processado e no banco de dados.

## Tabela: `dim_familias`
| Coluna | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `family_id` | TEXT | Identificador único da família (Chave Primária) | `FAM00001` |
| `bairro` | TEXT | Nome do bairro ou localidade | `CENTRO` |
| `rua` | TEXT | Nome do logradouro | `RUA PRINCIPAL` |
| `localidade_tipo` | TEXT | Classificação da zona (Urbana/Rural) | `URBANA` |
| `tipo_moradia` | TEXT | Material predominante da moradia | `ALVENARIA` |
| `agua` | TEXT | Forma de abastecimento de água | `REDE GERAL` |
| `esgoto` | TEXT | Forma de escoamento sanitário | `FOSSA SÉPTICA` |
| `lat` | REAL | Latitude da residência | `-3.621178` |
| `lon` | REAL | Longitude da residência | `-39.503291` |

## Tabela: `fact_indicadores_sociais`
| Coluna | Tipo | Descrição | Exemplo |
| :--- | :--- | :--- | :--- |
| `family_id` | TEXT | Chave estrangeira para `dim_familias` | `FAM00001` |
| `n_membros` | INTEGER | Número de pessoas na família | `5` |
| `renda_total` | REAL | Renda total da família (R$) | `181.00` |
| `renda_per_capita` | REAL | Renda por pessoa (R$) | `36.20` |
| `faixa_renda` | TEXT | Classificação socioeconômica baseada na renda | `EXTREMA POBREZA` |
| `recebe_bolsa_familia` | INTEGER | Flag (0/1) se recebe Bolsa Família | `1` |
| `recebe_bpc` | INTEGER | Flag (0/1) se recebe BPC (Benefício Prestação Continuada) | `0` |
| `tem_deficiencia` | INTEGER | Flag (0/1) se há pessoa com deficiência na família | `0` |
| `idade_responsavel` | INTEGER | Idade do responsável familiar | `45` |
| `faixa_etaria_responsavel`| TEXT | Grupo etário do responsável | `ADULTO (31-60)` |
| `escolaridade_responsavel`| TEXT | Nível de instrução do responsável | `FUNDAMENTAL INCOMPLETO` |
