def first(a):
  if type(a) == list or type(a) == tuple:
    return first(a[0])
  return a
def last(a):
  if type(a) == list or type(a) == tuple:
    return last(a[-1])
  return a
def extract(a, reverse = False):
  if reverse:
    return last(a)
  else:
    return first(a)
def max_num(lista, reverse = False):
  maior = lista[0]
  for num in lista:
    if extract(num, reverse) > extract(maior, reverse):
      maior = num
  return maior
def min_num(lista, reverse = False):
  menor = lista[0]
  for num in lista:
    if extract(num, reverse) < extract(menor, reverse):
      menor = num
  return menor
def sort_last(lista, reverse = False):
  maior = max_num(lista, reverse)
  antigo_menor = extract(min_num(lista, reverse), reverse) - 1
  lista_ordenada = []
  for i in lista:
    menor = maior
    for j in lista:
      if extract(j, reverse) < extract(menor, reverse) and extract(j, reverse) > extract(antigo_menor, reverse):
        menor = j
    lista_ordenada.append(menor)
    antigo_menor = menor

  return lista_ordenada