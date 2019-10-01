# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salary = float(input("Digite o salário do funcionário: R$"))
newSalary = salary + (salary * 15 / 100)

print(f"O novo salário do funcionário será de R${newSalary:.2f}")
