import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Forçar o uso do backend 'Agg' para salvar gráficos sem precisar de Tkinter
import matplotlib.pyplot as plt
from PIL import Image

# Carregar os dados
data = pd.read_csv('bike-data/bike-share.csv')

# Renomear as colunas para facilitar o trabalho com os dados
data.columns = ['dia', 'mes', 'ano', 'temporada', 'feriado', 'dia da semana', 
                'dia util', 'previsao do tempo', 'temperatura', 'atemp', 'hum', 
                'velocidade do vento', 'aluguel']

# Criar uma coluna 'data' para facilitar a manipulação
data['data'] = pd.to_datetime(data[['ano', 'mes', 'dia']].astype(str).agg('-'.join, axis=1))

# Obter o ano máximo registrado nos dados
ano_maximo = data['ano'].max()

# Entrada interativa para os anos de comparação
ano_inicial = int(input("Digite o ano inicial para a comparação: "))
ano_final = int(input("Digite o ano final para a comparação: "))

# Verificar se o intervalo está dentro dos dados disponíveis
if ano_inicial > ano_maximo or ano_final > ano_maximo:
    print(f"Os dados registrados são até o ano {ano_maximo}. Para anos além disso, será realizada uma análise preditiva.")

# Obter os anos no intervalo especificado
anos_intervalo = list(range(ano_inicial, ano_final + 1))

# Obter os nomes dos meses
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Função para gerar o gráfico
def gerar_grafico(ano_inicial, ano_final):
    plt.figure(figsize=(14, 7))

    for idx, ano in enumerate(anos_intervalo):
        # Filtrar os dados para o ano atual
        data_ano = data[data['ano'] == ano] if ano <= ano_maximo else None

        # Caso os dados para o ano não estejam disponíveis, realizar previsão
        if data_ano is None:
            print(f"Os dados para o ano {ano} não estão disponíveis. Realizando previsão...")
        else:
            # Agrupar por mês e somar os aluguéis
            data_ano_monthly = data_ano.groupby('mes')['aluguel'].sum()

            # Encontrar o melhor e o pior mês do ano
            best_month_ano = data_ano_monthly.idxmax()
            worst_month_ano = data_ano_monthly.idxmin()

            # Exibir os resultados para o ano
            print(f"Melhor mês de {ano}: {months[best_month_ano - 1]}, Pior mês de {ano}: {months[worst_month_ano - 1]}")

            # Gráfico para o ano
            plt.subplot(1, len(anos_intervalo), idx + 1)
            plt.bar(data_ano_monthly.index, data_ano_monthly, color='skyblue')
            plt.title(f'Aluguéis por Mês - {ano}', fontsize=14)
            plt.xlabel('Mês', fontsize=12)
            plt.ylabel('Número de Aluguéis', fontsize=12)

            # Destacar o melhor e pior mês
            plt.bar(best_month_ano, data_ano_monthly[best_month_ano], color='green', label=f'Melhor Mês: {months[best_month_ano-1]}')
            plt.bar(worst_month_ano, data_ano_monthly[worst_month_ano], color='red', label=f'Pior Mês: {months[worst_month_ano-1]}')
            plt.legend(loc='upper right')

    # Salvar o gráfico em um arquivo
    plt.tight_layout()
    plt.savefig('grafico_comparacao.png')
    print(f"O gráfico foi salvo como 'grafico_comparacao.png'.")

# Gerar o gráfico
gerar_grafico(ano_inicial, ano_final)

# Perguntar ao usuário se deseja visualizar o gráfico gerado
mostrar = input("Deseja visualizar o gráfico gerado? (sim/não): ").lower()
if mostrar == "sim":
    # Mostrar o gráfico gerado como uma imagem
    img = Image.open('grafico_comparacao.png')
    img.show()

# Perguntar se o usuário deseja gerar o gráfico novamente
reiniciar = input("Deseja gerar o gráfico novamente? (sim/não): ").lower()
if reiniciar == "sim":
    ano_inicial = int(input("Digite o ano inicial para a comparação: "))
    ano_final = int(input("Digite o ano final para a comparação: "))
    gerar_grafico(ano_inicial, ano_final)

# Perguntar se o usuário deseja sair
sair = input("Deseja sair do programa? (sim/não): ").lower()
if sair == "sim":
    print("Saindo do programa.")
    exit()
