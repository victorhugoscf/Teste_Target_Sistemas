"""
Módulo contendo a lógica de análise de faturamento diário.
"""

import json
from typing import Dict, List
from pathlib import Path

class RevenueAnalyzer:
    """Classe responsável por analisar dados de faturamento diário."""

    def __init__(self, file_path: str = "utilities/dados.json"):
        """Inicializa o analisador com o caminho do arquivo JSON."""
        self.file_path = Path(file_path)
        self.data: List[Dict] = []
    
    def load_data(self) -> None:
        """Carrega os dados do arquivo JSON."""
        try:
            with self.file_path.open('r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {self.file_path} não foi encontrado.")
        except json.JSONDecodeError:
            raise ValueError(f"Erro ao decodificar o arquivo JSON: {self.file_path}")
        except Exception as e:
            raise Exception(f"Erro inesperado ao carregar dados: {str(e)}")
    
    def analyze_revenue(self) -> Dict[str, float]:
        """
        Analisa o faturamento e retorna os resultados solicitados.
        
        Retorna:
            Dicionário com menor_valor, maior_valor, dias_acima_da_media e media_mensal.
        """
        if not self.data:
            raise ValueError("Nenhum dado carregado para análise")
        
        # Filtra dias com faturamento válido (> 0)
        valid_revenues = [
            record['valor'] for record in self.data 
            if record.get('valor', 0) > 0
        ]
        
        if not valid_revenues:
            raise ValueError("Nenhum dia com faturamento válido encontrado")
        
        # Cálculos
        lowest_value = min(valid_revenues)
        highest_value = max(valid_revenues)
        monthly_average = sum(valid_revenues) / len(valid_revenues)
        days_above_average = sum(
            1 for record in self.data 
            if record.get('valor', 0) > monthly_average
        )
        
        return {
            'lowest_value': lowest_value,
            'highest_value': highest_value,
            'days_above_average': days_above_average,
            'monthly_average': monthly_average
        }

def format_currency(value: float) -> str:
    """
    Formata um valor float como dinheiro em BRL (Reais).
    
    Args:
        value (float): Valor a ser formatado.
        
    Returns:
        str: Valor formatado como "R$ X.XXX,XX".
    """
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    """Função principal para execução do módulo Analyzer."""
    try:
        analyzer = RevenueAnalyzer()
        analyzer.load_data()  # Carrega os dados do arquivo JSON
        result = analyzer.analyze_revenue()  # Realiza a análise de faturamento
        
        # Formata os valores como dinheiro em BRL
        lowest_value_brl = format_currency(result['lowest_value'])
        highest_value_brl = format_currency(result['highest_value'])
        monthly_average_brl = format_currency(result['monthly_average'])
        
        # Exibe os resultados
        print("\nResultados da Análise de Faturamento:")
        print(f"Menor valor: {lowest_value_brl}")
        print(f"Maior valor: {highest_value_brl}")
        print(f"Dias acima da média: {result['days_above_average']}")
        print(f"Média mensal: {monthly_average_brl}")
        
    except Exception as e:
        print(f"Erro ao executar a análise: {e}")

if __name__ == "__main__":
    main()