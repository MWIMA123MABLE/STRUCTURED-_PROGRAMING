def syracuse_sequence(n):
  """Generates the Syracuse sequence for a given starting value.

  Args:
    n: The starting value for the sequence.

  Returns:
    A list containing the Syracuse sequence.
  """

  sequence = [n]
  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n = 3 * n + 1
    sequence.append(n)
  return sequence

# Get the starting value from the user
starting_value = int(input("Enter a starting value: "))

# Generate and print the Syracuse sequence
sequence = syracuse_sequence(starting_value)
print(sequence)