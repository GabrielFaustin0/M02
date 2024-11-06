contar=0
for i in range (10):
    frase=(input("escreva uma frase"))
    frase = frase.strip()
    if frase !=1:
        print("so pode haver uma letra")
    for letra in frase:
        if letra in "aeiou":
            contar=contar+1
print("a frase tem",contar,"vogais")