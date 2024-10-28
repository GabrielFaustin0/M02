#soma todos os valores inteiros
x = int(input("indique o valor a somar"))
y = int(input("indique o limite"))
if x > y:
    t=x
    x=y
    y=t
soma = 0
for i in range(x,y+1):
    soma = soma + i 
print(soma)