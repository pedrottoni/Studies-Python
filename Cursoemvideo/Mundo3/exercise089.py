"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""
students = []
student = 0
choice = True

while choice != "0":
    if choice == "1":
        students.append([str(input("Nome: "))])
        students[student].append(int(input("Nota 1: ")))
        students[student].append(int(input("Nota 2: ")))
        student += 1
    elif choice == "2":
        print(f"{'Nº':5}{'NOME':<10}{'MÉDIA':<10}")
        for s, position in enumerate(students):
            print(
                f"{s:<5}{students[s][0]:<10}{(students[s][1] + students[s][2]) / 2 } ")
        while True:
            choice = str(
                input("Digite o numero do aluno para ver suas notas ou [X] para voltar:\nEscolha: ")).upper()
            if choice == "X":
                break
            elif int(choice) < len(students):
                print(
                    f"As notas do aluno {students[int(choice)][0]} foram: {students[int(choice)][1:]}")
    choice = str(
        input("Acrescentar aluno: [1] - Ver medias: [2] - Sair: [0]\nEscolha: "))
