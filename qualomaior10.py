pos_maior=1
for i in range (10):
    n=int(input("inssira um numero"))
    if i==0:
        maior=n
    else:
        if n>maior:
            maior=n
            pos_maior=i+1
print("omaior é",maior,"e foi o ",pos_maior,"º a ser incerido")