f = open('surf.txt')
notas = []
nomes = []
for linha in f:
    nome, pontos = linha.split()
    notas.append(float(pontos))
    nomes.append(nome)
f.close()
notas.sort(reverse=True)
nomes.sort(reverse=True)
print ('%s %4.2f' %(nomes[0], notas[0]))
print ('%s %4.2f' %(nomes[1], notas[1]))
print ('%s %4.2f' %(nomes[2], notas[2]))

