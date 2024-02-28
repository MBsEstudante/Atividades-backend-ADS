# Recebendo os dados da pessoa
nome = input("Digite o nome da pessoa: ")
idade = int(input("Digite a idade da pessoa: "))
nacionalidade = input("Digite a nacionalidade da pessoa: ")
hobby = input("Digite o hobby da pessoa: ")

# Imprimindo os dados formatados
print(f"Nome: {nome}, Idade: {idade}, Nacionalidade: {nacionalidade}".format(), "Hobby:", hobby)
