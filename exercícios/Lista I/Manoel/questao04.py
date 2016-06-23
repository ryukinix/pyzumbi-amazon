salário = int(input('Qual o salário? '))
p = int(input('Digite o aumento em %: '))
novo_salário = salário + p*salário/100
aumento = novo_salário - salário 
print("O aumento é R$%.2f e o novo salário é R$%.2f" %(aumento, novo_salário))
