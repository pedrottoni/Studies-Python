def increase(number=0):
    return number + ((10 / 100) * number)


def decrease(number=0):
    return number - ((10 / 100) * number)


def double(number=0):
    return number * 2


def half(number=0):
    return number / 2


def string_to_float(number):
    number = float(number.replace(",", "."))
    return number


def coin(function):
    sign = "R$" + str(function)
    sign = sign.replace(".", ",")
    sign = sign.split(",")
    if len(sign) > 1:
        sign_float = sign[1]
        if len(sign_float) < 2:
            return sign[0] + "," + sign_float[0:2] + "0"
        return sign[0] + "," + sign_float[0:2]
    return sign[0] + ",00"
