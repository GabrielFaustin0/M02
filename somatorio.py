x=int(input("digite um numero para o somatorio"))
y=int(input("digite um numero para o somatorio"))
soma=0
for i in range(x,y+1):
    soma = soma + i
print("o somatorio de", x "e de", y "é", soma)