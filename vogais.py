#contar vogais de uma frase
frase=input("insira uma frase")
contar=0
for letra in frase:
    if letra in "aeiou":
        contar=contar+1
print("a frase tem",contar,"vogais")