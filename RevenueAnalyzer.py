"""
Programa para análise de faturamento diário de uma distribuidora.
Calcula o menor valor, o maior valor e o número de dias com faturamento
acima da média mensal, utilizando dados de um arquivo JSON.

Requisitos:
- Ignorar dias sem faturamento (valor = 0) no cálculo da média.
- Utilizar utilities/dados.json como fonte de dados.
"""

import json
from typing import Dict, List
from pathlib import Path
import logging

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

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
            logger.info(f"Dados carregados com sucesso de {self.file_path}")
        except FileNotFoundError:
            logger.error(f"Arquivo {self.file_path} não encontrado")
            raise
        except json.JSONDecodeError:
            logger.error("Erro ao decodificar o arquivo JSON")
            raise
        except Exception as e:
            logger.error(f"Erro inesperado ao carregar dados: {str(e)}")
            raise
    
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
            if record['valor'] > 0
        ]
        
        if not valid_revenues:
            raise ValueError("Nenhum dia com faturamento válido encontrado")
        
        # Cálculos
        lowest_value = min(valid_revenues)
        highest_value = max(valid_revenues)
        monthly_average = sum(valid_revenues) / len(valid_revenues)
        days_above_average = sum(
            1 for record in self.data 
            if record['valor'] > monthly_average
        )
        
        results = {
            'lowest_value': lowest_value,
            'highest_value': highest_value,
            'days_above_average': days_above_average,
            'monthly_average': monthly_average
        }
        
        logger.info("Análise de faturamento concluída com sucesso")
        return results

def display_results(results: Dict[str, float]) -> None:
    """Exibe os resultados da análise de forma formatada."""
    try:
        print("\n=== Relatório de Faturamento Mensal ===")
        print(f"Menor valor de faturamento: R$ {results['lowest_value']:,.2f}")
        print(f"Maior valor de faturamento: R$ {results['highest_value']:,.2f}")
        print(f"Número de dias acima da média: {results['days_above_average']}")
        print(f"Média mensal (ref.): R$ {results['monthly_average']:,.2f}")
        print("======================================\n")
    except KeyError as e:
        logger.error(f"Erro ao exibir resultados: chave {e} não encontrada")
        raise

def main() -> None:
    """Função principal do programa."""
    try:
        # Inicializa o analisador
        analyzer = RevenueAnalyzer()
        
        # Carrega e analisa os dados
        analyzer.load_data()
        results = analyzer.analyze_revenue()
        
        # Exibe os resultados
        display_results(results)
        
    except FileNotFoundError:
        logger.error("Programa encerrado devido a arquivo não encontrado")
    except ValueError as e:
        logger.error(f"Erro de validação: {str(e)}")
    except Exception as e:
        logger.error(f"Erro inesperado no programa: {str(e)}")
        raise

if __name__ == "__main__":
    main()