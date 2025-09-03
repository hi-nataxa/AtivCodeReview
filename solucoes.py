def sao_anagramas(str1, str2):
    
   str1 = str1.lower()
   str2 = str2.lower()

  # 2. Verificar se os comprimentos são iguais
   if len(str1) != len(str2):
     return False

  # 3. Ordenar as strings e compará-las
   if sorted(str1) == sorted(str2):
     return True
   else:
     return False

print(sao_anagramas("amor", "roma"))
print(sao_anagramas("race", "cafe"))
print(sao_anagramas("gato", "cabra")) 

pass

def cifra_de_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():  
         
            if char.isupper():
                resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
            
            else:
                resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
        else:
           
            resultado += char
    
    return resultado

print(cifra_de_cesar("abc", 2))                  
print(cifra_de_cesar("xyz", 3))                  
print(cifra_de_cesar("Ataque ao Amanhecer!", 5)) 
    
   
pass

import string

def encontrar_maior_palavra(frase):
   
    pontuacao = string.punctuation
    palavras = frase.split()
    
    maior = ""
    for palavra in palavras:
        
        palavra_limpa = palavra.strip(pontuacao)
        
       
        if len(palavra_limpa) > len(maior):
            maior = palavra_limpa
    
    return maior



print(encontrar_maior_palavra("O rato roeu a roupa do rei de Roma"))      
print(encontrar_maior_palavra("A jornada de mil milhas começa com um único passo."))  
print(encontrar_maior_palavra("Seja forte e corajoso"))                  

    
pass