# src/core/revenue_percent.py
"""
Módulo para cálculo e análise de percentuais de faturamento por estado.
"""

from typing import Dict

def calculate_revenue_percentages(revenue_data: Dict[str, float]) -> Dict[str, float]:
    """
    Calcula o percentual de representação de cada estado no faturamento total.
    
    Args:
        revenue_data: Dicionário com estados como chaves e valores de faturamento como valores.
    
    Returns:
        Dicionário com estados como chaves e seus percentuais como valores, além do total.
    """
    total = sum(revenue_data.values())
    percentages = {estado: (valor / total) * 100 for estado, valor in revenue_data.items()}
    percentages['total'] = total  # Adiciona o total ao resultado para uso posterior
    return percentages

def display_revenue_percentages(percentages: Dict[str, float]) -> None:
    """
    Exibe os percentuais de faturamento por estado e o total.
    
    Args:
        percentages: Dicionário com percentuais e o faturamento total.
    """
    print("Percentual de representação por estado:")
    for estado, percentual in percentages.items():
        if estado != 'total':  # Exclui o total da lista de percentuais
            print(f"{estado}: {percentual:.2f}%")
    print(f"\nFaturamento total: R${percentages['total']:.2f}")