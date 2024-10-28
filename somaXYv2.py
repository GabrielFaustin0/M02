#soma todos os valores inteiros
x = int(input("indique o valor a somar"))
y = int(input("indique o limite"))
soma=0
if x < y:
    for i in range(x,y+1):
        soma = soma + i
else:
    for i in range(y,x+1):
        soma = soma + i

print(soma)