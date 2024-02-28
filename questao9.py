# Solicitando ao usuário o dia, o mês e o ano de nascimento
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

# Formatando a data de nascimento
data_nascimento = f"{dia:02d}/{mes:02d}/{ano}"

# Exibindo a data de nascimento formatada
print("Data de nascimento:", data_nascimento)
