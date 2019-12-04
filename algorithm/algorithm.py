"""
- Recursion: having a function call it itself
- Base case: What is the final end-point of this algorithm?
- Recursive case: Call the function again. (algorithm not complete)
"""


def count_down(n):
    if n == 0: #base case
        return

    print(n)

    count_down(n-1)# recursive case


def sum_up_to(n: int) -> int:
    if n == 1: #base case
        return 1

    return n + sum_up_to(n-1) #recursive case 
  

def factorial(n: int) -> int:
    if n == 1:
        return 1 #base case
    elif n == 0:
        return 1 #base case

    return n * factorial(n - 1) #recursive case


def fibonacci(n: int) -> int:
    if n == 0:
        return 0 #base case
    if n == 1:
        return 1 #base case

    return fibonacci(n-1) + fibonacci(n-2) #recursive case


def bunnyEars(n: int) -> int:
    if n == 1:
        return 2 #base case
    elif n == 0:
        return 0

    return 2 + bunnyEars(n-1) #recursive case


def bunnyEars2(n: int) -> int:
    if n == 0: #base case
        return 0
    elif n % 2 == 0:
        return 3 + bunnyEars2(n-1) #recursive case
    else:
        return 2 + bunnyEars2(n-1)


def triangle(n: int) -> int:
    if n == 0: 
        return 0 #base case
    elif n == 1: 
        return 1

    return n + triangle(n-1) #recursive case


def sumDigits(n: int) -> int:
    if n < 10: #base case
        return n

    return n % 10 + sumDigits(n//10) #recursive case


def count7(n: int) -> int:
    if n == 7:
        return  1
    elif str(7) not in str(n):
        return 0
    elif n % 10 == 7:
        return 1 + count7(n//10)
    else:
        return count7(n//10)


def count8(n: int) -> int:
    if n == 8:
        return 1

    elif str(8) not in str(n):
        return 0

    elif n % 100 == 88:
        return 3 + count8(n//100)

    elif n % 10 == 8:
        return 1 + count8(n//10)
    
    else:
        return count8(n//10)


def powerN(base: int, n: int) -> int:
    if n == 0: #base case
        return 1
    
    elif n == 1:
        return base

    return base * powerN(base, n - 1) #recursive case


 



   
