#soma os numeros pares
soma=0
for i in range(1,101):
    if i % 2 == 0:
        soma = soma + i
print(soma)