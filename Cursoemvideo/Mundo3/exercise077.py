"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
words = "APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSOS"

for i in words:
    print(f"Na palavra {i} temos: ", end='')
    for w in i:
        # Complicando
        # if w == "A" or w == "E" or w == "I" or w == "O" or w == "U":
        # Descomplicando
        if w in "AEIOU":
            print(w, end=' ')
    print("")
