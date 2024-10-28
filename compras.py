orc=float(input(" diga o seu orssamento"))
peso=float(input(" diga o peso que pode levar"))
while orc>0 or peso>0:
    preço=float(input(" diga o preço do produto"))
    peso_prod=float(input("indique o peso do produto comprado"))
    if preço==0:
        break
    if orc < preço or peso<peso_prod:
        print("não tem dinheiro")
    else:
        orc=orc-preço
        peso=peso-peso_prod
    print("Ainda tem",orc,"€ e ainda pode carregar mais", peso,"Kg")
print("acabou as compras")