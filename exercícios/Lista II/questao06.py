money_hour = int(input("Quanto você ganha por hora?"))
total_hour = int(input("Quantas horas você trabalhou esse mês?"))
brute_money = money_hour * total_hour
impost = 0.11 * brute_money
inss = 0.08 * brute_money
sindicate = 0.05 * brute_money
discounts = impost + inss + sindicate
liquid_money = brute_money - discounts
print("+Salário Bruto: R$%.2f \n-IR: R$%.2f \n-INSS: R$%.2f \n-Sindicato: R$%.2f \n+Salário Líquido: R$%.2f" %(brute_money, impost, inss, sindicate, liquid_money)) 
