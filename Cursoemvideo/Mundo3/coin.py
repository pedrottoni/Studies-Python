def coin(function="0"):
    sign = "R$" + str(function)
    sign = sign.replace(".", ",")
    sign = sign.split(",")
    if len(sign) > 1:
        sign_float = sign[1]
        if len(sign_float) < 2:
            return sign[0] + "," + sign_float[0:2] + "0"
        return sign[0] + "," + sign_float[0:2]
    return sign[0] + ",00"


def string_to_float(number="0"):
    float_number = float(number.replace(",", "."))
    return float_number


def increase(number, inc):
    return coin(string_to_float(number) + ((inc / 100) * string_to_float(number)))


def decrease(number, dec):
    return coin(string_to_float(number) - ((dec / 100) * string_to_float(number)))


def double(number="0"):
    return coin(string_to_float(number) * 2)


def half(number="0"):
    return coin(string_to_float(number) / 2)


def resume(number="0", inc=10, dec=10):
    print (f'{"-"*35}\n{"Resumo do Valor".center(35)}\n{"-"*35}\n{"A metade de " + coin(number) + ":"}\t{half(number)}\n{"O dobro de " + coin(number) + ":"}\t{double(number)}\n{"Aumentando " + str(inc) + "%, temos:"}\t{increase(number, inc)}\n{"Diminuindo " + str(dec) + "%, temos:"}\t{decrease(number, dec)}')
