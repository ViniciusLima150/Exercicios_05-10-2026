soma = 0
media = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))

    soma += numero

if numero % 2 == 0:
    media = soma / 5
    print(f"A média dos números pares é: {media}")
else:
    print(f"Nem todos os número inseridos são pares, não é possivel calcular a média")