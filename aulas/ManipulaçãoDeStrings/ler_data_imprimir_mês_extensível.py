#ler dd/mm/aaaa e imprimir a data com mês escrito por extenso.
meses = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio','Junho',
		 'Julho', 'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']
entry = input('Insira a sua data de nascimento na forma dd/mm/aaaa: ')
split = entry.split('/')

dia = split[0]
mes = meses[int(split[1]) - 1]
ano = split[2]

print('Você nasceu no dia %s de %s de %s' %(dia, mes, ano))
