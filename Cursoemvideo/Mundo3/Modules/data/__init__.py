from Modules import coin

def money(value):
    number = str(input(value)).strip()
    while number.isnumeric() == False:
        number = str(input(value))
    return number

def percentage(value):
    number = input(value).strip()
    while number.isnumeric() == False:
        number = input(value)
    return float(number)