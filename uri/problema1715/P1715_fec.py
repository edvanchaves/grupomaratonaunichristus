cont = 0
entrada = input()
valores = entrada.split(" ")

n = int(valores[0]) #quantidade de jogadores
m = int(valores[1])  #quantidade de partidas
 
totalgols = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)
    totalgols.append(linha)
    
#para cada jogador, determina quantos gols por partida ele fez    
for i in range(n):
    gols = input() #gols marcados pelo jogador I
    vgols = gols.split(" ")
    for j in range(m):
        totalgols[i][j] = int(vgols[j])
 
 
#determina quem fez gols em todas as partidas
for i in range(n):
    naoFezGol = False
    for j in range(m):
        if totalgols[i][j] == 0:
            naoFezGol = True
    if naoFezGol == False:
        cont = cont + 1
 
print(cont)
