#neste alguritemo calculamos as notas de 10 alunos e calculamos a media
soma=0
for _ in range(10):
    nota = int(input("intrudosa uma nota"))
    soma = soma + nota
media = soma / 10
print(media)