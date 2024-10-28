opcao=("s")
duracao_t=float=0
while opcao==("s"):
    opcao=(input("deseija intrudosir mais musicas s se sim ou n se não"))
    if opcao==("n"):
        break
    duracao_s=int(input("Digite a duração da musica em sgundos"))
    duracao_t = duracao_t + duracao_s

duracao_m=duracao_t//60
duracao_s=float=duracao_t%60
print(duracao_m,",",duracao_s)