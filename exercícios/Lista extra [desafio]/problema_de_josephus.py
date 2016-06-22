#!C:\Python3.4\python.exe
# coding = utf-8
# Problema de Josephus
#
# Questão A. Problema de Josephus. Imagine que temos n pessoas dispostas em círculo. Suponha que as
# pessoas estão numeradas 1 a n no sentido horário. Começando com a pessoa de número 1, percorra o
# círculo no sentido horário e elimine cada m-ésima pessoa enquanto o círculo tiver duas ou mais pessoas.
# Qual o número do sobrevivente? Teste para n = 50 e m = 3, reposta 11.

def josephus(lista, n):
	lenght = len(lista)
	n = n - 1
	i = n 
	while lenght > 1:
		if n >= lenght:
			n = n % lenght
		f = lista[n];		
		lista.remove(f)
		lenght -= 1
		n += i		
	return lista

lista = list(range(1, 51));	m = 3
x = josephus(lista, m)
print(x)