# Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.

# 0 -> 0, 5 -> 5, 10 -> 55


def the_Fibonacci_sequence(rame):
    if rame <= 1:
        return rame
    
    return the_Fibonacci_sequence(rame - 1) + the_Fibonacci_sequence(rame - 2)


print(the_Fibonacci_sequence(0))
print(the_Fibonacci_sequence(5))
print(the_Fibonacci_sequence(10))