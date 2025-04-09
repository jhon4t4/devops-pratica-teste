# Lista com os valores de vendas realizadas em cada semana do mês
vendas_mensais = [100, 200, 300]  

# Função que recebe uma lista de valores e retorna a soma total
def calcular_total_vendas(vendas):
    return sum(vendas)

# Função que gera um relatório simples com o total de vendas
def gerar_relatorio():
    total = calcular_total_vendas(vendas_mensais)
    print("Relatório de vendas - Março")
    print("Total de vendas: R$", total)

# Executa a função principal
if __name__ == "__main__":
    gerar_relatorio()
