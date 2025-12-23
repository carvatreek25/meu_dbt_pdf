📊 Pipeline de Dados: Converter PDFs em dados estruturados usando Camelot & DBT & MYSQL & Power BI
Este projeto realiza a extração automática de dados de faturas em PDF, processa as transformações via dbt em um banco MySQL e disponibiliza os dados lapidados para um Dashboard no Power BI.

🏗️ Estrutura do Projeto
Extração: Scripts Python que transformam PDFs brutos em tabelas relacionais.



Warehouse: Banco de Dados MySQL (Schema: analytics).

Transformação: dbt (Data Build Tool) organizado em camadas Bronze, Silver e Gold.

BI: Dashboard no Power BI conectado à camada Gold.

🛠️ Configuração do Ambiente

1. Ativação do Ambiente Virtual
Como as bibliotecas foram instaladas diretamente no venv, sempre ative-o antes de trabalhar:

PowerShell

.\venv\Scripts\activate

2. Banco de Dados (MySQL)
O projeto está configurado para um servidor local:

Host: ****

User: ***

Database: analytics

3. Transformação com dbt
Para rodar as transformações e gerar a tabela final:

PowerShell

cd meu_dbt_pdf
dbt run
O modelo principal é o gold_fatura_jornada, que realiza um UNION ALL entre as fontes processadas.

📂 Estrutura do Projeto (Organização Real)
O projeto está estruturado da seguinte forma:

Abaixo está o mapeamento do fluxo de dados desde as tabelas de origem até a camada final Gold:

![Arquitetura de Tabelas](./img/arquitetura%20de%20tabelas.png)

meu_dbt_pdf/: Diretório raiz do projeto dbt.

models/: Contém as camadas de dados.

bronze/: Dados crus importados do extrator.

silver/: Modelos de limpeza como silver_fatura_jornada.sql.

gold/: Tabelas de negócio finais, como a gold_fatura_jornada.sql.

target/: Arquivos compilados pelo dbt após o comando run.

dbt_project.yml: Configuração principal do projeto dbt.

venv/: Ambiente virtual onde estão instaladas as dependências (dbt-mysql, pandas, etc).

🔄 Fluxo de Trabalho Atualizado
Ativação: O ambiente é ativado via .\venv\Scripts\Activate.ps1.

Transformação: O comando dbt run é executado dentro da pasta meu_dbt_pdf para processar os modelos SQL.

Destino: Os dados são consolidados no MySQL local (Schema: analytics).

Consumo: O Power BI conecta-se ao MySQL para ler a tabela final gerada na pasta gold.

📊 Visualização Final (Power BI)
O Dashboard final consome a tabela gold_fatura_jornada.

Conecte o Power BI ao MySQL (localhost:3306).

Selecione o banco analytics.

Importe a tabela gold_fatura_jornada.

Principais métricas:

Total de Movimentação Financeira.

Volume por Mercadoria.

Evolução diária (Data de Pregão).
