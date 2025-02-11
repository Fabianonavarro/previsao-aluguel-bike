import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Definir o backend para evitar dependência do Tkinter
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
import warnings
from PIL import Image

# Ignorar warnings específicos
warnings.filterwarnings("ignore", message="Too few observations")

# Carregar os dados
data = pd.read_csv('bike-data/bike-share.csv')

# Renomear as colunas
data.columns = ['dia', 'mes', 'ano', 'temporada', 'feriado', 'dia da semana', 
                'dia util', 'previsao do tempo', 'temperatura', 'atemp', 'hum', 
                'velocidade do vento', 'aluguel']

# Criar uma coluna 'data' para facilitar a manipulação
data['data'] = pd.to_datetime(data[['ano', 'mes', 'dia']].astype(str).agg('-'.join, axis=1))

# Filtrar os dados para os anos de 2023 e 2024
data_2023_2024 = data[(data['ano'] >= 2023) & (data['ano'] <= 2024)]

# Agrupar por mês e somar os aluguéis para cada mês
data_monthly = data_2023_2024.groupby(['ano', 'mes'])['aluguel'].sum()

# Criar uma série temporal de aluguéis mensais
monthly_series = data_monthly.values

# Ajustar o modelo SARIMA (com parâmetros ajustados para sazonalidade de 12 meses)
model = SARIMAX(monthly_series, 
                order=(1, 1, 1),  # ARIMA(p,d,q) simples
                seasonal_order=(1, 1, 1, 12),  # SARIMA(P,D,Q,s) com sazonalidade anual
                enforce_stationarity=False, 
                enforce_invertibility=False)
model_fit = model.fit(disp=False)

# Fazer previsões para 2025 (12 meses)
forecast = model_fit.forecast(steps=12)

# Adicionar as previsões para o ano de 2025
months_2025 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Visualizar a previsão de aluguéis para 2025
plt.figure(figsize=(10, 6))
plt.plot(months_2025, forecast, marker='o', color='blue', label='Previsão de Aluguel para 2025')

# Identificar o melhor e pior mês
best_month = np.argmax(forecast)  # Melhor mês
worst_month = np.argmin(forecast)  # Pior mês

# Destacar os melhores e piores meses no gráfico
plt.scatter(months_2025[best_month], forecast[best_month], color='green', label=f'Melhor Mês: {months_2025[best_month]}')
plt.scatter(months_2025[worst_month], forecast[worst_month], color='red', label=f'Pior Mês: {months_2025[worst_month]}')

# Título e rótulos
plt.title('Previsão de Aluguéis de Bicicleta para 2025')
plt.xlabel('Mês')
plt.ylabel('Número de Aluguéis')
plt.legend()

# Exibir gráfico
plt.grid(True)

# Salvar o gráfico como uma imagem PNG
plt.savefig('previsao_2025.png')

# Exibir uma mensagem indicando onde o gráfico foi salvo
print("O gráfico foi salvo como 'previsao_2025.png'.")

# Mostrar o gráfico gerado
img = Image.open('previsao_2025.png')
img.show()  # Abre o gráfico salvo como uma imagem
