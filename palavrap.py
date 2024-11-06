login="bomdia@email.com"
pas="1243"
t=3
while t>0:
    t=t-1
    log=(input("introduza o gmail"))
    ps=(input("introduza a pass"))
    if log==login and pas==ps:
        print("sessão iniciada")
        break
    elif log!=login:
        print("O gmail é invalido")
    elif log!=login and pas!=ps:
        print("invalido")

