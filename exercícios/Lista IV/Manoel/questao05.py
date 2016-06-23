'''
	Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres.
	Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais. 
'''
#variáveis
text = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. 
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
text_clean = ''
k = 0

while k < len(text):    #remove caracteres especiais de 'text' gerando uma nova string 'text_clean'
	if text[k] not in '.,\n':
		text_clean = text_clean + text[k]
	k += 1

array = text_clean.split()

n = 0
for word in array:      #contador_de_palavras
	for x in 'python':
		if x in word.lower() and len(word) > 4:
			n += 1

print(text, '\n')
print("No texto acima, o número de palavras com mais de 4 caracteres formadas por alguma das letras contidas em 'python' é: %d" %n)
