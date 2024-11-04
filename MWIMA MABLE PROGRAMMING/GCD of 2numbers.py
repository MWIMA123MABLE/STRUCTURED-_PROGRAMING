def gcd(m, n):
  

  while n != 0:
    m, n = n, m % n
  return m

# Example usage:
m = 48
n = 18
result = gcd(m, n)
print("The GCD of", m, "and", n, "is", result)