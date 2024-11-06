melhor_nota=-1
numero_aluno=-1
nr_alunos=int(input("numero de alunos"))
for i in range(nr_alunos):
    nota=int(input("nota do alunos"))
    if nota > melhor_nota:
        melhor_nota=nota
        numero_aluno=i+1
print("O aluno com melhor nota é o nº",numero_aluno)