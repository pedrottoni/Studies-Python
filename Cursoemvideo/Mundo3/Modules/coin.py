def string_to_float(number="0"):
    float_number = float(number.replace(",", "."))
    return float_number


def increase(number="0"):
    return string_to_float(number) + ((10 / 100) * string_to_float(number))


def decrease(number="0"):
    return string_to_float(number) - ((10 / 100) * string_to_float(number))


def double(number="0"):
    return string_to_float(number) * 2


def half(number="0"):
    return string_to_float(number) / 2


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
