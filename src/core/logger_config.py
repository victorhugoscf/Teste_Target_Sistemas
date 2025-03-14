"""
Configuração de logging para o projeto.
"""

import logging

def configure_logging():
    """Configura o logging para o projeto, garantindo que não seja reconfigurado."""
    logger = logging.getLogger()
    
    # Verifica se o logging já foi configurado
    if not logger.hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    return logger
