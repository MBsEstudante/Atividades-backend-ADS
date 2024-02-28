# Pedindo ao usuário para inserir um número inteiro, um número decimal e um número do tipo texto
numero_inteiro = int(input("Digite um número inteiro: "))
numero_decimal = float(input("Digite um número decimal: "))
numero_texto = input("Digite um número em formato de texto: ")

# Convertendo os números
inteiro_para_decimal = float(numero_inteiro)
decimal_para_texto = str(numero_decimal)
texto_para_inteiro = int(numero_texto)

# Mostrando os resultados e suas classificações de tipo
print("Resultado da conversão:")
print("Número inteiro convertido para decimal:", inteiro_para_decimal, "Tipo:", type(inteiro_para_decimal))
print("Número decimal convertido para texto:", decimal_para_texto, "Tipo:", type(decimal_para_texto))
print("Número em texto convertido para inteiro:", texto_para_inteiro, "Tipo:", type(texto_para_inteiro))
