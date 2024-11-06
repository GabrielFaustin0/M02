op=None
nc=12
o1=1
o2=0
o3=0
while op!="4":
    print("tem,",nc,"restantes na carta")
    print("1. Infração muito grave")
    print("2. Infração grave")
    print("3. Infração leve")
    print("4. Terminar")
    op=input("")
    if op=="1":
        nc=nc-6
        o3=o3+1
        continue
    elif op=="2":
        nc=nc-4
        o2=o2+1
        continue
    elif op=="3":
        if o1!=1:
            nc=nc-1
    if nc<=0:
        print("voce perdeu a carta")