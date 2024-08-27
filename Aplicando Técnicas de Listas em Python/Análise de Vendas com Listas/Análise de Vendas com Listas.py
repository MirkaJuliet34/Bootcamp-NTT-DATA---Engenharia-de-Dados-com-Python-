def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input().strip()  # Remove espaços extras ao redor da entrada
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split(',')))
    return vendas

def analise_vendas(vendas):
    # Calcula o total de vendas
    total_vendas = sum(vendas)
    # Calcula a média mensal de vendas
    media_vendas = total_vendas / len(vendas)
    # Retorna o total de vendas e a média mensal formatados
    return f"{total_vendas}, {media_vendas:.2f}"

# Obtém a lista de vendas do usuário
vendas = obter_entrada_vendas()
# Analisa as vendas e imprime o resultado
print(analise_vendas(vendas))
