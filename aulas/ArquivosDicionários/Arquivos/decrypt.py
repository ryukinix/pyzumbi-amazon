x = input('Digite a mensagem criptografada: ')
s = ''
for y in x:
    s += chr(ord(y) - 30000)
print('Foi identificado cachorrês na mensagem.\nEm português ficaria: ', s)
