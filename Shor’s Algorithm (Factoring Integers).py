from math import gcd
from random import randint

# Step 1: Choose random a
N = 15
a = randint(2, N-1)
while gcd(a, N) != 1:
    a = randint(2, N-1)

print("Chosen a:", a)

# Simulate f(x) = a^x mod N for x = 0 to 15
f = []
for x in range(16):
    val = pow(a, x, N)
    if val in f:
        break
    f.append(val)

print("Function values:", f)

# Guess the period r
r = len(f)
print("Estimated period r:", r)



if r % 2 == 0 and pow(a, r//2, N) != N - 1:
    factor1 = gcd(pow(a, r//2) - 1, N)
    factor2 = gcd(pow(a, r//2) + 1, N)
    print(f"Non-trivial factors of {N}: {factor1}, {factor2}")
else:
    print("Try again with a different 'a'")
