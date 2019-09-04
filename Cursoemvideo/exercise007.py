# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))

media = (primeiraNota + segundaNota) / 2

print(f"A media das notas digitadas é: {media:.1f}")
