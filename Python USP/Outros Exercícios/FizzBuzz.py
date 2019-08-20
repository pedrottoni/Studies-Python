def fizzbuzz (nInt) :
    if nInt % 3 == 0 and nInt % 5 != 0 :
        return ("Fizz")
    if nInt % 5 == 0 and nInt % 3 != 0 :
        return ("Buzz")
    if nInt % 5 == 0 and nInt % 3 == 0 :
        return ("FizzBuzz")
    if nInt % 5 != 0 and nInt % 3 != 0 :
        return (nInt)
