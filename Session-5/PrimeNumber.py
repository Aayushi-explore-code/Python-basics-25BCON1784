n = 29
is_prime = 1

if n <= 1:
    is_prime = 0
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = 0
            break

if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")