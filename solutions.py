import itertools
import timeit
import math

def problem_1():
    """Find the sum of all the multiples of 3 or 5 below 1000 """
    total = 0
    for i in range(3, 1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total 

def problem_2():
    """Sum of fibonacci sequence whose do not exceed 4 millions and are even"""
    fib_sequence = [1,2]        

    while fib_sequence[-1] < 4*10**6:
        fib_sequence.append(sum(fib_sequence[-2:]))

    #print fib_sequence
    return sum([fib if fib%2 == 0 else 0 for fib in fib_sequence[:-1]])

def is_palindrome(number):
        return number == int(str(number)[::-1])

def problem_4():
    """Largest palindrome made from the product of two 3-digit numbers"""
    biggest = 0
    
    for i,j in itertools.product(range(100, 1000), range(100, 1000)): 
        candidate = i*j    
        if is_palindrome(candidate):
            if candidate > biggest:
                biggest = candidate

    return biggest

def problem_25():
    """Find the first Fibonacci term with 1000 digits"""
    fib_sequence = [1,1,2]        

    while fib_sequence[-1] < 10**999:
        fib_sequence.append(sum(fib_sequence[-2:]))

    return len(fib_sequence)

def problem_36():
    """Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2"""
    def is_bin_palindrome(number):
        return (bin(number)[2:] == bin(number)[2:][::-1])

    return sum([i if is_palindrome(i) and is_bin_palindrome(i) else 0 for i in range(1*10**6)])

if __name__ == '__main__':
    implemented = [1,2,4,25,36]

    for i in implemented:
        func = locals()["problem_"+str(i)]
        print "problem_"+str(i)+":"
        print func.__doc__
        print func()

        print "--"

