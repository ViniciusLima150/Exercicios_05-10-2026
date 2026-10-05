nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o dano de seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print(nome, "você já é de maior e pode fazer a carteira de motorista.")

elif idade < 18 and idade >= 16:
    print(nome, "você já pode votar.")

else:
    print(nome, "Você é de menor e nem atende aos requisitos de idade para votar.")