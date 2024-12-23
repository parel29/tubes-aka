def is_prime_recursive(n, i=2):
    if n <= 1:
        return False
    if i > int(n**0.5):
        return True
    if n % i == 0:
        return False
    return is_prime_recursive(n, i + 1)

# Contoh penggunaan
number = 28
print(f"{number} adalah bilangan prima? {is_prime_recursive(number)}")