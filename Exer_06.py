maior_idade = -1
nome_velho = ""

for i in range(1, 6):
    idade, nome = int(input(f"Digite a idade da {i}ª pessoa: ")), input(f"Digite o nome da {i}ª pessoa: ")
    if idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
        
print(f"{nome_velho} é o mais velho com {maior_idade} anos")