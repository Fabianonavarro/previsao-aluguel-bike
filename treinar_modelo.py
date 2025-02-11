import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Função para carregar os dados
def carregar_dados():
    # Carregar os dados do arquivo CSV
    data = pd.read_csv('bike-data/bike-share.csv')
    return data

# Função para pré-processamento de dados
def preprocessar_dados(data):
    # Verificar se há valores ausentes
    if data.isnull().sum().any():
        print("Aviso: Existem valores ausentes nos dados. Tratando-os...")
        data = data.fillna(data.mean())  # Substituir valores ausentes pela média (caso existam)
    
    # Separar os dados em X (variáveis preditoras) e y (alvo)
    X = data.drop('aluguel', axis=1)  # Remover a coluna 'aluguel', que é o alvo
    y = data['aluguel']
    
    # Se houver colunas categóricas, você pode aplicar uma transformação aqui (exemplo com one-hot encoding)
    X = pd.get_dummies(X, drop_first=True)  # Converte variáveis categóricas em variáveis numéricas

    return X, y

# Função para treinar o modelo
def treinar_modelo():
    # Carregar os dados
    data = carregar_dados()
    
    # Pré-processar os dados
    X, y = preprocessar_dados(data)
    
    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Normalizar os dados (opcional, mas pode ajudar com alguns modelos)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Criar e treinar o modelo de regressão linear
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    # Avaliar o modelo (opcional)
    score = modelo.score(X_test, y_test)
    print(f"Acurácia do modelo: {score * 100:.2f}%")
    
    # Salvar o modelo treinado e o scaler (caso queira usar para previsões futuras)
    joblib.dump(modelo, 'modelo_previsao.pkl')
    joblib.dump(scaler, 'scaler.pkl')
    
    print("Modelo treinado e salvo com sucesso!")

# Chamar a função principal
if __name__ == "__main__":
    treinar_modelo()
