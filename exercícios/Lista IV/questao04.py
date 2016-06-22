'''
Seja o statement sobre diversidade: 

	“The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
	Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. 
	We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”.

Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “python”. 
Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas. 
'''

text = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. 
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. 
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
text_clean = ''
python_array = []
k = 0

while k < len(text):    #remove caracteres especiais de 'text' inserindo em 'text_clean'
	if text[k] not in '.,\n':
		text_clean = text_clean + text[k]
	k += 1

array = text_clean.split()

for word in array:      #gera uma lista de palavras que começam ou terminam com uma das letras formada por 'python'.
	for x in 'python':
		y = word.lower()[0] + word.lower()[-1]
		if x in y:
			python_array.append(word)

print(python_array)
