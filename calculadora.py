op="s"
soma=0
while op=="s":
    n1=float(input("Digite um numero"))
    pk=(input("escolha um operador"))
    n2=float(input("digite outro numero"))
    if pk=="+":
        re=n1+n2
        print(re)
    if pk=="-":
        re=n1-n2
        print(re)
    if pk=="/":
        re=n1/n2
        print(re)
    if pk=="*":
        re=n1*n2
        print(re)
    if pk=="somt":
        i1=int(n1)
        i2=int(n2)
        for i in range(n1,n2+1):
         soma = soma + i
         print(soma)
    op=(input("Quer outro"))
    op=op.strip().lower()