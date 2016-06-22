import urllib.request
pagina = urllib.request.urlopen(
         'http://beans.itcarlow.ie/prices.html') 
texto = pagina.read().decode('utf8')
texto = texto.splitlines()
for c in texto:
    if "price" in c:
        texto = c
        break
n = 0
price = ''
while (n < len(texto)):
    if texto[n] == '$':
        while (texto[n] != '<'):
            price += texto[n]
            n += 1
        break
    n += 1
print(price[1:])

