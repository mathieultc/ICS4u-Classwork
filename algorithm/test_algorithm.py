# Recursion-1 > factorial (p154669)

from algorithm import factorial, fibonacci, bunnyEars, bunnyEars2, sumDigits, triangle, count7, count8, powerN, countX, countHi

#factorial
def test_0():
    assert factorial(1) == 1

def test_1():
    assert factorial(2) == 2

def test_2():
    assert factorial(3) == 6

def test_3():
    assert factorial(4) == 24

def test_4():
    assert factorial(5) == 120

def test_5():
    assert factorial(6) == 720

def test_6():
    assert factorial(7) == 5040

def test_7():
    assert factorial(8) == 40320

def test_8():
    assert factorial(12) == 479001600

#fibonacci
# Recursion-1 > fibonacci (p120015)


def test_0():
    assert fibonacci(0) == 0

def test_1():
    assert fibonacci(1) == 1

def test_2():
    assert fibonacci(2) == 1

def test_3():
    assert fibonacci(3) == 2

def test_4():
    assert fibonacci(4) == 3

def test_5():
    assert fibonacci(5) == 5

def test_6():
    assert fibonacci(6) == 8

def test_7():
    assert fibonacci(7) == 13


#bunny ears 
def test_0():
    assert bunnyEars(0) == 0

def test_1():
    assert bunnyEars(1) == 2

def test_2():
    assert bunnyEars(2) == 4

def test_3():
    assert bunnyEars(3) == 6

def test_4():
    assert bunnyEars(4) == 8

def test_5():
    assert bunnyEars(5) == 10

def test_6():
    assert bunnyEars(12) == 24

def test_7():
    assert bunnyEars(50) == 100

def test_8():
    assert bunnyEars(234) == 468

#bunny ears 2

def test_0():
    assert bunnyEars2(0) == 0

def test_1():
    assert bunnyEars2(1) == 2

def test_2():
    assert bunnyEars2(2) == 5

def test_3():
    assert bunnyEars2(3) == 7

def test_4():
    assert bunnyEars2(4) == 10

def test_5():
    assert bunnyEars2(5) == 12

def test_6():
    assert bunnyEars2(6) == 15

def test_7():
    assert bunnyEars2(10) == 25


#sumDigits
def test_0():
    assert sumDigits(126) == 9

def test_1():
    assert sumDigits(49) == 13

def test_2():
    assert sumDigits(12) == 3

def test_3():
    assert sumDigits(10) == 1

def test_4():
    assert sumDigits(1) == 1

def test_5():
    assert sumDigits(0) == 0

def test_6():
    assert sumDigits(730) == 10

def test_7():
    assert sumDigits(1111) == 4

def test_8():
    assert sumDigits(11111) == 5

def test_9():
    assert sumDigits(10110) == 3

def test_10():
    assert sumDigits(235) == 10


#triangle

def test_0():
    assert triangle(0) == 0

def test_1():
    assert triangle(1) == 1

def test_2():
    assert triangle(2) == 3

def test_3():
    assert triangle(3) == 6

def test_4():
    assert triangle(4) == 10

def test_5():
    assert triangle(5) == 15

def test_6():
    assert triangle(6) == 21

def test_7():
    assert triangle(7) == 28


#count7
def test_0():
    assert count7(717) == 2

def test_1():
    assert count7(7) == 1

def test_2():
    assert count7(123) == 0

def test_3():
    assert count7(77) == 2

def test_4():
    assert count7(7123) == 1

def test_5():
    assert count7(771237) == 3

def test_6():
    assert count7(771737) == 4

def test_7():
    assert count7(47571) == 2

def test_8():
    assert count7(777777) == 6

def test_9():
    assert count7(70701277) == 4

def test_10():
    assert count7(777576197) == 5

def test_11():
    assert count7(99999) == 0

def test_12():
    assert count7(99799) == 1


#count8
def test_0():
    assert count8(8) == 1

def test_1():
    assert count8(818) == 2

def test_2():
    assert count8(8818) == 4

def test_3():
    assert count8(8088) == 4

def test_4():
    assert count8(123) == 0

def test_5():
    assert count8(81238) == 2

def test_6():
    assert count8(88788) == 6

def test_7():
    assert count8(8234) == 1

def test_8():
    assert count8(2348) == 1

def test_9():
    assert count8(23884) == 3

def test_10():
    assert count8(0) == 0

def test_11():
    assert count8(1818188) == 5

def test_12():
    assert count8(8818181) == 5

def test_13():
    assert count8(1080) == 1

def test_14():
    assert count8(188) == 3

def test_15():
    assert count8(9898) == 2

def test_16():
    assert count8(78) == 1


#powerN
def test_0():
    assert powerN(3, 1) == 3

def test_1():
    assert powerN(3, 2) == 9

def test_2():
    assert powerN(3, 3) == 27

def test_3():
    assert powerN(2, 1) == 2

def test_4():
    assert powerN(2, 2) == 4

def test_5():
    assert powerN(2, 3) == 8

def test_6():
    assert powerN(2, 4) == 16

def test_7():
    assert powerN(2, 5) == 32

def test_8():
    assert powerN(10, 1) == 10

def test_9():
    assert powerN(10, 2) == 100

def test_10():
    assert powerN(10, 3) == 1000


#countx
def test_0():
    assert countX("xxhixx") == 4

def test_1():
    assert countX("xhixhix") == 3

def test_2():
    assert countX("hi") == 0

def test_3():
    assert countX("h") == 0

def test_4():
    assert countX("x") == 1

def test_5():
    assert countX("") == 0

def test_6():
    assert countX("hihi") == 0

def test_7():
    assert countX("hiAAhi12hi") == 0


##countHi
def test_0():
    assert countHi("xxhixx") == 1

def test_1():
    assert countHi("xhixhix") == 2

def test_2():
    assert countHi("hi") == 1

def test_3():
    assert countHi("hihih") == 2

def test_4():
    assert countHi("h") == 0

def test_5():
    assert countHi("") == 0

def test_6():
    assert countHi("ihihihihih") == 4

def test_7():
    assert countHi("ihihihihihi") == 5

def test_8():
    assert countHi("hiAAhi12hi") == 3

def test_9():
    assert countHi("xhixhxihihhhih") == 3

def test_10():
    assert countHi("ship") == 1