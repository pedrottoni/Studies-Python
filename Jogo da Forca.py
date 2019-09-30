'''
V Receber 3 palavras
V Agrupar as 3 palavras
V Sortear uma das 3 palavras
- Receber uma letra
- Verificar se é uma letra
- Verificar se a letra é repetida
- Verificar se a letra pertence a palávra escolhida
- Verificar quantas letras faltam
-
-
-
'''

import random
# Receber 3 palavras
first_word = str(input('Digite uma palavra para ser sorteada: '))
second_word = str(input('Digite outra palavra para ser sorteada: '))
third_word = str(input('Digite outra palavra para ser sorteada: '))

# Agrupar as 3 palavras
word_group = [first_word, second_word, third_word]
# Sortear uma das 3 palavras
drawn_word = random.choice(word_group)


print(drawn_word)
