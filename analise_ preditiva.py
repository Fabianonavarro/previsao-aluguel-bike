import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Forçar o uso do backend 'Agg'
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
from PIL import Image

# Carregar os dados
data = pd.read_csv('bike-data/bike-share.csv')

# Renomear as colunas para garantir que correspondem ao que você mencionou
data.columns = ['dia', 'mes', 'ano', 'temporada', 'feriado', 'dia da semana', 
                'dia util', 'previsao do tempo', 'temperatura', 'atemp', 'hum', 
                'velocidade do vento', 'aluguel']

# Criar a coluna 'data' com a data correta, ajustando a ordem das colunas
data['data'] = pd.to_datetime(data[['ano', 'mes', 'dia']].astype(str).agg('-'.join, axis=1))

# Criar uma nova coluna para o número de dias passados (para prever a partir de dados temporais)
data['dias_passados'] = (data['data'] - data['data'].min()).dt.days

# Definir as variáveis independentes (X) e dependentes (y)
X = data[['dias_passados', 'temperatura', 'atemp', 'hum', 'velocidade do vento']]
y = data['aluguel']

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)

# Aqui você pode exibir uma mensagem personalizada sobre o desempenho
if mse < 100000:  # Se o erro quadrático médio for baixo, exiba uma mensagem positiva
    print(f"Modelo treinado com sucesso! O erro quadrático médio (MSE) é baixo: {mse:.2f}. O modelo tem bom desempenho.")
else:  # Caso o MSE seja alto, mostre que o modelo pode precisar de melhorias
    print(f"Modelo treinado com sucesso! O erro quadrático médio (MSE) é: {mse:.2f}. O modelo pode precisar de ajustes para melhorar a precisão.")

# Encontrar os valores mínimo, máximo e médio
min_rentals = data['aluguel'].min()
max_rentals = data['aluguel'].max()
mean_rentals = data['aluguel'].mean()

# Encontrar os dias em que ocorrem esses valores
min_day = data.loc[data['aluguel'] == min_rentals, 'data'].iloc[0]
max_day = data.loc[data['aluguel'] == max_rentals, 'data'].iloc[0]

# Encontrar o dia mais próximo da média
mean_day = data.iloc[(data['aluguel'] - mean_rentals).abs().argsort()[:1]]['data'].iloc[0]

# Plotar o gráfico
plt.figure(figsize=(10, 6))

# Plotar os dados históricos
plt.plot(data['data'], data['aluguel'], label='Aluguel Histórico', color='gray', alpha=0.6)

# Plotar os pontos mínimo, máximo e médio com as cores solicitadas
plt.scatter(min_day, min_rentals, color='blue', label=f'Mínimo: {min_rentals} em {min_day.strftime("%d-%m-%Y")}', zorder=5)
plt.scatter(max_day, max_rentals, color='red', label=f'Máximo: {max_rentals} em {max_day.strftime("%d-%m-%Y")}', zorder=5)
plt.scatter(mean_day, mean_rentals, color='yellow', label=f'Média: {mean_rentals:.2f} em {mean_day.strftime("%d-%m-%Y")}', zorder=5)

# Adicionar título e rótulos
plt.title('Aluguel de Bicicletas ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Aluguéis')
plt.legend()

# Salvar o gráfico como imagem
plt.savefig('grafico_alugueis.png')
print("O gráfico foi salvo como 'grafico_alugueis.png'.")

# Mostrar o gráfico gerado
img = Image.open('grafico_alugueis.png')
img.show()  # Abre o gráfico salvo como uma imagem
