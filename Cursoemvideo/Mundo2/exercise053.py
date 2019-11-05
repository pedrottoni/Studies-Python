'''
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Uma maneira alternativa é com o "sentence[::-1]"
'''
sentence = input('Digite uma frase: ').upper().replace(" ", "")
sentence_length = len(sentence)
sentence_inverse = ''

for i in range(sentence_length-1, -1, -1):
    sentence_inverse += sentence[i]

print(
    f'O inverso de \033[1;33m{sentence}\033[m é: \033[1;31m{sentence_inverse}\033[m')

if sentence == sentence_inverse:
    print('Temos um palíndromo')
else:
    print('A frase não é um palíndromo')
