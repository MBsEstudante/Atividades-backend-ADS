# Recebendo o número decimal do usuário
numero_decimal = float(input("Digite um número decimal: "))

# Formatando o número como um valor em dinheiro
valor_em_dinheiro = "{:,.2f}".format(numero_decimal)

# Adicionando o símbolo de R$
valor_em_dinheiro = "R$ " + valor_em_dinheiro

# Mostrando o valor formatado
print("O número em formato de dinheiro é:", valor_em_dinheiro)
