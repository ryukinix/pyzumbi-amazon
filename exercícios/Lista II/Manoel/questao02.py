#Python!
#Criador por Manoel Vilela | 29/04/2014 às 18:41
year = int(input("Digite um ano a ser verificado:"))
if year%4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Esse ano é bissexto!")
else:
    print("Esse ano não é bissexto!")
