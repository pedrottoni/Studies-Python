"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
"""
student = {}

student["Nome"] = str(input("Nome: "))
student["Média"] = float(input(f"Média de {student['Nome']}: "))

if student["Média"] < 5:
    student["Situação"] = "Reprovado"
elif 5 <= student["Média"] < 7:
    student["Situação"] = "Recuperação"
else:
    student["Situação"] = "Aprovado"

print("-=-"*10)

for k, v in student.items():
    print(f"{k}: {v}")

print("-=-"*10)
