soma_pares = 0
soma_impares = 0
total_pares = 0
total_impares = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
  
    if numero % 2 == 0:
        soma_pares += numero
        total_pares += 1
    else:
        soma_impares += numero
        total_impares += 1

print(f"A soma dos números pares é: {soma_pares}")
print(f"A soma dos números ímpares é: {soma_impares}")
print(f"O total de números pares é: {total_pares}")
print(f"O total de números ímpares é: {total_impares}")