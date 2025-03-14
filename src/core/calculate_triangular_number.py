class TriangularNumberCalculator:
    """Classe para calcular números triangulares."""

    @staticmethod
    def calculate_triangular_number(n: int) -> int:
        """
        Calcula o n-ésimo número triangular (soma dos números de 1 até n).
        
        Args:
            n (int): O índice limite para o cálculo da soma
            
        Returns:
            int: O n-ésimo número triangular
            
        Raises:
            ValueError: Se o número for negativo
        """
        if n < 0:
            raise ValueError("O valor de n não pode ser negativo")
        
        # Fórmula para o número triangular
        return n * (n + 1) // 2


def main():
    """Função principal do programa."""

    try:
        # Define o índice
        INDEX = 13
        
        # Calcula o número triangular para o índice 13
        triangular_number = TriangularNumberCalculator.calculate_triangular_number(INDEX)
        print("=======================================\n")
        print(f"Resultado: {triangular_number}\n")
        print("=======================================\n")
        
    except Exception as e:
        print(f"\nErro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    