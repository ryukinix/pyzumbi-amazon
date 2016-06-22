x = float(input("Digite um comprimento em metros: "))
y = x * 1000
if y.is_integer() == True:
    y = int(y)
print('%d equivale em milimetros: ' %x, y,'(mm)') 
