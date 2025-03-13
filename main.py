import importlib
import os

def listar_modulos():
    modulos = [f[:-3] for f in os.listdir('.') if f.endswith('.py') and f not in ['main.py', '__init__.py']]
    return modulos

def exibir_menu(modulos):
    print("\nSelecione um módulo para executar:")
    for i, mod in enumerate(modulos, 1):
        print(f"{i}. {mod}")
    print("0. Sair")

def executar_modulo(modulo_nome):
    try:
        modulo = importlib.import_module(modulo_nome)
        if hasattr(modulo, 'main'):
            modulo.main()
        else:
            print(f"O módulo {modulo_nome} não possui uma função 'main'.")
    except Exception as e:
        print(f"Erro ao executar {modulo_nome}: {e}")

def main():
    while True:
        modulos = listar_modulos()
        exibir_menu(modulos)
        
        escolha = input("Escolha uma opção: ")
        if escolha == "0":
            print("Saindo...")
            break
        
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(modulos):
                executar_modulo(modulos[escolha - 1])
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

if __name__ == "__main__":
    main()
