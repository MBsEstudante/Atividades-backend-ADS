# Recebendo o nome e o telefone do usuário
nome = input("Digite o nome: ")
telefone = int(input("Digite o telefone: "))

# Usando vírgula para separar o nome e o telefone
saida_virgula = nome + ", " + str(telefone)

# Usando concatenação para unir o nome e o telefone
saida_concatenacao = nome + " " + str(telefone)

# Usando f-string para formatar o nome e o telefone
saida_f_string = f"{nome}, {telefone}"

# Usando o método format para formatar o nome e o telefone
saida_format = "{}, {}".format(nome, telefone)

# Exibindo as saídas
print("Saída com vírgula:", saida_virgula)
print("Saída com concatenação:", saida_concatenacao)
print("Saída com f-string:", saida_f_string)
print("Saída com método format:", saida_format)
