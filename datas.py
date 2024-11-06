dia=int(input("digite o dia"))
mes=int(input("digite o mes"))
ano=int(input("digite o ano"))
mes2=None
ano2=None
for i in range(mes,13):
   
    if mes =="1"or mes =="3"or mes =="5"or mes =="7"or mes =="8"or mes =="10"or mes =="12":
        mes2=31
    elif mes==2:
        if(ano%4 == 0 and ano %100 !=0) or ano % 400 == 0:
          mes2=29
          ano2=366
        else:
          mes2=28
          ano2=365
    else:
        mes2=30
    faltam=mes
    dia=0
    mes2=mes2+faltam
   
print("faltao",mes2,"dias")

