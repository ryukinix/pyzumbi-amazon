#ler dd/mm/aaaa e imprimir a data com mês escrito por extenso.
dia, mes, ano = input('Insira a sua data de nascimento na forma dd/mm/aaaa: ').split('/')
meses = ['Janeiro','Fevereiro', 'Março', 'Abril', 'Maio','Junho',
		 'Julho', 'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = meses[int(mes) - 1]
print('Você nasceu no dia %s de %s de %s' %(dia, mes, ano))
