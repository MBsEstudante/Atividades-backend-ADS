# Pedindo ao usuário para inserir o valor do salário por hora e o número de horas trabalhadas no mês
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calculando o total do salário no referido mês
salario_total = valor_por_hora * horas_trabalhadas

# Mostrando o total do salário no referido mês
print("O total do seu salário no mês é:", salario_total)
