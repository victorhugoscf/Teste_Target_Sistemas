"""
Módulo para cálculo e análise de percentuais de faturamento por estado.
"""

import json
from typing import Dict
from pathlib import Path
import locale

# Configura o locale para pt_BR (formato brasileiro)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_currency(value: float) -> str:
    """
    Formata um valor float como dinheiro em BRL (Reais).
    
    Args:
        value (float): Valor a ser formatado.
        
    Returns:
        str: Valor formatado como "R$ X.XXX,XX".
    """
    return locale.currency(value, grouping=True)

def load_revenue_data(file_path: str = "utilities/faturamento_estados.json") -> Dict[str, float]:
    """
    Carrega os dados de faturamento por estado a partir de um arquivo JSON.
    
    Args:
        file_path: Caminho do arquivo JSON.
    
    Returns:
        Dicionário com estados como chaves e valores de faturamento como valores.
    
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado.
        json.JSONDecodeError: Se o arquivo JSON estiver mal formatado.
    """
    path = Path(file_path)
    try:
        with path.open('r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {file_path} não encontrado.")
    except json.JSONDecodeError:
        raise ValueError(f"Erro ao decodificar o arquivo JSON: {file_path}")

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
    
    # Formata o faturamento total como dinheiro
    total_brl = format_currency(percentages['total'])
    print(f"\nFaturamento total: {total_brl}")

def main():
    """Função principal que carrega os dados do JSON e exibe os percentuais."""
    try:
        # Carrega os dados de faturamento do arquivo JSON
        revenue_data = load_revenue_data()
        
        # Calcula os percentuais de faturamento
        percentages = calculate_revenue_percentages(revenue_data)
        
        # Exibe os resultados
        display_revenue_percentages(percentages)
    
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar o arquivo JSON: {e}")
    except Exception as e:
        print(f"Erro inesperado ao executar a análise: {e}")

if __name__ == "__main__":
    main()
    