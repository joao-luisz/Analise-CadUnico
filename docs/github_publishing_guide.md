# Guia de Publicação no GitHub

Este guia explica como colocar seu projeto no GitHub e torná-lo atraente para recrutadores.

## 1. Preparação do Repositório (Local)

Já criei o arquivo `.gitignore` para você. Isso impede que arquivos desnecessários (como pastas de ambiente virtual ou arquivos temporários) sejam enviados.

### Passo a Passo no Terminal (Git Bash ou VS Code):

1.  **Inicialize o Git**:
    ```bash
    git init
    ```

2.  **Adicione os arquivos**:
    ```bash
    git add .
    ```

3.  **Faça o primeiro commit**:
    ```bash
    git commit -m "Initial commit: Projeto de Análise de Dados CadÚnico"
    ```

4.  **Renomeie a branch principal (boas práticas)**:
    ```bash
    git branch -M main
    ```

## 2. Criando o Repositório no GitHub

1.  Acesse [github.com/new](https://github.com/new).
2.  **Nome do Repositório**: `uruburetama-analytics` (ou algo similar).
3.  **Descrição**: "Análise de dados end-to-end do Cadastro Único de Uruburetama usando Python, SQL e Power BI."
4.  **Visibilidade**: Público.
5.  **NÃO** marque "Add a README file" (já temos um).
6.  Clique em **Create repository**.

## 3. Conectando e Enviando

Copie o link do repositório criado (ex: `https://github.com/seu-usuario/uruburetama-analytics.git`) e execute no terminal:

```bash
git remote add origin https://github.com/seu-usuario/uruburetama-analytics.git
git push -u origin main
```

## 4. Tornando o Projeto "Apresentável" (Dicas de Ouro)

Para se destacar como Senior/Profissional:

### A. Adicione Screenshots do Dashboard
Recrutadores são visuais. Eles podem não baixar seu Power BI, mas verão as imagens.
1.  Tire prints das telas do seu Dashboard no Power BI.
2.  Salve na pasta `docs/img/` (crie essa pasta).
3.  Edite o `README.md` para incluir as imagens logo após a introdução.
    ```markdown
    ## 📊 Dashboard
    ![Visão Geral](docs/img/dashboard_overview.png)
    ```

### B. Use "Topics" (Tags)
No seu repositório no GitHub, clique na engrenagem ao lado de "About" e adicione tags:
`data-analysis`, `python`, `sql`, `powerbi`, `etl`, `portfolio`.

### C. Fixe no seu Perfil
Vá no seu perfil do GitHub, clique em "Customize your pins" e selecione este projeto.

### D. Descrição "Sobre"
No lado direito do repositório, preencha a seção "About" com uma descrição curta e impactante. Se tiver um link (ex: artigo no LinkedIn sobre o projeto), coloque no campo "Website".

---

**Checklist Final:**
- [ ] Código organizado em pastas (`src`, `data`)? (Feito!)
- [ ] README completo e bonito? (Feito!)
- [ ] `.gitignore` configurado? (Feito!)
- [ ] Screenshots adicionados? (Pendente - você precisa criar o dashboard primeiro!)
