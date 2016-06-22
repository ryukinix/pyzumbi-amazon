mercadoria = int(input('Digite o valor da mercadoria: '))
desconto = int(input('Digite o valor do desconto em %: '))
new_price = mercadoria - desconto*mercadoria/100
print('O preço da mercadoria com desconto é: R$%.2f' %new_price)
