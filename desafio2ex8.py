B=int(input("digite com quantas bacterias tem no final do mes"))
Ba=B % 2
T=0
while Ba==0:
    Ba=B/2                     
    T=T+1
print(T,"dias")
print("Começou com",int(Ba),"bactérias")