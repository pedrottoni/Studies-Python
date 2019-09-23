'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''
phrase = str(input('Digite uma frase: ').upper().strip())
print(f'A letra A aparece {phrase.count("A")} vezes na frase.\nA primeira letra A apareceu na posição: {phrase.find("A")+1}\nA última letra A apareceu na posição: {phrase.rfind("A")+1}')
