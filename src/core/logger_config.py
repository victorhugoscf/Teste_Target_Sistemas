# src/core/logger_config.py
"""
Configuração de logging para o projeto.
"""

import logging

def configure_logging():
    """Configura o logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)