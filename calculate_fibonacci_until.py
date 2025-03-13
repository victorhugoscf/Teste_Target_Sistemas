from typing import Tuple, List
import sys

class FibonacciChecker:
    """Classe para verificar se um número pertence à sequência de Fibonacci."""
    
    @staticmethod
    def calculate_fibonacci_until(target: int) -> Tuple[bool, List[int]]:
        """
        Calcula a sequência de Fibonacci até alcançar ou ultrapassar o número alvo.
        
        Args:
            target (int): Número a ser verificado
            
        Returns:
            Tuple[bool, List[int]]: (pertence_sequencia, sequencia_calculada)
            
        Raises:
            ValueError: Se o número for negativo
        """
        if target < 0:
            raise ValueError("Números negativos não pertencem à sequência de Fibonacci")
            
        # Casos base
        if target == 0:
            return True, [0]
        if target == 1:
            return True, [0, 1]
            
        # Inicializa a sequência
        sequence = [0, 1]
        while sequence[-1] < target:
            next_value = sequence[-1] + sequence[-2]
            sequence.append(next_value)
            if next_value == target:
                return True, sequence
                
        return False, sequence

    @classmethod
    def check_number(cls, number: int) -> str:
        """
        Verifica se o número pertence à sequência e retorna mensagem formatada.
        
        Args:
            number (int): Número a ser analisado
            
        Returns:
            str: Mensagem com resultado da análise
        """
        try:
            is_fib, sequence = cls.calculate_fibonacci_until(number)
            sequence_str = ", ".join(map(str, sequence))
            
            if is_fib:
                position = len(sequence) - 1
                return (
                    f"O número {number} PERTENCE à sequência de Fibonacci!\n"
                    f"Posição na sequência (iniciando em 0): {position}\n"
                    f"Sequência até este ponto: {sequence_str}"
                )
            else:
                return (
                    f"O número {number} NÃO pertence à sequência de Fibonacci.\n"
                    f"Ele está entre {sequence[-2]} e {sequence[-1]}\n"
                    f"Sequência calculada: {sequence_str}"
                )
                
        except ValueError as e:
            return f"Erro: {str(e)}"

def get_user_input() -> int:
    """
    Obtém e valida a entrada do usuário.
    
    Returns:
        int: Número informado pelo usuário
        
    Raises:
        SystemExit: Se a entrada for inválida após tentativas
    """
    attempts = 3
    while attempts > 0:
        try:
            user_input = input("Digite um número inteiro para verificar: ").strip()
            return int(user_input)
        except ValueError:
            attempts -= 1
            print(f"Entrada inválida! Restam {attempts} tentativas.")
    
    print("Número máximo de tentativas excedido.")
    sys.exit(1)

def main():
    """Função principal do programa."""
    print("=== Verificador de Sequência de Fibonacci ===")
    print("Este programa verifica se um número pertence à sequência de Fibonacci")
    print("Sequência exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...")
    print("==========================================\n")
    
    try:
        number = get_user_input()
        checker = FibonacciChecker()
        result = checker.check_number(number)
        print("\nResultado:")
        print(result)
        
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()