player_number = int(input('Escolha um número entre 1 e 300: '))
min = 1
max = 300
computer_number = 0
attempts = 0

while computer_number != player_number:
    computer_number = int((max + min) / 2)
    if player_number < computer_number:
        max = computer_number - 1
    else:
        min = computer_number + 1
    attempts += 1
    print(computer_number)

print(f'O computador acertou em {attempts} tentativas')
