palavra=input("intrudusa uma palavra")
inv=""
for i in range(len(palavra)-1,-1,-1 ):
    inv=inv+palavra[i]
print(inv)
if inv == palavra:
    print("é um palindromo")
else:
    print("nao é um palindromo")