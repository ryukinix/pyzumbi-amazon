#Python!
#Criador por Manoel Vilela | 28/04/2014 às 09:46 AM
weight = int(input('Peso do peixe:'))
if weight > 50:
    excess = weight - 50
    mulct = excess * 4
    print ("O excesso foi de %dKG e a multa que deve ser paga é de R$%d." %(excess, mulct))
else:
    print ("O excesso e a multa são equivalentes a ZERO")
