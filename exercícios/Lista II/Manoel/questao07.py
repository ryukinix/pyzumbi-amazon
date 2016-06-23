tamanho = int(input("Qual o tamanho em m² da área a ser pintada?"))
tinta_necessaria = 3 * tamanho
lata_tinta, lata_preço = 18, 80
quant_latas = tinta_necessaria / lata_tinta
if type(quant_latas) == float:
    quant_latas = quant_latas +1
    preço_total = quant_latas * lata_preço
    print("Quantidade de latas necessarias: %d \nPreço total: R$%.2f" %(quant_latas , preço_total))
else:
    preço_total = quant_latas * lata_preço
    print("Quantidade de latas necessarias: %d \nPreço total: R$%.2f" %(quant_latas, preço_total))
