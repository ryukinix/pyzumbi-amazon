#!/usr/bin/python3
#Tempo_Estimado_de_Download
#Autor: Manoel Vilela| manoel_vilela@engineer.com | Última atualização: 12:17 (19/05/2014)
from time import sleep
print("Isto é uma calculadora que estimará o tempo de um download.")
print("Informe a sua velocidade de internet junto com a grandeza, exemplo:\n30MB (Megabyte);\n30KB (Kilobyte);\n15Mbps (Megabits por segundo);\n15KB/s (Kilobytes por segundo)")
size = input('Qual o tamanho do arquivo a ser baixado?')
link = input('Qual a velocidade da sua internet?')
size_str = size
link_str = link
a = 2 ** 10

def reduce(string):
    n = -1
    while abs(n) <= len(string):
        if string[n].isalpha() is True:
            index = string[n]
        n = n -1
    tupla = string.partition(index)
    lista = list(tupla).pop(0)
    link = int(lista)
    return link  

size = reduce(size)
link = reduce(link)

if "GB" in size_str.upper():
    if "MB" in link_str.upper():
        size = size * a
    elif "KB" in link_str.upper():
        size = size * a ** 2
elif "MB" in size_str.upper():
    if "GB" in link_str.upper():
        size = size * a ** (-1)
    elif "KB" in link_str.upper():
        size = size * a 
elif "KB" in size_str.upper():
    if "GB" in link_str.upper():
        size = size * a ** (-2)
    elif "MB" in link_str.upper():
        size = size * a 
if "b" in link_str:
    size = size * 8

time = size / link

if time < 60:
    print('O tempo estimado de download é de %.2f segundos.' %time)
elif time < 60 ** 2:
    time_m = time / 60
    print('O tempo estimado de download é de %.2f minutos.' %time_m)
else:
    time_h = time/ 60 ** 2
    print ('O tempo estimado de download é de %.2f hora(s)' %time_h)
sleep(10)

#A função *reduce* reduz a string em apenas números(beta). 
#Deve ser melhorado pra ser usado em qualquer ocorrência de caracteres e números(não implementado) - implementado.
