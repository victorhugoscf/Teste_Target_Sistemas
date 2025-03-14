def display_results(results: dict) -> None:
    """Exibe os resultados da análise de forma formatada."""
    print("\n=== Relatório de Faturamento Mensal ===")
    print(f"Menor valor de faturamento: R$ {results['lowest_value']:,.2f}")
    print(f"Maior valor de faturamento: R$ {results['highest_value']:,.2f}")
    print(f"Número de dias acima da média: {results['days_above_average']}")
    print(f"Média mensal (ref.): R$ {results['monthly_average']:,.2f}")
    print("======================================\n")

def main():
    print("O módulo 'display' é responsável por exibir os resultados de faturamento.")
