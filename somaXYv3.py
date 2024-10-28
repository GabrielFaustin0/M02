#soma todos os valores inteiros
x = int(input("indique o valor a somar"))
y = int(input("indique o limite"))
soma=0
if x < y:
    incremento = 1
else:
    incremento = -1

for i in range(x,y + incremento,incremento):
    soma = soma + i

print(soma)