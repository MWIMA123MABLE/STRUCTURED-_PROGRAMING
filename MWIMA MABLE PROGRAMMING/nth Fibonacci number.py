def fibonacci(n):
  """Calculates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate (starting from 1).

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    raise ValueError("n must be a positive integer")
  elif n == 1 or n == 2:
    return 1
  else:
    fib_n_minus_1, fib_n_minus_2 = 1, 1
    for _ in range(3, n + 1):
      fib_n = fib_n_minus_1 + fib_n_minus_2
      fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n
    return fib_n

# Get the desired Fibonacci number from the user
n = int(input("Enter the desired Fibonacci number (n): "))

# Calculate and print the result
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")