x = input('Digite uma mensagem a ser criptografada: ')
s = ''
for y in x:
    s += chr(ord(y) + 30000)
print('A mensagem criptografada é: ', s)
