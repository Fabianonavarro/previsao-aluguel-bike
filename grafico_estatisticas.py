import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Forçar o uso do backend 'Agg' para evitar problemas com o Tkinter
import matplotlib.pyplot as plt
from PIL import Image

# Carregar os dados
data = pd.read_csv('bike-data/bike-share.csv')

# Renomear as colunas para garantir que correspondem ao que você mencionou
data.columns = ['dia', 'mes', 'ano', 'temporada', 'feriado', 'dia da semana', 
                'dia util', 'previsao do tempo', 'temperatura', 'atemp', 'hum', 
                'velocidade do vento', 'aluguel']

# Calcular as estatísticas de aluguel
min_rentals = data['aluguel'].min()
max_rentals = data['aluguel'].max()
mean_rentals = data['aluguel'].mean()

# Encontrar o dia com o maior número de aluguéis
max_rentals_day = data[data['aluguel'] == max_rentals].iloc[0]
max_rentals_date = f'{max_rentals_day["dia"]}/{max_rentals_day["mes"]}/{max_rentals_day["ano"]}'

# Encontrar o dia com o menor número de aluguéis
min_rentals_day = data[data['aluguel'] == min_rentals].iloc[0]
min_rentals_date = f'{min_rentals_day["dia"]}/{min_rentals_day["mes"]}/{min_rentals_day["ano"]}'

# Exibir estatísticas no console
print(f'Mínimo: {min_rentals} no dia {min_rentals_date}')
print(f'Máximo: {max_rentals} no dia {max_rentals_date}')
print(f'Média: {mean_rentals}')

# Gerar o gráfico
plt.figure(figsize=(8, 6))

# Gráfico de barras com Mínimo, Máximo e Média
bars = plt.bar(['Mínimo', 'Máximo', 'Média'], [min_rentals, max_rentals, mean_rentals], color=['blue', 'green', 'orange'])

# Adicionar título e rótulos
plt.title('Estatísticas de Aluguel de Bicicletas')
plt.xlabel('Estatísticas')
plt.ylabel('Número de Aluguéis')

# Adicionar os valores nas barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 50, round(yval, 2), ha='center', va='bottom', fontsize=12, color='black')

# Adicionar a anotação com o dia de maior aluguel, mas fora do título
plt.figtext(0.5, 0.97, f'Máximo no dia: {max_rentals_date}', ha='center', va='bottom', fontsize=10, color='red')
plt.figtext(0.5, 0.93, f'Mínimo no dia: {min_rentals_date}', ha='center', va='bottom', fontsize=10, color='blue')

# Salvar o gráfico como uma imagem PNG
plt.savefig('grafico_estatisticas.png')

# Exibir uma mensagem indicando onde o gráfico foi salvo
print("O gráfico foi salvo como 'grafico_estatisticas.png'.")

# Mostrar o gráfico gerado
img = Image.open('grafico_estatisticas.png')
img.show()  # Abre o gráfico salvo como uma imagem
