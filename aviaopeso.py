contarmalas=0
limitepeso=1000
while limitepeso>=0:
    pesomala=float(input("peso da mala"))
    if pesomala>limitepeso:
        break
    contarmalas=contarmalas+1
    limitepeso=limitepeso-pesomala
    print("ainda pode transportar mais",limitepeso,"Kg")
print("O valor a cobrar pelo trasporte das malas é de",contarmalas*20,"€")