"""Author: Brandon Barrett
Program: Fibonacci Numbers
Description: A program to generate fibonacci numbers 1 - 4 million
Date: October 4, 2026"""

# make 2 lists one for the working fibo number (1st, 2nd, fibo) and another that stores everything after ever iteration

first_number = 1
second_number = 2
first_replacement = 0
second_replacement = 0
fibonacci_number = first_number + second_number
fibonacci_sequence = [first_number, second_number, fibonacci_number]
print(fibonacci_sequence)

# def even_fibo():
#    fibonacci_sequence.remove[0]

# for x in range(0, 4):
#    print(fibonacci_number)

fibonacci_sequence.remove(first_number)
first_number = fibonacci_sequence[0]
second_number = fibonacci_sequence[1]
fibonacci_number = first_number + second_number
fibonacci_sequence.append(fibonacci_number)
print(fibonacci_sequence)
