def is_prime_iterative(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Contoh penggunaan
number = 29
print(f"{number} adalah bilangan prima? {is_prime_iterative(number)}")
