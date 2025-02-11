# Previsão de Aluguel de Bicicletas

Este projeto visa criar um modelo de previsão de aluguéis de bicicletas usando dados históricos. O modelo leva em consideração diversas variáveis, como a temperatura, o dia da semana, a temporada, entre outras, para prever o número de aluguéis. Além disso, o projeto oferece análises estatísticas e gráficos para facilitar a visualização de dados.

## Passo a Passo

### 1. Configurar o Ambiente

Antes de começar, é necessário configurar o ambiente Python.

- **Crie um ambiente virtual** (opcional, mas recomendado):

    python -m venv venv
   
- **Ative o ambiente virtual**:
  - No Windows:
    .\venv\Scripts\activate
   
  - No macOS/Linux:
    source venv/bin/activate
   
- **Instale as dependências**: Com o ambiente virtual ativado, instale as bibliotecas necessárias com o seguinte comando:

    pip install -r requirements.txt
   
### 2. Estrutura do Projeto

O projeto contém os seguintes arquivos e pastas:

- **analise_previsiva.py**: Contém funções para análises preditivas.
- **comparacao_mes.py**: Realiza comparações entre meses de aluguéis.
- **grafico_estatisticas.py**: Gera gráficos de análise de dados.
- **menu.py**: Menu interativo para fácil navegação pelo projeto.
- **modelo_previsao.pkl**: O modelo treinado de previsão de aluguéis.
- **prever_aluguel.py**: Script para fazer previsões de aluguéis usando o modelo.
- **treinar_modelo.py**: Script para treinar o modelo com os dados históricos.
- **bike-data/**: Pasta com os dados de bicicletas.
- **requirements.txt**: Arquivo com as dependências do projeto.

### 3. Usando o Menu Interativo

A maneira mais fácil de começar a usar o projeto é através do menu interativo.

Execute o seguinte comando:
python menu.py
O menu oferece opções como:

Treinar o modelo: Treina o modelo de previsão com os dados históricos.
Prever o aluguel de bicicletas: Faz previsões com base no modelo treinado.
Gerar gráficos e análises estatísticas: Gera gráficos e análises sobre os dados de aluguéis de bicicletas.

# 4. Treinando o Modelo
Caso queira treinar o modelo com os dados históricos, use o script:
python treinar_modelo.py
Esse comando irá treinar o modelo com os dados disponíveis e gerar o arquivo modelo_previsao.pkl, que será utilizado para realizar as previsões de aluguel.

# 5. Fazendo Previsões
Para fazer previsões sobre o número de aluguéis de bicicletas, execute o script:
python prever_aluguel.py
Esse script utiliza o modelo treinado para prever o número de aluguéis com base nas condições fornecidas, como temperatura, dia da semana, entre outras variáveis.

# 6. Gerando Gráficos e Análises
O projeto também oferece opções para gerar gráficos e análises estatísticas. Para isso, use o script:
python grafico_estatisticas.py
Este comando irá gerar gráficos e exibir análises que ajudam a visualizar e compreender melhor os dados históricos de aluguéis de bicicletas.

### Conclusão
Agora você está pronto para usar o modelo de previsão de aluguéis de bicicletas! Você pode treinar o modelo, fazer previsões ou analisar os dados através das ferramentas e scripts fornecidos.
