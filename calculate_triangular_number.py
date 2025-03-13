def calculate_triangular_number(n: int) -> int:
    """
    Calcula o n-ésimo número triangular (soma dos números de 1 até n).
    
    Args:
        n (int): O índice limite para o cálculo da soma
        
    Returns:
        int: A soma dos números de 1 até n
    """
    sum_result = 0
    for number in range(1, n + 1):
        sum_result += number
    return sum_result

def main():
    """Função principal do programa."""
    INDEX = 13
    result = calculate_triangular_number(INDEX)
    print(f"A soma dos números de 1 até {INDEX} é: {result}")

if __name__ == "__main__":
    main()