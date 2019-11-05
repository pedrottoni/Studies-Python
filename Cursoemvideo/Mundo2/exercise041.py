'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM - Azul
- Até 14 anos: INFANTIL - Amarelo
- Até 19 anos: JÚNIOR - Verde
- Até 25 anos: SÊNIOR - Vermelho
- Acima de 25 anos: MASTER - Preto com fundo branco
'''
import datetime

swimmer_birth = int(input('Ano do nascimento: '))
swimmer_age = datetime.date.today().year - swimmer_birth

print(f'O nadador tem: {swimmer_age} anos')

if swimmer_age <= 9:
    print('Classificação: \033[1;34mMIRIM\033[m')
elif 9 < swimmer_age <= 14:
    print('Classificação: \033[1;33mINFANTIL\033[m')
elif 14 < swimmer_age <= 19:
    print('Classificação: \033[1;32mJÚNIOR\033[m')
elif 19 < swimmer_age <= 25:
    print('Classificação: \033[1;31mSÊNIOR\033[m')
else:
    print('Classificação: \033[7;97;40mMASTER\033[m')
