#neste alguritemo calculamos as notas de 10 alunos e calculamos a media
soma=0
alunos=10
for _ in range(10):
    nota = int(input("intrudosa uma nota"))
    positiva = 0
    soma = soma + nota
    if nota > 10:
        positiva = positiva + 1
media = soma / 10
print(round(media,2))
print("n de positivas ", positiva)
print("numero de negativas", alunos-positiva)
positivas = positiva/alunos*100
print("persentagem positiva",positivas)
print("perssentagem negativas",(alunos-positiva)*100)