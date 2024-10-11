# Análise e Priorização de Reclamações de Clientes para iFood

Este projeto de estudo tem como objetivo analisar e priorizar reclamações de clientes da **iFood** obtidas através da plataforma **Reclame Aqui**. Utilizando técnicas de **web scraping**, **análise de dados** e **Processamento de Linguagem Natural (NLP)**, o projeto visa otimizar o atendimento ao cliente, identificando e respondendo de forma eficaz às reclamações mais urgentes.

## 📁 Estrutura do Projeto
├── data/ │ ├── comentarios_coletados.csv │ ├── comentarios_coletados.xlsx │ └── comentarios_coletados_atualizado.csv ├── scripts/ │ ├── scrape_reclamacoes.py │ └── analyze_sentimentos.py ├── README.md ├── requirements.txt └── .gitignore

## 📝 Descrição

### Fase 1: Coleta e Classificação de Reclamações

**O que já realizamos:**

1. **Coleta de Dados Automatizada:**
   - Utilizamos **Selenium** e **BeautifulSoup** para extrair cerca de **15 mil comentários não respondidos** da página de reclamações do iFood no Reclame Aqui de forma automatizada.

2. **Classificação por Frequência:**
   - **Produtos ou Serviços:** Mapeamos cada categoria com base no número de reclamações recebidas, aplicando uma escala logarítmica para normalizar os dados e atribuir pesos de **0 a 10**.
   - **Problemas:** Da mesma forma, classificamos os diferentes tipos de problemas enfrentados pelos clientes, também normalizando os pesos para facilitar a priorização.

3. **Estruturação dos Dados:**
   - Organizamos os comentários em formatos **CSV** e **Excel**, facilitando futuras análises e integrações.

### Fase 2: Análise de Sentimentos e Classificação de Urgência

**Próximos Passos:**

1. **Análise de Sentimentos:**
   - Implementaremos modelos de **Processamento de Linguagem Natural (NLP)**, como **BERT**, para avaliar o **sentimento** e o **tom** de cada comentário. Isso permitirá identificar a intensidade das emoções expressas pelos clientes, diferenciando entre reclamações críticas e menos impactantes.

2. **Atribuição de Peso de Sentimento:**
   - Cada comentário receberá um **peso de sentimento** na escala de **0 a 10**, refletindo a negatividade ou positividade do feedback.

3. **Cálculo do Peso Final:**
   - Combinação dos **pesos de frequência** e **sentimento** para obter o **peso final**, que servirá como base para a classificação da urgência.

4. **Classificação da Urgência:**
   - **Alta Urgência:** Comentários com peso final >= 8 serão priorizados para resposta imediata.
   - **Média Urgência:** Comentários com peso final entre 5 e 8 serão tratados com atenção moderada.
   - **Baixa Urgência:** Comentários com peso final < 5 serão monitorados para possíveis melhorias futuras.

## 💻 Tecnologias Utilizadas

- **Python 3.8+**
- **Selenium:** Automação de navegador para web scraping.
- **BeautifulSoup:** Análise e extração de dados HTML.
- **Pandas:** Manipulação e análise de dados.
- **Transformers (Hugging Face):** Modelos de NLP para análise de sentimentos.
- **NLTK:** Pré-processamento de texto.
- **OpenPyXL:** Manipulação de arquivos Excel.
- **Git:** Controle de versão.

## 🛠️ Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/analise-reclamacoes-ifood.git
   cd analise-reclamacoes-ifood

2. **Crie um Ambiente Virtual (Opcional, mas Recomendado):**
    ```bash

    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate


3. **Instale as Dependências:**

    ```bash
    pip install -r requirements.txt

4. **Configure o WebDriver do Chrome:**

    * Faça o download do ChromeDriver compatível com a versão do seu navegador aqui.
    * Extraia o executável e adicione o caminho dele à variável de ambiente PATH ou coloque-o na raiz do projeto.


📈 Uso
1. **Coleta de Reclamações**

    Execute o script de scraping para coletar as reclamações:
    ```bash
    python scripts/scrape_reclamacoes.py

* Saída: Arquivos comentarios_coletados.csv e comentarios_coletados.xlsx na pasta data/.

    2. **Análise de Sentimentos**
    Após coletar os dados, execute o script de análise de sentimentos:
    ```bash
    python scripts/analyze_sentimentos.py
* Saída: Arquivo comentarios_coletados_atualizado.csv na pasta data/ com as novas colunas de análise.

📊 Resultados

Priorização de Reclamações: Combinando os pesos de frequência e sentimento, cada comentário é classificado em termos de urgência, facilitando a identificação das reclamações que requerem atenção imediata.

Insights para Melhoria: A análise fornece uma visão clara das principais áreas que necessitam de melhorias, baseando-se em dados concretos de feedback dos clientes.

🛠️ Scripts Principais

scrape_reclamacoes.py
Script responsável por coletar e classificar as reclamações.

analyze_sentimentos.py
Script responsável por analisar o sentimento dos comentários e calcular o peso final para priorização.

