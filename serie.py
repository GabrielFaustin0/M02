o=int(input("Quantos numero par da serie de fibonnachi quer"))
n1=0
n2=1
o=o//2
for i in range(o):
    print(n1,n2)
    n1=n1+n2
    n2=n2+n1
