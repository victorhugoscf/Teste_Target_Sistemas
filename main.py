import importlib
import os
import logging
from pathlib import Path

# Configura o logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

def list_modules():
    """
    Lista os módulos presentes em 'src/core', excluindo arquivos específicos e módulos sem 'main'.
    
    Returns:
        List[str]: Lista de nomes dos módulos válidos.
    """
    modules = []
    core_path = Path("src/core")  # Caminho para a pasta 'src/core'
    
    if not core_path.exists():
        logger.error(f"Diretório 'src/core' não encontrado: {core_path}")
        return modules

    for f in core_path.iterdir():
        if f.is_file() and f.suffix == ".py" and f.name not in ["main.py", "__init__.py", "display.py", "logger_config.py"]:
            module_name = f.stem  # Remove a extensão .py
            try:
                # Tenta importar o módulo para verificar se ele possui uma função 'main'
                module = importlib.import_module(f"src.core.{module_name}")
                if hasattr(module, 'main'):
                    modules.append(module_name)
            except Exception as e:
                logger.error(f"Erro ao tentar importar o módulo {module_name}: {e}")
                continue  # Ignora módulos que não podem ser importados ou não têm 'main'
    
    return modules

def display_menu(modules):
    """
    Exibe o menu de opções para o usuário com os títulos em português e na ordem correta.
    
    Args:
        modules (List[str]): Lista de nomes dos módulos válidos.
    """
    # Mapeia os nomes dos módulos para títulos em português e define a ordem correta
    titulos_ordenados = [
        ("calculate_triangular_number", "1. Calcular Número Triangular"),
        ("calculate_fibonacci_until", "2. Calcular Sequência de Fibonacci"),
        ("analyzer", "3. Analisador de Faturamento"),
        ("revenue_percent", "4. Percentual de Faturamento por Estado"),
        ("inverter", "5. Inversor de String")
    ]

    print("\n=== Menu de resoluções ===")
    print("Selecione um desafio para executar:")
    
    # Exibe os títulos na ordem correta
    for module_name, titulo in titulos_ordenados:
        if module_name in modules:
            print(titulo)
    print("0. Sair")

def run_module(module_name):
    """
    Executa o módulo selecionado pelo usuário.
    
    Args:
        module_name (str): Nome do módulo a ser executado.
    """
    try:
        # Importa o módulo a partir de src.core
        module = importlib.import_module(f"src.core.{module_name}")
        if hasattr(module, 'main'):
            logger.info(f"Executando o módulo {module_name}...")
            module.main()
        else:
            logger.warning(f"O módulo {module_name} não possui uma função 'main'.")
            print(f"O módulo {module_name} não possui uma função 'main'.")
    except Exception as e:
        logger.error(f"Erro ao executar o módulo {module_name}: {e}")
        print(f"Erro ao executar o módulo {module_name}: {e}")

def main():
    """Função principal que exibe o menu e gerencia a execução do programa."""
    while True:
        logger.info("Listando módulos disponíveis...")
        modules = list_modules()
        
        if not modules:
            logger.error("Nenhum módulo válido encontrado. Verifique o diretório 'src/core'.")
            print("Nenhum módulo válido encontrado. Verifique o diretório 'src/core'.")
            break
        
        display_menu(modules)
        choice = input("Escolha uma opção: ")
        
        if choice == "0":
            logger.info("Saindo do sistema...")
            print("Saindo...")
            break
        
        try:
            choice = int(choice)
            # Mapeia a escolha numérica para o nome do módulo
            titulos_ordenados = [
                ("calculate_triangular_number", "1. Calcular Número Triangular"),
                ("calculate_fibonacci_until", "2. Calcular Sequência de Fibonacci"),
                ("analyzer", "3. Analisador de Faturamento"),
                ("revenue_percent", "4. Percentual de Faturamento por Estado"),
                ("inverter", "5. Inversor de String")
            ]
            
            if 1 <= choice <= len(titulos_ordenados):
                module_name, _ = titulos_ordenados[choice - 1]
                if module_name in modules:
                    run_module(module_name)
                else:
                    logger.warning(f"O módulo {module_name} não está disponível.")
                    print(f"O módulo {module_name} não está disponível.")
            else:
                logger.warning("Opção inválida. O usuário escolheu uma opção que não está no menu.")
                print("Opção inválida. Tente novamente.")
        except ValueError:
            logger.warning("Entrada inválida. O usuário não digitou um número válido.")
            print("Entrada inválida. Por favor, insira um número.")

if __name__ == "__main__":
    main()
    