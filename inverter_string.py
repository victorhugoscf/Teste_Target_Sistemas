# teste2.py

import sys
from src.core.inverter import inverter_string

def main():
    string = input("Digite uma string para inverter: ").strip()

    if not string:
        print("Erro: A entrada não pode estar vazia.")
    else:
        print(f"String original: {string}")
        print(f"String invertida: {inverter_string(string)}")

if __name__ == "__main__":
    main()
