nomes1=input("digite um nome")
nomes2=input("digite outro nome")
n1=len(nomes1)
n2=len(nomes2)
if n1 == n2:
    print("os nomes tem as mesmas letras")
elif n1 > n2:
    print("o", nomes1, "é maior do que o", nomes2)
else:
    print("o", nomes2, "é maior do que o", nomes1)