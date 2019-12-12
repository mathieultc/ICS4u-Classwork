# Recursion-1 > factorial (p154669)

from algorithm import factorial, fibonacci, bunnyEars, bunnyEars2, sumDigits, triangle, count7, count8, powerN, countX, countHi, changeXY, noX, changePi, array6, array11, array220, allStar, pairStar, endX, countAbc

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

#changXY
def test_0():
    assert changeXY("codex") == "codey"

def test_1():
    assert changeXY("xxhixx") == "yyhiyy"

def test_2():
    assert changeXY("xhixhix") == "yhiyhiy"

def test_3():
    assert changeXY("hiy") == "hiy"

def test_4():
    assert changeXY("h") == "h"

def test_5():
    assert changeXY("x") == "y"

def test_6():
    assert changeXY("") == ""

def test_7():
    assert changeXY("xxx") == "yyy"

def test_8():
    assert changeXY("yyhxyi") == "yyhyyi"

def test_9():
    assert changeXY("hihi") == "hihi"

#noX
def test_0():
    assert noX("xaxb") == "ab"

def test_1():
    assert noX("abc") == "abc"

def test_2():
    assert noX("xx") == ""

def test_3():
    assert noX("") == ""

def test_4():
    assert noX("axxbxx") == "ab"

def test_5():
    assert noX("Hellox") == "Hello"

#changePi

def test_0():
    assert changePi("xpix") == "x3.14x"

def test_1():
    assert changePi("pipi") == "3.143.14"

def test_2():
    assert changePi("pip") == "3.14p"

def test_3():
    assert changePi("pi") == "3.14"

def test_4():
    assert changePi("hip") == "hip"

def test_5():
    assert changePi("p") == "p"

def test_6():
    assert changePi("x") == "x"

def test_7():
    assert changePi("") == ""

def test_8():
    assert changePi("pixx") == "3.14xx"

def test_9():
    assert changePi("xyzzy") == "xyzzy"


#array6

def test_0():
    assert array6([1, 6, 4], 0) == True

def test_1():
    assert array6([1, 4], 0) == False

def test_2():
    assert array6([6], 0) == True

def test_3():
    assert array6([], 0) == False

def test_4():
    assert array6([6, 2, 2], 0) == True

def test_5():
    assert array6([2, 5], 0) == False

def test_6():
    assert array6([1, 9, 4, 6, 6], 0) == True

def test_7():
    assert array6([2, 5, 6], 0) == True


#array11
def test_0():
    assert array11([1, 2, 11], 0) == 1

def test_1():
    assert array11([11, 11], 0) == 2

def test_2():
    assert array11([1, 2, 3, 4], 0) == 0

def test_3():
    assert array11([1, 11, 3, 11, 11], 0) == 3

def test_4():
    assert array11([11], 0) == 1

def test_5():
    assert array11([1], 0) == 0

def test_6():
    assert array11([], 0) == 0

def test_7():
    assert array11([11, 2, 3, 4, 11, 5], 0) == 2

def test_8():
    assert array11([11, 5, 11], 0) == 2


#array220
def test_0():
    assert array220([1, 2, 20], 0) == True

def test_1():
    assert array220([3, 30], 0) == True

def test_2():
    assert array220([3], 0) == False

def test_3():
    assert array220([], 0) == False

def test_4():
    assert array220([3, 3, 30, 4], 0) == True

def test_5():
    assert array220([2, 19, 4], 0) == False

def test_6():
    assert array220([20, 2, 21], 0) == False

def test_7():
    assert array220([20, 2, 21, 210], 0) == True

def test_8():
    assert array220([2, 200, 2000], 0) == True

def test_9():
    assert array220([0, 0], 0) == True

def test_10():
    assert array220([1, 2, 3, 4, 5, 6], 0) == False

def test_11():
    assert array220([1, 2, 3, 4, 5, 50, 6], 0) == True

def test_12():
    assert array220([1, 2, 3, 4, 5, 51, 6], 0) == False

def test_13():
    assert array220([1, 2, 3, 4, 4, 50, 500, 6], 0) == True


#allStar
def test_0():
    assert allStar("hello") == "h*e*l*l*o"

def test_1():
    assert allStar("abc") == "a*b*c"

def test_2():
    assert allStar("ab") == "a*b"

def test_3():
    assert allStar("a") == "a"

def test_4():
    assert allStar("") == ""

def test_5():
    assert allStar("3.14") == "3*.*1*4"

def test_6():
    assert allStar("Chocolate") == "C*h*o*c*o*l*a*t*e"

def test_7():
    assert allStar("1234") == "1*2*3*4"


#pairStar

def test_0():
    assert pairStar("hello") == "hel*lo"

def test_1():
    assert pairStar("xxyy") == "x*xy*y"

def test_2():
    assert pairStar("aaaa") == "a*a*a*a"

def test_3():
    assert pairStar("aaab") == "a*a*ab"

def test_4():
    assert pairStar("aa") == "a*a"

def test_5():
    assert pairStar("a") == "a"

def test_6():
    assert pairStar("") == ""

def test_7():
    assert pairStar("noadjacent") == "noadjacent"

def test_8():
    assert pairStar("abba") == "ab*ba"

def test_9():
    assert pairStar("abbba") == "ab*b*ba"

#endX
def test_0():
    assert endX("xxre") == "rexx"

def test_1():
    assert endX("xxhixx") == "hixxxx"

def test_2():
    assert endX("xhixhix") == "hihixxx"

def test_3():
    assert endX("hiy") == "hiy"

def test_4():
    assert endX("h") == "h"

def test_5():
    assert endX("x") == "x"

def test_6():
    assert endX("xx") == "xx"

def test_7():
    assert endX("") == ""

def test_8():
    assert endX("bxx") == "bxx"

def test_9():
    assert endX("bxax") == "baxx"

def test_10():
    assert endX("axaxax") == "aaaxxx"

def test_11():
    assert endX("xxhxi") == "hixxx"

#countAbc
def test_0():
    assert countAbc("abc") == 1

def test_1():
    assert countAbc("abcxxabc") == 2

def test_2():
    assert countAbc("abaxxaba") == 2

def test_3():
    assert countAbc("ababc") == 2

def test_4():
    assert countAbc("abxbc") == 0

def test_5():
    assert countAbc("aaabc") == 1

def test_6():
    assert countAbc("hello") == 0

def test_7():
    assert countAbc("") == 0

def test_8():
    assert countAbc("ab") == 0

def test_9():
    assert countAbc("aba") == 1

def test_10():
    assert countAbc("aca") == 0

def test_11():
    assert countAbc("aaa") == 0