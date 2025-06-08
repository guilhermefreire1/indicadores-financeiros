
📊 Indicadores Financeiros - Dashboard Interativo com Streamlit

Este projeto realiza a coleta, tratamento, armazenamento e visualização interativa de indicadores econômicos brasileiros: SELIC, IPCA e Dólar Comercial, utilizando dados reais da API SGS do Banco Central do Brasil.

🚀 Funcionalidades

- 🔄 Coleta automática de dados financeiros com requests e pandas
- 🗂️ Armazenamento local em banco de dados SQLite
- 📈 Visualização de séries temporais com Plotly
- 🎛️ Filtros dinâmicos de período e indicadores no dashboard
- 💡 Resumo estatístico com máximo, mínimo e média
- 🌐 Deploy no Streamlit Cloud

🛠️ Tecnologias Utilizadas

Python     - Linguagem principal do projeto
Pandas     - Manipulação e limpeza de dados
Requests   - Requisição de dados via API
SQLite     - Armazenamento local
Streamlit  - Criação do dashboard web
Plotly     - Gráficos interativos

📁 Estrutura do Projeto

indicadores_financeiros/
├── data/
│   └── indicadores.csv
├── db/
│   └── indicadores.db
├── dashboard/
│   └── dashboard_indicadores.py
├── src/
│   ├── coleta_unificada.py
│   └── salva_sqlite.py
├── main.py
├── requirements.txt
└── README.txt

⚙️ Como Executar Localmente

1. Clone o repositório:
   git clone https://github.com/guilhermefreire1/indicadores-financeiros.git
   cd indicadores-financeiros

2. Crie um ambiente virtual (opcional):
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/macOS

3. Instale as dependências:
   pip install -r requirements.txt

4. Execute o pipeline:
   python main.py

5. Rode o dashboard:
   streamlit run dashboard/dashboard_indicadores.py

🌍 Acesse Online

Indicadores Econômicos - Streamlit App (https://indicadores-financeiros.streamlit.app/)

📌 Exemplos de Uso

- Visualizar a evolução histórica da taxa SELIC
- Comparar o comportamento do IPCA e do Dólar no mesmo período
- Obter médias e valores máximos/mínimos filtrando por datas

🤝 Contribuição

Contribuições são bem-vindas! Fique à vontade para abrir issues, sugestões ou pull requests.

📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
