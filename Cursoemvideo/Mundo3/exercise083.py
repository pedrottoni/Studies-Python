"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""
bracket = []

expression = str(input("Digite sua expressão: "))

for element in expression:
    if element == "(":
        bracket.append(element)
    elif element == ")":
        if bracket.count("(") == 0:
            bracket.append(")")
            break
        bracket.pop()

if len(bracket) != 0:
    print("Expressão inválida")
else:
    print("Expressão válida")
