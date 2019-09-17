# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importa a biblioteca random
import random
# Pega o nome dos grupos:
firstStudent = str(input("Digite o nome de um grupo: "))
secondStudent = str(input("Digite o nome de outro grupo: "))
thirdStudent = str(input("Digite o nome de outro grupo: "))
fourthStudent = str(input("Digite o nome de outro grupo: "))
# Cria uma lista com os nomes dos grupos
lista = [firstStudent, secondStudent, thirdStudent, fourthStudent]
# Embaralha o nome dos grupos
random.shuffle(lista)
# Imprime na tela o programa
print(
    f"Com o SAMPLE: A ordem de apresentação será: {random.sample([firstStudent,secondStudent,thirdStudent,fourthStudent],k=4)}\nCom o SHUFFLE: A ordem de apresentação será: {lista}"
)
