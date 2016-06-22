data = open('data_acme.txt', 'r')
relatorio = open('relatorio.txt', 'w')

def convert(n):
    return n / 2 ** 20
def percentual(n, total):
    return n * 100 / total

relatorio.write("ACME Inc. \t\t\t Uso do espaço em disco pelos usuários \n-----------------------------------------------------------------\n")
relatorio.write("Nr. \t Usuários \t Espaço utilizado \t % do uso\n")

total = 0
lista = data.read().split()
for c in lista:
    if c.isdigit():
        total += int(c)
total = convert(total)

n = 0
while (n < len(lista)/2):
    x = convert(int(lista[2*n + 1]))
    relatorio.write("%d \t %s  \t  %8.2f MB \t \t %5.2f%%\n" %(n +1, lista[2*n], x, percentual(x, total)))
    n += 1

media = total / len(lista)/2
relatorio.write("\nEspaço total ocupado: %.2f MB\n" %total)
relatorio.write("Espaço médio ocupado: %.2f MB\n" %media)

data.close()
relatorio.close()
