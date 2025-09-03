def sao_anagramas(string1, string2):
    str1 = string1.replace(" ", "").lower()
    str2 = string2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)



palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if sao_anagramas(palavra1, palavra2):
    print("São anagramas ")
else:
    print("Não são anagramas ")


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



mensagem = input("Digite a frase para aplicar a Cifra de César: ")
desloc = int(input("Digite o valor do deslocamento: "))

print("Mensagem criptografada:", cifra_de_cesar(mensagem, desloc))

    
   
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



frase = input("Digite uma frase: ")
print("A maior palavra é:", encontrar_maior_palavra(frase))
               
  
pass