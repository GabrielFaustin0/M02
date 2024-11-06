n1=int(input("n"))
n2=int(input("n"))
if n1==n2:
    print("iguais")
else:
    print("diferenca")
    d=n1-n2
    if d<0:
        d=d*(-1)
    print(d)