import joblib
import pandas as pd
import numpy as np

# Função para carregar o modelo e o scaler
def carregar_modelo():
    modelo = joblib.load('modelo_previsao.pkl')  # Carregar o modelo treinado
    scaler = joblib.load('scaler.pkl')  # Carregar o scaler usado para normalizar os dados
    return modelo, scaler

# Função para fazer a previsão
def fazer_previsao(modelo, scaler, ano_escolhido):
    # Exemplo de dados de entrada (o ano agora é variável)
    dados_exemplo = {
        'dia': [1],
        'mes': [1],
        'ano': [ano_escolhido],  # Ano escolhido pelo usuário
        'temporada': [1],
        'feriado': [0],
        'dia da semana': [5],
        'dia util': [1],
        'previsao do tempo': [1],
        'temperatura': [0.344167],
        'atemp': [0.363625],
        'hum': [0.805833],
        'velocidade do vento': [0.160446]
    }

    # Criar DataFrame com os dados de exemplo
    dados_df = pd.DataFrame(dados_exemplo)

    # Normalizar os dados de entrada (como foi feito no treinamento)
    dados_normalizados = scaler.transform(dados_df)

    # Fazer previsão
    previsao = modelo.predict(dados_normalizados)

    return previsao[0]

# Função principal
def main():
    # Carregar o modelo e o scaler
    modelo, scaler = carregar_modelo()

    # Entrada interativa para o ano
    while True:
        try:
            ano_escolhido = int(input("Digite o ano para a previsão (ex: 2023): "))
            break  # Se a entrada for válida, sai do loop
        except ValueError:
            print("Por favor, insira um número válido para o ano.")

    # Fazer a previsão
    previsao = fazer_previsao(modelo, scaler, ano_escolhido)

    # Exibir a previsão
    print(f"Previsão de aluguel de bicicletas para o ano {ano_escolhido}: {previsao:.2f}")

# Chamar a função principal
if __name__ == "__main__":
    main()
