# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

firstStudent = str(input("Digite o neme de um aluno para ser sorteado: "))
secondStudent = str(input("Digite o neme de outro aluno para ser sorteado: "))
thirdStudent = str(input("Digite o neme de outro aluno para ser sorteado: "))
fourthStudent = str(input("Digite o neme de outro aluno para ser sorteado: "))

print(
    f"O aluno escolhido foi {random.choice([firstStudent,secondStudent,thirdStudent,fourthStudent])}")
