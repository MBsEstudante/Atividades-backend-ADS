# Recebendo o número inteiro do usuário
numero_inteiro = int(input("Digite um número inteiro: "))

# Definindo o tamanho desejado para o número formatado
tamanho = 8  # Por exemplo, tamanho 8

# Formatando o número com preenchimento de zeros à esquerda
numero_formatado = f"{numero_inteiro:0{tamanho}d}"

# Mostrando o número formatado
print("Número formatado:", numero_formatado)
