# Teste Prático: Soluções em Python

Este repositório contém a implementação de 5 desafios práticos em Python. Cada desafio resolve um problema específico.

## Desafios Implementados

1. **Cálculo do Número Triangular**  
   Calcula o n-ésimo número triangular, que é a soma dos números de 1 até n.

2. **Verificação de Número na Sequência de Fibonacci**  
   Verifica se um número pertence à sequência de Fibonacci e exibe a sequência até o número informado.

3. **Análise de Faturamento Diário**  
   Analisa um conjunto de dados de faturamento diário, calculando o menor valor, o maior valor e o número de dias em que o faturamento foi superior à média mensal.

4. **Percentual de Faturamento por Estado**  
   Calcula o percentual de representação de cada estado no faturamento total de uma distribuidora, com base em dados fornecidos.

5. **Inversão de String**  
   Inverte os caracteres de uma string sem utilizar funções prontas, como `reverse`.

## Estrutura do Projeto

A estrutura deste projeto foi cuidadosamente projetada para promover boas práticas de desenvolvimento e facilitar a escalabilidade. A separação entre código, dados e módulos reutilizáveis proporciona uma organização modular que facilita a manutenção e o crescimento do sistema. Cada desafio é isolado em um arquivo principal, enquanto os módulos essenciais são centralizados na pasta `src/core/`, tornando o código mais reutilizável e fácil de expandir.

A estrutura de pastas é a seguinte:

```
meu_projeto/
├── main.py                  # Arquivo principal 
├── utilities/               # Pasta contendo dados auxiliares
│   └── dados.json           # Arquivo JSON com dados de faturamento diário
│   └── faturamento_estados.json	# Arquivo JSON com dados de faturamento dos estados
└── src/                     # Pasta com módulos reutilizáveis
    └── core/                # Módulos principais
        ├── __init__.py          # Arquivo vazio para marcar o diretório como módulo
        ├── calculate_triangular_number.py   # Módulo para cálculo do número triangular
        ├── calculate_fibonacci_until.py     # Módulo para cálculo e verificação da sequência de Fibonacci
        ├── analyzer.py             # Módulo com a lógica de análise de faturamento diário
        ├── revenue_percent.py      # Módulo para cálculo e exibição de percentuais por estado
        └── inverter.py            # Módulo para inversão de strings
```

### A Estrutura Escalável

A separação clara entre os módulos no diretório `src/core/` permite que o projeto cresça de forma organizada. Aqui estão algumas razões pelas quais esta estrutura é escalável:

1. **Modularidade**: Cada desafio é encapsulado em um arquivo ou módulo específico, o que permite que novos desafios ou funcionalidades sejam adicionados sem impactar o restante do projeto. Por exemplo, se no futuro você desejar adicionar mais cálculos ou funcionalidades, pode criar novos módulos de forma independente.
   
2. **Reutilização**: Os módulos em `src/core/` são reutilizáveis em diferentes contextos, o que facilita a manutenção do código e reduz a duplicação. Por exemplo, a lógica de cálculo do número triangular ou de Fibonacci pode ser utilizada em novos projetos ou módulos sem a necessidade de reescrever o código.

3. **Organização Lógica**: A pasta `src/core/` abriga a lógica principal do projeto, mantendo o código limpo e organizado. Os módulos são nomeados de maneira a refletir sua funcionalidade, facilitando a localização e o entendimento do código. Além disso, a pasta `utilities/` armazena arquivos auxiliares, como os dados de faturamento, evitando que eles se misturem com a lógica do código.

4. **Expansão Futura**: Caso o projeto precise ser expandido com novas funcionalidades (como relatórios adicionais, integração com bancos de dados ou novas análises de dados), a estrutura atual permite que essas expansões sejam realizadas de forma simples e sem complicação. Módulos podem ser criados para novas funcionalidades e integrados facilmente.

## Instruções de Uso

### Pré-requisitos
- Python 3.6 ou superior instalado.

### Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/victorhugoscf/Teste_Target_Sistemas.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Teste_Target_Sistemas-main
   ```

### Execução

- **Desafio 1 - Cálculo do Número Triangular**  
   ```bash
   python main.py
   ```

---
 
Victor  
<victorhugoscf@gmail.com>


>


