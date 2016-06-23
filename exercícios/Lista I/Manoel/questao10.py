#Python!
#Life countdown
#Consideração: 'Um fumante perde 10 minutos de vida a cada cigarro'
qtc = int(input('Qual a quantidade de cigarros fumados por dia?'))
anos = int(input('Por quantos anos já fumou? '))
days_lost =  ( 365 * anos / 144 ) * qtc
print('Essa pessoa perdeu cerca de %d dias da sua vida por causa do tabaco \nOu seja, aproximadamente %d anos!' %(days_lost, (days_lost / 365)))
