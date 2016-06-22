#cálculo para peso ideal de uma pessoa
from time import sleep
while True:
    try:
        h = float(input("Qual sua altura?"))
        break
    except ValueError:
        print ("Não use vírgula! Use ponto")    
while True:
    sex = input("Você é homem ou mulher?")
    man_ideal = (72.7 * h) - 58
    woman_ideal = (62.1 * h) - 44.7
    if sex.upper() == "HOMEM":
        man_weight = int(input("Qual seu peso?"))
        if man_weight == man_ideal:
            print("%.2fKG? Seu peso é ideal!" %(man_ideal))            
            break
        elif man_weight > man_ideal:
            print("Hmm ... Você tá gordo. Melhor emagrecer, mano. Seu peso ideal é %.2fKG" %(man_ideal))
            break
        elif man_weight < man_ideal:
            print("Você come? Tem certeza? Não é o que parece. Você está desnutrido!\n%.2fKG deveria ser seu peso." %(man_ideal))            
            break
    elif sex.upper() == "MULHER":
        woman_weight = int(input("Qual seu peso?"))
        if woman_weight == woman_ideal:
            print("%.2fKG? Seu peso é ideal!" %(woman_ideal))            
            break
        elif woman_weight > woman_ideal:
            print("Hmm... Você tá gordinha. Melhor emagrecer, mana. Seu peso ideal é %.2fKG" %(woman_ideal))            
            break
        elif woman_weight < woman_ideal:
            print("Você come? Tem certeza? Não é o que parece. Você esta desnutrida!\n%.2fKG deveria ser seu peso." %(woman_ideal))            
            break
sleep(15)    
        
        
        
