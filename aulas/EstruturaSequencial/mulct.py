#Python!
#Cálculo de excesso
weight = int(input('Peso do peixe:'))
if weight > 50:
    excess = weight - 50
    mulct = excess * 4
    print ("O excesso foi de %dKG e a multa que deve ser paga é de R$%d." %(excess, mulct))
else:
    print ("ZERO")
