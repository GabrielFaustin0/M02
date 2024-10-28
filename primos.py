#um programa qu pede ao utilisdor um numero inteiro e dz se o mesmo é primo
numero=int(input("digite um numero inteiro"))
primo=True
for x in range(2,numero):
    if numero % x == 0:
        primo = False
        break
if primo ==True:
    print("o numero", numero, "é primo")
else:
    print("o numero ", numero, "nao é primo")