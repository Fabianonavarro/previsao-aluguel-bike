import subprocess

def menu():
    while True:
        print("\nMenu de Opções:")
        print("1. Rodar Análise Preditiva")
        print("2. Rodar Análise Preditiva 2025")
        print("3. Comparar Aluguéis por Mês")
        print("4. Gerar Gráficos de Estatísticas de Aluguéis")
        print("5. Prever Aluguel")
        print("6. Treinar Modelo de Regressão Linear")
        print("7. Sair")
        
        opcao = input("Escolha uma opção (1-7): ")
        
        if opcao == '1':
            subprocess.run(["python", "analise_ preditiva.py"])  # Rodar Análise Preditiva
        elif opcao == '2':
            subprocess.run(["python", "analise_ preditiva_2025.py"])  # Rodar Análise Preditiva 2025
        elif opcao == '3':
            subprocess.run(["python", "comparacao_mes.py"])  # Comparação mensal
        elif opcao == '4':
            subprocess.run(["python", "grafico_estatisticas.py"])  # Gerar Gráficos de Estatísticas
        elif opcao == '5':
            subprocess.run(["python", "prever_aluguel.py"])  # Prever Aluguel
        elif opcao == '6':
            subprocess.run(["python", "treinar_modelo.py"])  # Treinar o modelo
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Rodar o menu
if __name__ == "__main__":
    menu()
