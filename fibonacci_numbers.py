"""Author: Brandon Barrett
Program: Fibonacci Numbers
Description: A program to generate fibonacci numbers 1 - 4 million and take the sum of even values
Date: October 4, 2026"""


first_number = 1
second_number = 2
fibonacci_number = first_number + second_number
fibonacci_sequence = [first_number, second_number, fibonacci_number]
fibonacci_result = [first_number, second_number, fibonacci_number]
even_fibonacci = []

for x in range(0, 29):
    fibonacci_sequence.remove(first_number)
    first_number = fibonacci_sequence[0]
    second_number = fibonacci_sequence[1]
    fibonacci_number = first_number + second_number
    fibonacci_sequence.append(fibonacci_number)
    fibonacci_result.append(fibonacci_number)

for even in fibonacci_result:
    if even % 2 == 0:
        even_fibonacci.append(even)

print(
    f"Sum of all even numbered values from fibonacci sequence: {sum(even_fibonacci)}")
