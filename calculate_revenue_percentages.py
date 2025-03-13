# teste.py
"""
Programa para análise de percentuais de faturamento por estado.
"""

from src.core.revenue_percent import calculate_revenue_percentages, display_revenue_percentages

def main() -> None:
    """Função principal do programa."""
    # Dados de faturamento por estado
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    
    # Calcula os percentuais
    resultados = calculate_revenue_percentages(faturamento)
    
    # Exibe os resultados
    display_revenue_percentages(resultados)

if __name__ == "__main__":
    main()