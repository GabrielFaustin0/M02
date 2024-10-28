#este programa faz a media entre os numeros 20 e 
soma=0
contar=0
for i in range(20):
    n=int(input("digite um numero inteiro"))
    if n>=20 and n<=50:
        soma=soma+n
        contar=contar+1
media=soma/contar
print("A media dos n entre 20 e 50 foi de", media)

