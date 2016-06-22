#método_comum
arquivo = open('numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()
#método_pythonic(way)
with open('numeros.txt') as f:
    print(f.read())
