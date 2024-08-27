# Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, Venda e Relatorio, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes.
# Classe Venda:
# Já está definida e contém as informações sobre uma venda, como produto, quantidade e valor.
# Classe Relatorio:
# Você precisa implementar o método adicionar_venda, que deve verificar se o objeto passado é uma instância da classe Venda antes de adicioná-lo à lista de vendas.
# Também, no método calcular_total_vendas, você deve calcular o total de vendas multiplicando a quantidade pelo valor de cada venda adicionada ao relatório.
# Função main:
# Você deverá implementar a lógica para exibir o total de vendas utilizando o método calcular_total_vendas da classe Relatorio.

# Entrada
# A entrada consiste em dados de vendas com as seguintes colunas:

# Produto (string)
# Quantidade (inteiro)
# Valor (decimal)
# Saída
# A saída é o total de vendas calculado pela classe Relatorio.

# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	                                                          Saída
# Notebook
# 3
# 1500.00
# Mouse
# 10
# 50.00
# Teclado
# 5
# 100.00	                                                         Total de Vendas: 5500.0

# Monitor
# 2
# 800.00
# Webcam
# 1
# 120.00
# Fone de Ouvido
# 4
# 75.00	                                                          Total de Vendas: 2020.0


# Impressora
# 1
# 350.00
# Cartucho
# 3
# 60.00
# Scanner
# 2
# 200.00	                                                        Total de Vendas: 930.0


class Venda:
    def __init__(self, produto, quantidade, valor):
        # Inicializa uma nova instância da classe Venda com produto, quantidade e valor
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        # Inicializa uma nova instância da classe Relatorio com uma lista vazia de vendas
        self.vendas = []

    def adicionar_venda(self, venda):
        # Verifica se o objeto passado é uma instância da classe Venda
        if isinstance(venda, Venda):
            # Adiciona a venda à lista de vendas se a verificação for verdadeira
            self.vendas.append(venda)

    def calcular_total_vendas(self):
        # Inicializa a variável total para armazenar o total de vendas calculado
        total = 0
        # Itera sobre todas as vendas na lista de vendas
        for venda in self.vendas:
            # Calcula o valor total para cada venda multiplicando a quantidade pelo valor unitário e adiciona ao total
            total += venda.quantidade * venda.valor
        # Retorna o total acumulado de vendas
        return total

def main():
    # Cria uma instância da classe Relatorio
    relatorio = Relatorio()
    
    # Leitura das vendas (assume que haverá 3 vendas para este exemplo)
    for _ in range(3):  # Laço que itera 3 vezes para ler os dados das 3 vendas
        produto = input().strip()  # Lê o nome do produto e remove espaços em branco extras
        quantidade = int(input().strip())  # Lê a quantidade, converte para inteiro e remove espaços em branco extras
        valor = float(input().strip())  # Lê o valor, converte para float e remove espaços em branco extras
        venda = Venda(produto, quantidade, valor)  # Cria uma nova instância da classe Venda com os dados lidos
        relatorio.adicionar_venda(venda)  # Adiciona a nova venda ao relatório
    
    # Exibe o total de vendas
    total_vendas = relatorio.calcular_total_vendas()  # Calcula o total de vendas usando o método calcular_total_vendas
    print(f'Total de Vendas: {total_vendas:.1f}')  # Imprime o total de vendas formatado com uma casa decimal

if __name__ == "__main__":
    main()  # Chama a função main para executar o programa se o script for executado diretamente

